# MVA for Ds->HNL analysis

## Getting Started
```bash
source /cvmfs/sft.cern.ch/lcg/views/dev4/latest/x86_64-centos7-gcc12-opt/setup.sh
python config.py ntuples_input_directory
```

It is also possible to configure the output directory path, with the `-o` option.

## Run

```bash
python analyze.py
```
It is also possible to configure the output directory path, with the `-o` option.

## Execution on vscode - using Remote Explorer (SSH)

Using the *vscode* editor, it is possible to configure the entire working environment using the 
"SSH - Remote Explorer" functionalities.

### Setting the local machine
Before starting configuring vscode, the *ssh_config* must be correctly setup to allow a 
correct ssh connection:
- The `ssh_config` file is located under `/etc/ssh/`, and allows the creation of aliases for 
different ssh setups. In our case, to configure it using the Bologna Tier3, simply add in the
bottom of this file:
```bash
Host bastion
  User <your_bastion_username>
  Hostname bastion.cnaf.infn.it
  ForwardX11 yes
  ForwardAgent yes
  IdentityFile ~/.ssh/<your_ssh_key>

Host tier3
  User <your_tier3_username>
  Hostname uibo-cms-01.cr.cnaf.infn.it
  ForwardX11 yes
  ForwardAgent yes
  ProxyJump bastion
  IdentityFile ~/.ssh/<your_ssh_key>
```
Where <your_xxx_username> is the username required to connect to those machines and <your_ssh_key> is the *private keys* used for authentication (instructions to authn with ssh keypair, [here](https://www.digitalocean.com/community/tutorials/how-to-configure-ssh-key-based-authentication-on-a-linux-server)).

After editing this file, you should be able to connect to the *tier3* machine by simply typing:
```bash
ssh tier3
```

### Setting the remote machine
If the previous step was successful, with the command `ssh tier3` you should be connected to the
remote Tier3 machine.  
To setup the working environment with all the libraries, add this lines to the `.bashrc` and 
`.bash_profile`:
- `.bashrc`:
```bash
if [ "$TERM_PROGRAM" == "vscode" ]; then
   source /cvmfs/sft.cern.ch/lcg/views/dev4/latest/x86_64-centos7-gcc12-opt/setup.sh
fi
```
- `.bash_profile`:
```bash
source /cvmfs/sft.cern.ch/lcg/views/dev4/latest/x86_64-centos7-gcc12-opt/setup.sh

if [ -f ~/.bashrc ]; then
    source ~/.bashrc
fi
```
NB: The `source ...` command in the `.bash_profile` MUST be used ONLY for the first connection 
to the remote machine with vscode. After everything is set, it is possible to remove it 
(especially if you don't need all the libraries to be loaded at every connection, even outside 
of vscode). All the other options are mandatory, even for the following connections.

### Setting the remote explorer on vscode
Now you are ready to configure vscode:

- Open your vscode editor, and click on the `Remote Explorer` icon on the iconbar (check if the 
Remote Explorer extension is installed on your local machine). If the ssh configuration (made on 
the previous step) was done correctly, you should see the `tier3` name displayed: clicking on 
the arrow next to the name will perform a ssh connection to the machine, directly on the vscode 
interface (and with no password)!

- Once the connection is established, install the following vscode extensions: `python` and `jupyter`. 
Then reboot the SSH connection.

- **All set**! When opening any `.ipynb` notebook, on the top-right corner, click on *select kernel* 
-> *select another kernel* -> *python environments*. Select the 
`Python 3.9.12 /cvmfs/sft-nightlies.cern.ch/lcg/views/...` kernel: it will remain as a default for all
the following connections. 

Now you can use jupyter normally, with all the dependencies installed! 

### Throubleshooting
If some step was not successful, it is important to fully delete the folder `.vscode-server` before 
retrying from scratch.