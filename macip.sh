#!/bin/bash

echo "
$ ./macip.sh
===============================================================================
                            macip | [Version]: 1.0.0
===============================================================================
                             [Twitter]: @ogyhacker
===============================================================================
"
ifconfig
ifconfig wlan0 down 
echo "enter your mac address here"
echo "00:00:00:00:00:00"
read mac
ifconfig wlan0 hw ether $mac
macchanger -e wlan0
macchanger -e wlan0
macchanger -e wlan0
macchanger -e wlan0
macchanger -e wlan0
ifconfig wlan0 up
ifconfig

echo "macaddress has been changed successfully"


echo "enter your ip here "
echo "000.00.0.0"
read ip
ifconfig wlan0 $ip
ifconfig

echo "macaddress and the Ip address has been changed successfully"
