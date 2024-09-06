#!/usr/bin/env python

import subprocess
import argparse
import re
import random


def generate_random_mac():
    mac = [0x02, random.randint(0x00, 0x7f), random.randint(0x00, 0xff),
           random.randint(0x00, 0xff), random.randint(0x00, 0xff), random.randint(0x00, 0xff)]
    return ':'.join(map(lambda x: f"{x:02x}", mac))


def get_arguments():
    parser = argparse.ArgumentParser(description="MAC address changer tool for multiple layers")
    parser.add_argument("-i", "--interface", dest="interface", required=True, help="Network interface to change its MAC address multiple times with random MACs")
    return parser.parse_args()


def check_interface_exists(interface):
    try:
        subprocess.check_output(["ifconfig", interface], stderr=subprocess.DEVNULL)
        return True
    except subprocess.CalledProcessError:
        return False


def change_mac(interface, new_mac):
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
            print(f"[-] Could not read MAC address for {interface}.")
            return None
    except subprocess.CalledProcessError:
        print(f"[-] Could not execute 'ifconfig' for interface {interface}. Please check if the interface exists.")
        return None


def change_mac_multiple_times(interface, times=5):
    
    if not check_interface_exists(interface):
        print(f"[-] Interface '{interface}' does not exist. Exiting.")
        return
    
    print(f"[*] Starting MAC address change process for interface '{interface}'")

    
    for layer in range(times):
        random_mac = generate_random_mac()
        
        current_mac = get_current_mac(interface)
        print(f"\n[*] Current MAC: {current_mac} -> Changing to new random MAC: {random_mac}")
        
        change_mac(interface, random_mac)

        
        new_mac = get_current_mac(interface)
        if new_mac and new_mac.lower() == random_mac.lower():
            print(f"[+] MAC successfully changed to: {new_mac}")
        else:
            print(f"[-] Failed to change the MAC address for layer {layer + 1}.")

    print(f"\n[*] MAC address change process completed for '{interface}'.")


options = get_arguments()


change_mac_multiple_times(options.interface)
