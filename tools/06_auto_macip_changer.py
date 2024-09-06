#!/usr/bin/env python

import subprocess
import argparse
import re
import random
import time

def get_arguments():
    parser = argparse.ArgumentParser(description="IP and MAC address changer tool")
    parser.add_argument("-i", "--interface", dest="interface", required=True, help="Network interface to change IP and MAC address")
    return parser.parse_args()

def check_interface_exists(interface):
    try:
        subprocess.check_output(["ifconfig", interface], stderr=subprocess.DEVNULL)
        return True
    except subprocess.CalledProcessError:
        return False

def generate_random_ip():
    
    return f"192.168.{random.randint(0, 255)}.{random.randint(1, 254)}"

def generate_random_mac():
    
    mac = [0x00, random.randint(0x00, 0x7f), random.randint(0x00, 0xff),
           random.randint(0x00, 0xff), random.randint(0x00, 0xff), random.randint(0x00, 0xff)]
    return ':'.join(map(lambda x: f"{x:02x}", mac))

def change_ip(interface, new_ip):
    print(f"[+] Changing IP address of interface {interface} to {new_ip}")
    subprocess.call(["ifconfig", interface, new_ip, "netmask", "255.255.255.0"])

def change_mac(interface, new_mac):
    print(f"[+] Changing MAC address of interface {interface} to {new_mac}")
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

def get_current_ip(interface):
    try:
        ifconfig_result = subprocess.check_output(["ifconfig", interface], stderr=subprocess.DEVNULL).decode("utf-8")
        ip_address_search_result = re.search(r"inet\s(\d+\.\d+\.\d+\.\d+)", ifconfig_result)
        if ip_address_search_result:
            return ip_address_search_result.group(1)
        else:
            print("[-] Could not read IP address.")
            return None
    except subprocess.CalledProcessError:
        print(f"[-] Could not execute 'ifconfig' for interface {interface}. Please check if the interface exists.")
        return None

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

def change_ip_mac_multiple_times(interface, times=5):
    for i in range(1, times + 1):
        print(f"\n=== Changing IP and MAC address for {interface} - Attempt {i}/{times} ===")
        
        
        new_ip = generate_random_ip()
        new_mac = generate_random_mac()

        
        current_ip = get_current_ip(interface)
        current_mac = get_current_mac(interface)

        if current_ip:
            print(f"[*] Current IP address: {current_ip}")
        if current_mac:
            print(f"[*] Current MAC address: {current_mac}")

        
        change_ip(interface, new_ip)
        change_mac(interface, new_mac)

        
        updated_ip = get_current_ip(interface)
        updated_mac = get_current_mac(interface)

        if updated_ip == new_ip:
            print(f"[+] Successfully changed IP address to: {updated_ip}")
        else:
            print("[-] Failed to change the IP address.")
        
        if updated_mac and updated_mac.lower() == new_mac.lower():
            print(f"[+] Successfully changed MAC address to: {updated_mac}")
        else:
            print("[-] Failed to change the MAC address.")
        
        
        time.sleep(1)  


options = get_arguments()


if not check_interface_exists(options.interface):
    print(f"[-] Interface '{options.interface}' does not exist. Exiting.")
else:
    
    change_ip_mac_multiple_times(options.interface, times=5)
