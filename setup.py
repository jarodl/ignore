#!/usr/bin/env python
# encoding: utf-8

from setuptools import setup
import os, sys

version = '0.1.0'

install_requires = []

setup(
    name="ignore",
    version=version,
    description="Download .gitignore files for a given language",
    long_description=(open("./README.md").read()),
    author="Jarod Luebbert",
    author_email="jarodluebbert@gmail.com",
    url="http://github.com/jarodl/ignore",
    packages=["ignore"],
    scripts=["bin/ignore"],
    include_package_data=True,
    zip_safe=True,
    install_requires=install_requires,
    license="MIT",
    classifiers=(
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Intended Audience :: End Users/Desktop",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content :: CGI Tools/Libraries",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
    )
)
