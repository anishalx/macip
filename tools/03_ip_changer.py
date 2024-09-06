#!/usr/bin/env python

import subprocess
import argparse
import re

def get_arguments():
    parser = argparse.ArgumentParser(description="IP address changer tool")
    parser.add_argument("-i", "--interface", dest="interface", required=True, help="Interface to change its IP address")
    parser.add_argument("-ip", "--ipaddress", dest="new_ip", required=True, help="New IP address to assign")
    return parser.parse_args()

def check_interface_exists(interface):
    try:
        subprocess.check_output(["ifconfig", interface], stderr=subprocess.DEVNULL)
        return True
    except subprocess.CalledProcessError:
        return False

def validate_ip_address(ip):
    
    ip_regex = r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$"
    if re.match(ip_regex, ip):
        
        segments = ip.split('.')
        for segment in segments:
            if int(segment) > 255:
                return False
        return True
    else:
        return False

def change_ip(interface, new_ip):
    print(f"[+] Changing IP address of interface {interface} to {new_ip}")
    subprocess.call(["ifconfig", interface, new_ip, "netmask", "255.255.255.0"])

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


options = get_arguments()


if not check_interface_exists(options.interface):
    print(f"[-] Interface '{options.interface}' does not exist. Exiting.")
else:
    
    if not validate_ip_address(options.new_ip):
        print("[-] Invalid IP address format. Please provide a valid IP address (e.g., 192.168.1.1).")
    else:
        
        current_ip = get_current_ip(options.interface)
        if current_ip:
            print(f"[*] Current IP address of {options.interface}: {current_ip}")
        
        
        change_ip(options.interface, options.new_ip)
        
        
        updated_ip = get_current_ip(options.interface)
        if updated_ip == options.new_ip:
            print(f"[+] Successfully changed IP address to: {updated_ip}")
        else:
            print("[-] Failed to change the IP address.")
