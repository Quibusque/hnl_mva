from hnl_mva_tools import *

if __name__ == '__main__':

    ntuples = read_json_file("cfg/ntuples.json")
    histograms = read_json_file("cfg/histograms.json")
    treename = "final_tree"
    weight_name = "tot_weight"

    for histo in histograms:
        plot(ntuples,treename,weight_name,histo)