# macip

<h1>This tool is only work for the wlan0 interface </h1>
<h3>This will help you to change your macadress and the ip adress of your system .</h3> 
<h3>You can select your custom macadress(extra 5 layers) and ip adress</h3>

## Software Requirements:
The following OSs are officially supported:

- Debian 8+
- Kali Linux Rolling 2018.1+

The following OSs are likely able to run macip:

- Deepin 15+
- Fedora 22+
- Linux Mint
- Parrot Security
- Ubuntu 15.10+
- Void Linux

## Setup

### update your system

```bash
apt update
```

### upgrade your system

```bash
apt upgrade -y
```

### Git's Quick Install

**NOTE**:
- Installation must be done with superuser privileges. If you are not using the root account (as default with Kali Linux), prepend commands with `sudo` or change to the root user before beginning.
- Your package manager may be different to `apt`. You will also need an X server running, either on the system itself, or on your local system.

```bash
sudo apt-get -y install git
git clone https://github.com/anishalx/macip.git
```
### File permission
This will generate the output file for `macip.sh`.
To make that file executable .

```bash
chmod +x macip.sh
```
### launch the tool
You can launch the tool by using the file.

```bash
./macip.sh
```
## Example Usage

macip's Main Menu:


```bash
$ ./macip.sh
===============================================================================
                            macip | [Version]: 1.0.0
===============================================================================
                             [Twitter]: @ogyhacker
===============================================================================



wlan0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 00.00.00.0 netmask 255.255.252.0  broadcast 100.0.0.0
        inet6 fg80::dgh6:9jhe:3680:f582e  prefixlen 64  scopeid 0x20<link>
        ether 15:25:15:d9:87:c5  txqueuelen 1000  (Ethernet)
        RX packets 2188298  bytes 2588045471 (2.4 GiB)
        RX errors 0  dropped 4231  overruns 0  frame 0
        TX packets 333498  bytes 49251682 (46.9 MiB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

enter your mac address here
00:00:00:00:00:00
52:58:69:58:54:45

```



## SUCCESSFUL MACADDRESS CHANGED

```bash
Current MAC:   52:58:69:58:54:45 (unknown)
Permanent MAC: 50:28:4a:66:4a:22 (unknown)
New MAC:       50:58:69:f7:8d:76 (unknown)
Current MAC:   50:58:69:f7:8d:76 (unknown)
Permanent MAC: 50:28:4a:66:4a:22 (unknown)
New MAC:       50:58:69:b8:10:05 (unknown)
Current MAC:   50:58:69:b8:10:05 (unknown)
Permanent MAC: 50:28:4a:66:4a:22 (unknown)
New MAC:       50:58:69:77:a6:67 (unknown)
Current MAC:   50:58:69:77:a6:67 (unknown)
Permanent MAC: 50:28:4a:66:4a:22 (unknown)
New MAC:       50:58:69:35:9e:58 (unknown)
Current MAC:   50:58:69:35:9e:58 (unknown)
Permanent MAC: 50:28:4a:66:4a:22 (unknown)
New MAC:       50:58:69:d0:e9:27 (unknown)


wlan0: flags=4099<UP,BROADCAST,MULTICAST>  mtu 1500
        inet 00.00.0.0  netmask 255.255.252.0  broadcast 10.30.3.255
        inet6 fg80::dgh6:9jhe:3680:f582e  prefixlen 64  scopeid 0x20<link>
        ether 15:25:15:d9:87:c5  txqueuelen 1000  (Ethernet)
        RX packets 2188298  bytes 2588045471 (2.4 GiB)
        RX errors 0  dropped 4231  overruns 0  frame 0
        TX packets 333498  bytes 49251682 (46.9 MiB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

macaddress has been changed successfully

```

## IP ADDRESS CHANGE

```bash
enter your ip here 
000.00.0.0
198.25.36.22

wlan0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 198.25.36.22  netmask 255.255.255.0  broadcast 10.30.3.255
        inet6 fg80::dgh6:9jhe:3680:f582e  prefixlen 64  scopeid 0x20<link>
        ether 15:25:15:d9:87:c5  txqueuelen 1000  (Ethernet)
        RX packets 2194740  bytes 2596372978 (2.4 GiB)
        RX errors 0  dropped 4244  overruns 0  frame 0
        TX packets 334499  bytes 49408641 (47.1 MiB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

macaddress and the Ip address has been changed successfully

```

