import uproot
import matplotlib.pyplot as plt
import awkward as ak
import json
import subprocess
import os
import sys
import numpy as np
import mplhep as hep

plt.style.use(hep.style.CMS) #Attiva stile CMS

def write_json_file(filename, data):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

def read_json_file(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
    return data

def load_variables(ntuples_cfg, headers, treename, weight_name):
    sig = {} 
    bkg = {} 
    sig_weight = {} 
    bkg_weight = {}
    stree = uproot.open(ntuples_cfg["signal"][0])[treename]
    btrees = [uproot.open(bfn)[treename] for bfn in ntuples_cfg["background"]]
    data_sig = stree.arrays(headers)
    data_bkg = [btree.arrays(headers) for btree in btrees]    
    weight_sig = stree.arrays(weight_name)
    weight_bkg = [btree.arrays(weight_name) for btree in btrees]

    print("The following headers will be loaded: " + ', '.join(headers))
    for h in headers:
        print("Loading variable: " + h)
        ##signal
        sa = data_sig[h]
        sw = weight_sig[weight_name]
        #broadcast sw with sa to match the shape
        sw = ak.broadcast_arrays(sw, sa)[0]
        
        sig[h] = ak.flatten(sa)
        sig_weight[h] = ak.flatten(sw)

        ##background
        ba = [data_bkg[i][h] for i in range(len(data_bkg))]
        bw = [weight_bkg[i][weight_name] for i in range(len(weight_bkg))]
        #broadcast bw with ba to match the shape
        bw = [ak.broadcast_arrays(bw[i], ba[i])[0] for i in range(len(bw))]

        bkg[h] = [ak.flatten(ba[i]) for i in range(len(ba))]
        bkg_weight[h] = [ak.flatten(bw[i]) for i in range(len(bw))]
    print("Variables Loaded!")
    return sig, bkg, sig_weight, bkg_weight
    

def plot(histo_cfg,sig,bkg,sig_weight,bkg_weight,sig_labels="signal",bkg_labels=None,out_dir=None):

    column_name = histo_cfg["column_name"]
    nbins = histo_cfg["nbins"]
    xlow = histo_cfg["xlow"]
    xhigh = histo_cfg["xhigh"]
    xlabel = histo_cfg["xlabel"]
    
    bins = np.linspace(xlow, xhigh, nbins)

    fig, ax = plt.subplots()

    ax.hist(sig[column_name], bins=bins, weights=sig_weight[column_name], alpha=0.5, density=True, label=sig_labels)
    ax.hist(bkg[column_name], bins=bins, weights=bkg_weight[column_name], alpha=0.5, density=True, stacked=True, label=bkg_labels)
    
    ax.set_xlabel(xlabel)
    ax.set_ylabel('events')
    ax.set_title('')
    ax.legend()
    hep.cms.text("Test",fontsize=18,loc=0)
    plt.xlim(xlow,xhigh)

    ##plt.show() Non si può usare senza backend GUI
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)
    print("Saving plot for variable: " + column_name)    
    plt.savefig(os.path.join(out_dir,column_name+".png"))