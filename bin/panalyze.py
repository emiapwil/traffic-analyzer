#!/usr/bin/env python3

from itertools import islice
from scapy.all import *

from panalyzer.packet_size import packet_size

if __name__ == '__main__':
    import sys

    pcap_file = sys.argv[1]
    with PcapReader(pcap_file) as pcap:
        packet_size(pcap, 8)
