import argparse
from script.hnl_mva_tools import read_json_file, plot, load_variables

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('-o', '--outputdir', type=str, default='plots', help= 'Name of the output plot directory, defaults to "plots"')
    args = parser.parse_args()

    ntuples = read_json_file("cfg/ntuples.json")
    histograms = read_json_file("cfg/histograms.json")
    treename = "final_tree"
    weight_name = "tot_weight"

    headers = [hdr["column_name"] for hdr in histograms]
    bkg_labels = [s[s.rfind("QCD_Pt-"):s.rfind("_MuEnriched")] for s in ntuples["background"]]
   
   #Load variables from ROOT files
    signal, background, sig_weight, bkg_weight = load_variables(ntuples, headers, treename, weight_name)
    
    #Plot variables
    for histo in histograms:
        plot(histo,signal,background,sig_weight,bkg_weight,bkg_labels=bkg_labels,out_dir=args.outputdir)