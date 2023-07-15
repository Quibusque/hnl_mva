import numpy as np
# pandas
import pandas as pd
# matplotlib
import matplotlib.pyplot as plt
import uproot
import mplhep
import awkward as ak
import glob
import json
import subprocess
import os

def read_json_file(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
    return data

def plot(column_name,stree,btrees,nbins,xlow,xhigh,xlabel):

    data_sig = stree.arrays(column_name)
    data_bkg = [btree.arrays(column_name) for btree in btrees]    

    sa = ak.flatten(data_sig,axis=None)
    ba = [ak.flatten(ba,axis=None) for ba in data_bkg]

    bins = np.linspace(xlow, xhigh, nbins)

    bkg_labels = [s[s.rfind("QCD_Pt-"):s.rfind("_MuEnriched")] for s in ntuples["background"]]


    fig, ax = plt.subplots()

    ax.hist(sa, bins=bins, alpha=0.5, density=True, label='signal')
    ax.hist(ba, bins=bins, alpha=0.5, density=True, stacked=True, label=bkg_labels)
    
    ax.set_xlabel(xlabel)
    ax.set_ylabel('events')
    ax.set_title('')
    ax.legend()

    plt.xlim(xlow,xhigh)

    plt.show()
    
    outdir = "plots"
    subprocess.call("mkdir -p {}".format(outdir),shell=True)
    plt.savefig(os.path.join(outdir,column_name+".png"))


if __name__ == '__main__':

    ntuples = read_json_file("cfg/ntuples.json")
    histograms = read_json_file("cfg/histograms.json")
    treename = "final_tree"

    stree = uproot.open(ntuples["signal"][0])[treename]
    btrees = [uproot.open(bfn)[treename] for bfn in ntuples["background"]]

    for histo in histograms:
        column_name = histo["column_name"]
        nbins = histo["nbins"]
        xlow = histo["xlow"]
        xhigh = histo["xhigh"]
        xlabel = histo["xlabel"]
        plot(column_name,stree,btrees,nbins,xlow,xhigh,xlabel)

