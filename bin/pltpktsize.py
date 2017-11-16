#!/usr/bin/env python3

from itertools import accumulate
import matplotlib.pyplot as mp

def plot_pktsize(lines, output):
    data = map(lambda l: l.split(' '), lines)
    data = [(int(k), int(v)) for k, v in data]

    x = map(lambda a: a[0], data)
    y = accumulate(map(lambda a: a[1], data))

    fig, ax = mp.subplots()

    ax.plot(list(x), list(y))
    mp.savefig(output, bbox_inches='tight')

if __name__ == '__main__':
    import sys

    filename, output = sys.argv[1:]

    with open(filename, 'r') as f:
        plot_pktsize(f.readlines(), output)
