#!/usr/bin/env python3

"""
Simple module to write statistics to log
"""

STATFILE = "./stats"

def add_stat(stat_stamp):
    with open(STATFILE, 'a') as statfile:
        statfile.write(stat_stamp + '\n')
