#!/usr/bin/env python

import scapy.all as scapy

def scan(ip):
    # scapy.arping(ip) implementing this function
    arp_request=scapy.ARP(pdst=ip)
    arp_request.show()
    # print(arp_request.summary())
    brodcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    brodcast.show()
    arp_request_brodcast = brodcast/arp_request
    # print(arp_request_brodcast.summary())
    arp_request_brodcast.show()


scan("192.168.43.166")
