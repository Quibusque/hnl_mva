# matplotlib
import matplotlib.pyplot as plt
import awkward as ak
import json
import subprocess
import os
import sys
import numpy as np


def write_json_file(filename, data):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

def read_json_file(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
    return data

def plot(column_name,weight_name,stree,btrees,nbins,xlow,xhigh,xlabel):

    data_sig = stree.arrays(column_name)
    data_bkg = [btree.arrays(column_name) for btree in btrees]    

    weight_sig = stree.arrays(weight_name)
    weight_bkg = [btree.arrays(weight_name) for btree in btrees]

    sa = ak.flatten(data_sig,axis=None)
    ba = [ak.flatten(ba,axis=None) for ba in data_bkg]

    #probably there is a more clever way to initialize weights...
    sw = np.repeat(weight_sig.to_list(), [len(sublist.to_list()[column_name]) for sublist in data_sig])
    bw = [np.repeat(bw.to_list(), [len(sublist.to_list()[column_name]) for sublist in ba]) for (bw,ba) in zip(weight_bkg,data_bkg)]

    #...and to avoid having to do this
    sw = [x[weight_name] for x in sw]
    bw = [[x[weight_name] for x in b] for b in bw]

    bins = np.linspace(xlow, xhigh, nbins)

    bkg_labels = [s[s.rfind("QCD_Pt-"):s.rfind("_MuEnriched")] for s in ntuples["background"]]


    fig, ax = plt.subplots()

    ax.hist(sa, bins=bins, weights=sw, alpha=0.5, density=True, label='signal')
    ax.hist(ba, bins=bins, weights=bw, alpha=0.5, density=True, stacked=True, label=bkg_labels)
    
    ax.set_xlabel(xlabel)
    ax.set_ylabel('events')
    ax.set_title('')
    ax.legend()

    plt.xlim(xlow,xhigh)

    plt.show()
    
    outdir = "plots"
    subprocess.call("mkdir -p {}".format(outdir),shell=True)
    plt.savefig(os.path.join(outdir,column_name+".png"))
