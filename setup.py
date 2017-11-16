#!/usr/bin/env python3

from setuptools import setup, find_packages
from os import path, listdir

def openfile(fname):
    return open(path.join(path.dirname(__file__), fname)).read()


def files(dirname):
    return [path.join(dirname, filename) for filename in listdir(dirname)]


setup(
    name="pcap-analyzer",
    version="0.1",
    description="A tool to analyze and plot traffic characteristics from pcap files",
    url="https://github.com/emiapwil/traffic-analyzer",
    author="Kai Gao",
    author_email="emiapwil@gmail.com",
    classifiers=[
    ],
    license="GPLv2",
    long_description=openfile("README.rst"),
    packages=find_packages(),
    scripts=files('bin'),
    zip_safe=False
)
