#!/usr/bin/env python3

from scapy.all import *
from statistics import mean, stdev

FIN = 0x01
SYN = 0x02
RST = 0x04
PSH = 0x08
ACK = 0x10
URG = 0x20
ECE = 0x40
CWR = 0x80

def conn_key(sip, dip, sport, dport):
    return '-'.join([str(sip), str(dip), str(sport), str(dport)])

def bidirection_key(sip, dip, sport, dport):
    return conn_key(sip, dip, sport, dport), conn_key(dip, sip, dport, sport)

def lookup_first(active, k1, k2):
    if k1 in active:
        return k1, active[k1], True
    if k2 in active:
        return k2, active[k2], True
    return None, (0, 0), False

def get_connection_info(pkts, **kargs):
    peak_cc = 0
    conn = []
    active = {}
    for p in pkts:
        if not TCP in p:
            continue
        ip = p[IP]
        tcp = p[TCP]

        sip, dip = ip.src, ip.dst
        sport, dport = tcp.sport, tcp.dport
        k1, k2 = bidirection_key(sip, dip, sport, dport)
        k, conn_info, success = lookup_first(active, k1, k2)

        flags = tcp.flags
        if not success:
            if not flags & SYN:
                # ignore incomplete connections
                continue
            else:
                active[k1] = (1, len(p))
        else:
            conn_info = (conn_info[0] + 1, conn_info[1] + len(p))
            if flags & FIN or flags & RST:
                # TODO
                conn += [conn_info]
                del active[k]
            else:
                active[k] = conn_info
        if len(active) > peak_cc:
            peak_cc = len(active)
    return peak_cc, conn
