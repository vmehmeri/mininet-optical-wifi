### Mininet-Optical-WiFi
Mininet-Optical-WiFi is a fork of Mininet-Wifi (wich is a fork of Mininet) which allows the using of both WiFi Stations and Access Points, as well as Optical ROADMs with LINC-OE switches (LINC switches with Optical Extensions). 

### Wireless Mininet User Manual  
[Access the User Manual](https://github.com/ramonfontes/manual-mininet-wifi/raw/master/mininet-wifi-draft-manual.pdf)

### Optical Features
The Optical Features are best used with ONOS. Refer to https://wiki.onosproject.org/display/ONOS/Packet+Optical+Tutorial for a tutorial on how to use it (you can skip the Packet Optical Dev Environment setup part, as Mininet-Optical-Wireless takes care of that).
  
## Installation  
step 1: $ sudo apt-get install git  
step 2: $ git clone https://github.com/vmehmeri/mininet-optical-wifi  
step 3: $ cd mininet-optical-wifi  
step 4: $ sudo util/install.sh -Wonfvl 
#### install.sh options:   
-W: wireless dependencies   
-n: mininet-wifi dependencies    
-o: optical dependencies (LINC-OE)    
-f: OpenFlow   
-v: OpenvSwitch   
-l: wmediumd   
   
## Note
Mininet-WiFi should work fine in any Ubuntu distribution from 14.04, but in some cases (only if you have problems when starting it) you have to stop NetworkManager with `stop network-manager` (you can also use `sudo systemctl stop network-manager` or `sudo service network-manager stop`).    

