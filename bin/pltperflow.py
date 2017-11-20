#!/usr/bin/env python3

from panalyzer.plot import plot_cdf, plot_abs
from panalyzer.plot import list_to_cdf, list_to_accumcdf
from panalyzer.plot import list_to_logcdf, list_to_accumlogcdf

if __name__ == '__main__':
    import sys

    filename = sys.argv[1]
    prefix = sys.argv[2]
    suffix = sys.argv[3]

    with open(filename, 'r') as f:
        conn = list(map(lambda l: l.split(' '), f.readlines()[1:]))

    cnt = list(map(lambda c: int(c[0]), conn))
    size = list(map(lambda c: int(c[1]), conn))

    cntcdf = list(list_to_logcdf(cnt))
    plot_abs(cntcdf, '%s-perflow-cnt.%s' % (prefix, suffix))
    plot_cdf(cntcdf, '%s-perflow-cntcdf.%s' % (prefix, suffix))

    cntacdf = list(list_to_accumlogcdf(cnt))
    plot_cdf(cntacdf, '%s-perflow-cntaccum.%s' % (prefix, suffix))

    sizecdf = list(list_to_logcdf(size))
    plot_abs(sizecdf, '%s-perflow-size.%s' % (prefix, suffix))
    plot_cdf(sizecdf, '%s-perflow-sizecdf.%s' % (prefix, suffix))

    sizeacdf = list(list_to_accumlogcdf(size))
    plot_cdf(sizeacdf, '%s-perflow-sizeaccum.%s' % (prefix, suffix))
