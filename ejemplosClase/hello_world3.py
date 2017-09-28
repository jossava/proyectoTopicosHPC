#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 08:45:19 2017

@author: 
"""

from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.rank
size = comm.size

print 'rank', rank
print 'node count', size
print 9**(rank+3)