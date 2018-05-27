#!/usr/bin/env python3.5
import sys
print("Printing First argument which is script name", sys.argv[0])

## take a slice of the list [] to print positional argument
print("Positinal Arguments are", sys.argv[1:])
print("First Argument is ", sys.argv[1])

## Script Usage : ./cmd_arg_ex.py testing tessting1 testing2 testing3
