#!/usr/bin/env python

import subprocess
import argparse
import re

def get_arguments():
    parser = argparse.ArgumentParser(description="MAC address changer tool")
    parser.add_argument("-i", "--interface", dest="interface", required=True, help="Interface to change its MAC address")
    parser.add_argument("-m", "--mac", dest="new_mac", required=True, help="New MAC address")
    return parser.parse_args()

def check_interface_exists(interface):
    try:
        subprocess.check_output(["ifconfig", interface], stderr=subprocess.DEVNULL)
        return True
    except subprocess.CalledProcessError:
        return False

def validate_mac_address(mac):
    mac_regex = r"^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$"
    if re.match(mac_regex, mac):
        return True
    else:
        print("[-] Invalid MAC address format. A valid MAC address is in the format XX:XX:XX:XX:XX:XX")
        return False

def change_mac(interface, new_mac):
    print(f"[+] Changing MAC address of interface {interface} to {new_mac}")
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

def get_current_mac(interface):
    try:
        ifconfig_result = subprocess.check_output(["ifconfig", interface], stderr=subprocess.DEVNULL).decode("utf-8")
        mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)
        if mac_address_search_result:
            return mac_address_search_result.group(0)
        else:
            print("[-] Could not read MAC address.")
            return None
    except subprocess.CalledProcessError:
        print(f"[-] Could not execute 'ifconfig' for interface {interface}. Please check if the interface exists.")
        return None


options = get_arguments()


if not check_interface_exists(options.interface):
    print(f"[-] Interface '{options.interface}' does not exist. Please check the available interfaces.")
elif not validate_mac_address(options.new_mac):
    print("[-] Provided MAC address is invalid.")
else:
    current_mac = get_current_mac(options.interface)
    print(f"[*] Your current MAC address is: {str(current_mac)}")
    
    
    change_mac(options.interface, options.new_mac)
    
    
    current_mac = get_current_mac(options.interface)
    if current_mac and current_mac.lower() == options.new_mac.lower():
        print(f"[+] MAC address was successfully changed to {current_mac}")
    else:
        print("[-] Failed to change the MAC address.")
