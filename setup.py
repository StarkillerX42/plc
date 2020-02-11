#!/usr/bin/env python
"""Install this package. Requires sdss3tools.

To use:
python setup.py install
"""
import os, sys, subprocess
try:
    import sdss3tools
except ImportError:
    print 'ERROR: You need to set up sdss3tools before building this package!'
    sys.exit(-1)

if len(sys.argv) > 1 and sys.argv[1] in ("build", "install"):
    try:
        for dirName in ["include","etc"]:
            subprocess.call(["sdssmake"], cwd=dirName)
    except OSError:
        print 'WARNING: sdssmake is not set up. Not building include/ and etc/ portions.'
        print 'WARNING: Unless the appropriate files were include in your distribution/svn-tag, there may be runtime errors.'

sdss3tools.setup(
    description = "PLC logic and display",
    data_dirs = ["include", "src"]
)
