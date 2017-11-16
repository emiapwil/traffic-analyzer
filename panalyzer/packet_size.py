#!/usr/bin/env python3

from scapy.all import *

def get_packet_size(p):
    return len(p)

def packet_size(pkts, n_core):
    from itertools import groupby

    results = map(get_packet_size, pkts)

    results = sorted(results)
    for k, v in groupby(results, lambda x: x):
        print(k, len(list(v)))
