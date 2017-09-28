#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 08:33:44 2017

@author: asanchez
"""

from mpi4py import MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
print "hello world from process", rank