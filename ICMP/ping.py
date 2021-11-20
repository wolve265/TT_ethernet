import os
import sys

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from icmplib import multiping
from ARP.arp_scanner import scan_arp

number_of_pings = 1
list_of_ip = ['192.168.0.206', '192.168.0.102', '192.168.0.136']
hosts = multiping(list_of_ip, number_of_pings)
print(hosts)

for host in hosts:
    if host.is_alive:
        scan_arp(host.address)
    else:
        print(f'No response from: {host.address}')
