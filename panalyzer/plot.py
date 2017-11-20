#!/usr/bin/env python3

import math
from itertools import accumulate, groupby
import matplotlib.pyplot as mp

def plot_cdf(data, output):
    x = map(lambda a: a[0], data)
    y = list(accumulate(map(lambda a: a[1], data)))
    ymax = y[-1]
    y = map(lambda v: v*100/ymax, y)

    fig, ax = mp.subplots()

    ax.plot(list(x), list(y))
    mp.savefig(output, bbox_inches='tight')

def plot_abs(data, output):
    x = map(lambda a: a[0], data)
    y = map(lambda a: a[1], data)

    fig, ax = mp.subplots()

    ax.plot(list(x), list(y))
    mp.savefig(output, bbox_inches='tight')

def list_to_cdf(data):
    results = sorted(data)
    for k, v in groupby(results, lambda x: x):
        yield k, len(list(v))

def list_to_logcdf(data):
    results = sorted(data)
    for k, v in groupby(results, lambda x: x):
        yield math.log(k, 10), len(list(v))

def list_to_accumcdf(data):
    results = sorted(data)
    for k, v in groupby(results, lambda x: x):
        yield k, len(list(v)) * k

def list_to_accumlogcdf(data):
    results = sorted(data)
    for k, v in groupby(results, lambda x: x):
        yield math.log(k, 10), len(list(v)) * k
