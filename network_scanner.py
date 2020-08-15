#!/usr/bin/env python

import scapy.all as scapy

def scan(ip):
    # scapy.arping(ip) implementing this function
    arp_request = scapy.ARP(pdst=ip)
    brodcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_brodcast = brodcast/arp_request
    answered_list = scapy.srp(arp_request_brodcast, timeout=1, verbose=False)[0]
    print("IP\t\t\tMAC Address\n-----------------------------------------------")
    for element in answered_list:
        print(element[1].psrc + "\t\t" + element[1].hwsrc)
scan("192.168.43.166/24")
