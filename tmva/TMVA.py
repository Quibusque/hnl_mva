from ROOT import TMVA, TFile, TTree, TCut, TChain
from subprocess import call
import os
import re
import argparse

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation
from tensorflow.keras.optimizers import SGD

# if name is main
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    # add parser for input tree
    parser.add_argument(
        "-i", "--inputtree", type=str, help="Name of the input tree file path"
    )
    args = parser.parse_args()

    signal_file_name = args.inputtree
    signal_label = re.findall(r"(mN\d+p\d+_ctau\d+)", signal_file_name)[0]

    background_files = [
        "/home/CMS-T3/lunerti/hnl_ntuples_for_mva/tree_HnlToMuPi_prompt_QCD_Pt-20To30_MuEnrichedPt5_TuneCP5_13TeV-pythia8_tree.root",
        "/home/CMS-T3/lunerti/hnl_ntuples_for_mva/tree_HnlToMuPi_prompt_QCD_Pt-30To50_MuEnrichedPt5_TuneCP5_13TeV-pythia8_tree.root",
        "/home/CMS-T3/lunerti/hnl_ntuples_for_mva/tree_HnlToMuPi_prompt_QCD_Pt-50To80_MuEnrichedPt5_TuneCP5_13TeV-pythia8_tree.root",
        "/home/CMS-T3/lunerti/hnl_ntuples_for_mva/tree_HnlToMuPi_prompt_QCD_Pt-80To120_MuEnrichedPt5_TuneCP5_13TeV-pythia8_tree.root",
        "/home/CMS-T3/lunerti/hnl_ntuples_for_mva/tree_HnlToMuPi_prompt_QCD_Pt-120To170_MuEnrichedPt5_TuneCP5_13TeV-pythia8_tree.root",
        "/home/CMS-T3/lunerti/hnl_ntuples_for_mva/tree_HnlToMuPi_prompt_QCD_Pt-170To300_MuEnrichedPt5_TuneCP5_13TeV-pythia8_tree.root",
    ]
    treename = "final_tree"
    weight_name = "tot_weight"

    # read good_vars.txt for list of good_variables
    good_vars = []
    with open("good_vars.txt", "r") as f:
        for line in f:
            good_vars.append(line.strip())

    # remove C_pass_gen_matching from good_vars
    good_vars.remove("C_pass_gen_matching")

    # vertex vars are those with vertex in their name
    vertex_vars = [var for var in good_vars if re.search("vertex", var)]
    #!TMath::IsNaN(PT_1) && !TMath::IsNaN(PT_2)
    # make such a string for every variable in vertex_vars
    cut_string = ""
    for var in vertex_vars:
        cut_string += f"!TMath::IsNaN({var}) && "
    # cut the last && away
    cut_string = cut_string[:-4]

    # Generate model

    # Define model
    model = Sequential()
    model.add(Dense(64, activation="relu", input_dim=len(good_vars)))
    model.add(Dense(2, activation="softmax"))

    # Set loss and optimizer
    model.compile(
        loss="categorical_crossentropy",
        optimizer=SGD(learning_rate=0.01),
        weighted_metrics=[
            "accuracy",
        ],
    )

    # Store model to file
    model.save("modelClassification.h5")
    model.summary()

    # Setup TMVA
    TMVA.Tools.Instance()
    TMVA.PyMethodBase.PyInitialize()

    output = TFile.Open(f"TMVA_{signal_label}.root", "RECREATE")
    factory = TMVA.Factory(
        "TMVAClassification",
        output,
        "!V:!Silent:Color:DrawProgressBar:Transformations=D,G:AnalysisType=Classification",
    )

    # use TChain for multiple files
    background = TChain(treename)
    for bkg in background_files:
        background.Add(bkg)

    signal_file = TFile(signal_file_name)
    signal = signal_file.Get(treename)

    dataloader = TMVA.DataLoader("dataset")

    for var in good_vars:
        dataloader.AddVariable(var)

    # prepare dataloader
    dataloader.AddSignalTree(signal, 1.0)
    dataloader.AddBackgroundTree(background, 1.0)

    # splitting entries for training and testing
    n_signal = signal.GetEntries()
    n_background = background.GetEntries()
    split = 0.8
    train_sgn = int(n_signal * split)
    train_bkg = int(n_background * split)
    test_sgn = n_signal - train_sgn
    test_bkg = n_background - train_bkg

    # NormMode=EqualNumEvents, important
    dataloader.PrepareTrainingAndTestTree(
        TCut(cut_string),
        f"nTrain_Signal={train_sgn}:nTrain_Background={train_bkg}:nTest_Signal={test_sgn}:nTest_Background={test_bkg}:SplitMode=Random:NormMode=EqualNumEvents:!V",
    )
    dataloader.SetSignalWeightExpression(weight_name)
    dataloader.SetBackgroundWeightExpression(weight_name)

    # Book methods
    factory.BookMethod(
        dataloader, TMVA.Types.kFisher, "Fisher", "!H:!V:Fisher:VarTransform=D,G"
    )
    # add a BDT
    factory.BookMethod(
        dataloader,
        TMVA.Types.kBDT,
        "BDT",
        "!H:!V:NTrees=200:MinNodeSize=2.5%:MaxDepth=3:BoostType=AdaBoost:AdaBoostBeta=0.5:SeparationType=GiniIndex:nCuts=20",
    )
    factory.BookMethod(
        dataloader,
        TMVA.Types.kPyKeras,
        "PyKeras",
        "H:!V:VarTransform=D,G:FilenameModel=modelClassification.h5:FilenameTrainedModel=trainedModelClassification.h5:NumEpochs=25:BatchSize=64:TriesEarlyStopping=8",
    )

    # Run training, test and evaluation
    factory.TrainAllMethods()
    factory.TestAllMethods()
    factory.EvaluateAllMethods()
