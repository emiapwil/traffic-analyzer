#!/usr/bin/env python3

from scapy.all import *

from panalyzer.packet_size import packet_size
from panalyzer.plot import plot_cdf

if __name__ == '__main__':
    import sys

    pcap_file = sys.argv[1]

    with PcapReader(pcap_file) as pcap:
        data = packet_size(pcap, n_core=8)

        for ps in data:
            print(ps)
