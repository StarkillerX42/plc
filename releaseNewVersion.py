#!/usr/bin/env python
"""A script to release a new version of plc from a subversion working copy

This builds the necessary files from the appropriate .skl files via sdssmake, 
checks them in to trunk, and tags a new version in SVN.

To use:
    ./releaseNewVersion.py
"""

import os
import re
import sys
import subprocess

PkgName = "plc"

def get_yes(text):
    getOk = eval(input(text))
    if not getOk.lower().startswith("y"):
        sys.exit(0)

os.environ['PLC_DIR'] = os.getcwd()

print("Status of subversion repository:")
subprocess.call(["svn", "status"])

get_yes("Is the subversion repository up to date? (y/[n]) ")

print("Subversion repository OK")

version = eval(input('What is the new tagged version? '))
# should be no whitespace in a version string.
if version[0] != 'v' or re.search(r'\s+',version):
    print("Version number syntax is 'vX_X', no whitepace. You'll have to start again.")
    sys.exit(-1)

print("Setting up sdssmake, cleaning, and building")
status = subprocess.call('setup sdss3tools && setup sdsstools && sdssmake clean && python setup.py build',shell=True,env=os.environ)
if status != 0:
    print(('Could not complete build:',status))
    sys.exit(1)

print("Checking-in pre-built files.")
message = 'Auto check-in of prebuilt files for PLC prior to tagging.'
status = subprocess.call(['svn','ci','-m '+message])
if status != 0:
    print(('svn ci failed with:',status))
    sys.exit(2)

get_yes("Tagging new SVN version: %s (y/[n])"%version)
svnbase = 'svn+ssh://sdss3svn@sdss3.org/repo/apo/plc'
svntrunk = svnbase+'/trunk'
svntag = svnbase+'/tags/'+version
print(('svn copy',svntrunk,svntag))
message = 'Tagging PLC '+version
status = subprocess.call(['svn','copy','-m '+message,svntrunk,svntag])
if status != 0:
    print(('svn trunk copy failed with:',status))
    sys.exit(2)

print('Done.')
