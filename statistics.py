#!/usr/bin/env python3

"""
Simple module to write statistics to log
"""

import os

STATFILE = (os.path.dirname(os.path.realpath(__file__))+"/stats"

def add_stat(stat_stamp):
    with open(STATFILE, 'a') as statfile:
        statfile.write(stat_stamp + '\n')
