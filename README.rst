pcap-analyzer: A tool to analyze and plot traffic characteristics from pcap files
---------------------------------------------------------------------------------

Install
=======

Use the following script to install the library first.

::
  python setup.py install --user

Get the packet size distribution
================================

- Template
  ::
    python bin/procpktsize.py $PCAP_FILENAME > $PKT_FILENAME
    python bin/pltpktsize.py $PKT_FILENAME $FIGURE_NAME

- Example
  ::
    # python bin/procpktsize.py a.pcap > a.pktsize
    # python bin/pltpktsize.py a.pktsize a.eps

Get the per-flow statistics
===========================

Per-flow statistics include the distribution of number of packets and total
bytes (including header length).

- Template
  ::
    python bin/procperflow.py $PCAP_FILENAME > $PFS_FILENAME
    python bin/pltperflow.py $PFS_FILENAME $PREFIX $SUFFIX

- Example
  ::
    # python bin/properflow.py a.pcap > a.pfs
    # python bin/pltperflow.py a.pfs output/a eps

  The first line of ``a.pfs`` contains a single number which represents the
  maximum number of concurrent TCP connections.

  The resulted figures are:

  - ``output/a-perflow-cnt.eps``

  - ``output/a-perflow-cntcdf.eps``

  - ``output/a-perflow-cntaccum.eps``

  - ``output/a-perflow-size.eps``

  - ``output/a-perflow-sizecdf.eps``

  - ``output/a-perflow-sizeaccum.eps``

  The x-axis is using the log scale.
