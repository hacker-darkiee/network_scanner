#!/usr/bin/env python

import scapy.all as scapy
import argparse

def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t","--target",dest="target", help="Target IP / IP Range.")
    option = parser.parse_args()
    return option

def scan(ip):
    # scapy.arping(ip) implementing this function
    arp_request = scapy.ARP(pdst=ip)
    brodcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_brodcast = brodcast/arp_request
    answered_list = scapy.srp(arp_request_brodcast, timeout=1, verbose=False)[0]
    clients_list=[]
    for element in answered_list:
        clients_dict={"ip":element[1].psrc,"mac":element[1].hwsrc}
        clients_list.append(clients_dict)
        return clients_list

def print_results(result_list):
    print("IP\t\t\tMAC Address\n-----------------------------------------------")
    for client in result_list:
        print(client["ip"]+ "\t\t" + client["mac"])

option = get_arguments
scan_result = scan("option.target")
print_results(scan_result)
