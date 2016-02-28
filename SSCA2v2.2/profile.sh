#!/usr/bin/bash
valgrind --tool=callgrind --cache-sim=yes --branch-sim=yes --callgrind-out-file=$1 ./SSCA2 11
