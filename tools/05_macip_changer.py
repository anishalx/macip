#!/usr/bin/env python

import subprocess
import argparse
import re

def get_arguments():
    parser = argparse.ArgumentParser(description="IP and MAC address changer tool")
    parser.add_argument("-i", "--interface", dest="interface", required=True, help="Interface to change its IP and MAC address")
    parser.add_argument("-ip", "--ipaddress", dest="new_ip", required=True, help="New IP address to assign")
    parser.add_argument("-m", "--mac", dest="new_mac", required=True, help="New MAC address to assign")
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

def validate_mac_address(mac):
    mac_regex = r"^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$"
    if re.match(mac_regex, mac):
        return True
    else:
        print("[-] Invalid MAC address format. A valid MAC address is in the format XX:XX:XX:XX:XX:XX")
        return False

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


options = get_arguments()


if not check_interface_exists(options.interface):
    print(f"[-] Interface '{options.interface}' does not exist. Exiting.")
else:
    
    if not validate_ip_address(options.new_ip):
        print("[-] Invalid IP address format. Please provide a valid IP address (e.g., 192.168.1.1).")
    
    elif not validate_mac_address(options.new_mac):
        print("[-] Invalid MAC address format. Please provide a valid MAC address (e.g., 00:1A:2B:3C:4D:5E).")
    else:
        
        current_ip = get_current_ip(options.interface)
        current_mac = get_current_mac(options.interface)

        if current_ip:
            print(f"[*] Current IP address of {options.interface}: {current_ip}")
        if current_mac:
            print(f"[*] Current MAC address of {options.interface}: {current_mac}")
        
        
        change_ip(options.interface, options.new_ip)
        change_mac(options.interface, options.new_mac)
        
        
        updated_ip = get_current_ip(options.interface)
        updated_mac = get_current_mac(options.interface)

        if updated_ip == options.new_ip:
            print(f"[+] Successfully changed IP address to: {updated_ip}")
        else:
            print("[-] Failed to change the IP address.")
        
        if updated_mac and updated_mac.lower() == options.new_mac.lower():
            print(f"[+] Successfully changed MAC address to: {updated_mac}")
        else:
            print("[-] Failed to change the MAC address.")
