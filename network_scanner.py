#!/usr/bin/env python

import scapy.all as scapy

def scan(ip):
    # scapy.arping(ip) implementing this function
    arp_request = scapy.ARP(pdst=ip)
    brodcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_brodcast = brodcast/arp_request
    answered_list, unanswered_list = scapy.srp(arp_request_brodcast, timeout=1)
    print(unanswered_list.summary())

scan("192.168.43.166")
