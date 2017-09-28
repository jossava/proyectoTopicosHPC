#!/usr/bin/bash
# -*- coding: utf-8 -*-

if ! [ -x /usr/bin/nproc ]; then
    echo "nproc is not installed. Please install it"
    exit 1
fi
CORES=$(nproc)
EXAMPLE=1
mpiexec -np ${CORES} python ./hello_world${EXAMPLE}.py