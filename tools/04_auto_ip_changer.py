#!/usr/bin/env python

import subprocess
import argparse
import random
import re
import time

def get_arguments():
    parser = argparse.ArgumentParser(description="IP address changer tool")
    parser.add_argument("-i", "--interface", dest="interface", required=True, help="Interface to change its IP address")
    return parser.parse_args()

def check_interface_exists(interface):
    try:
        subprocess.check_output(["ifconfig", interface], stderr=subprocess.DEVNULL)
        return True
    except subprocess.CalledProcessError:
        return False

def generate_random_ip():
    
    return f"192.168.{random.randint(0, 255)}.{random.randint(1, 254)}"

def change_ip(interface, new_ip):
    try:
        subprocess.call(["ifconfig", interface, new_ip, "netmask", "255.255.255.0"])
    except Exception as e:
        print(f"[-] Failed to change IP address: {e}")

def get_current_ip(interface):
    try:
        ifconfig_result = subprocess.check_output(["ifconfig", interface], stderr=subprocess.DEVNULL).decode("utf-8")
        ip_address_search_result = re.search(r"inet\s(\d+\.\d+\.\d+\.\d+)", ifconfig_result)
        if ip_address_search_result:
            return ip_address_search_result.group(1)
        else:
            return None
    except subprocess.CalledProcessError:
        return None


options = get_arguments()


if not check_interface_exists(options.interface):
    print(f"[-] Interface '{options.interface}' does not exist. Exiting.")
else:
    
    current_ip = get_current_ip(options.interface)
    if current_ip:
        print(f"[*] Current IP address: {current_ip}")
    else:
        print(f"[-] Could not retrieve the current IP address.")

    
    for layer in range(1, 6):
        new_ip = generate_random_ip()
        print(f"\n[+] Changing IP address to: {new_ip}")
        
        
        change_ip(options.interface, new_ip)
        
        
        current_ip = get_current_ip(options.interface)
        if current_ip == new_ip:
            print(f"[+] Successfully changed to IP: {current_ip}")
        else:
            print(f"[-] Failed to change the IP address.")
        
        
        time.sleep(1)  
