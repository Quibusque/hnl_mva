import argparse
import json
import os
import files
import subprocess

def write_json_file(filename, data):
    """Write data to a JSON file."""
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('inputdir', type=str, help='Name of the input directory')
    args = parser.parse_args()

    inputdir = args.inputdir
    cfg = dict()
    cfg["background"] = [os.path.join(inputdir,x) for x in files.background_filenames]
    cfg["signal"] = [os.path.join(inputdir,x) for x in files.signal_filenames]

    outdir = "cfg"
    subprocess.call("mkdir -p {}".format(outdir),shell=True)
    # Write the data to the JSON file
    write_json_file(os.path.join(outdir,"ntuples.json"), cfg)

