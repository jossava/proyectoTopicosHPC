#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 08:45:19 2017

@author: 
"""

from mpi4py import MPI

comm = MPI.COMM_WORLD

print 'My rank is', comm.rank
if comm.rank == 1:
    print 'Doing the task of rank 1'

if comm.rank == 2:
  print 'Haciendo la tarea del nodo 2'
  
if comm.rank == 3:
  print 'faisant noeud de devoirs 3'