#!/usr/bin/env python3

from scapy.all import *

from panalyzer.packet_size import packet_size
from panalyzer.plot import plot_cdf
from panalyzer.plot import list_to_cdf, list_to_accumcdf

if __name__ == '__main__':
    import sys

    filename, output = sys.argv[1:]
    with open(filename, 'r') as f:
        data = list_to_cdf(map(int, f.readlines()))

        plot_cdf(list(data), output)
