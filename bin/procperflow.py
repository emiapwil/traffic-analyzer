#!/usr/bin/env python3

from scapy.all import *
from panalyzer.connection import get_connection_info

if __name__ == '__main__':
    import sys

    pcap_file = sys.argv[1]

    with PcapReader(pcap_file) as pcap:
        peak_cc, conn = get_connection_info(pcap, n_core=8)
        print(peak_cc)
        for c in conn:
            print(c[0], c[1])
