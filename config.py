import argparse
import json
import os
import script.files as files
import subprocess
from script.hnl_mva_tools import write_json_file

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('inputdir', type=str, help='Name of the input directory')
    parser.add_argument('-o', '--outputdir', type=str, default='cfg', help= 'Name of the output config directory, defaults to "cfg"')
    args = parser.parse_args()

    inputdir = args.inputdir
    cfg = dict()
    cfg["background"] = [os.path.join(inputdir,x) for x in files.background_filenames]
    cfg["signal"] = [os.path.join(inputdir,x) for x in files.signal_filenames]

    if not os.path.exists(args.outputdir):
        os.makedirs(args.outputdir)
    # Write the data to the JSON file
    write_json_file(os.path.join(args.outputdir,"ntuples.json"), cfg)