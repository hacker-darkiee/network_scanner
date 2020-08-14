#!/usr/bin/env python

import scapy.all as scapy

def scan(ip):
    # scapy.arping(ip) implementing this function
    arp_request=scapy.ARP(pdst=ip)
    print(arp_request.summary())
    # scapy.ls(arp_request) Checking list ip
    brodcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    # scapy.ls(brodcast) checking list for mac
    print(brodcast.summary())
scan("192.168.43.166")
