#!/usr/bin/env python3.5

import argparse

parser=argparse.ArgumentParser(description='Read the file in reverse')

# Add argument1
parser.add_argument('filename', help='the file to read')
#add argument2
parser.add_argument('--limit', '-l', type=int, help='the number of lines to read')
# Add argument3
parser.add_argument('--version', '-v', action='version', version='%(prog)s 1.0')

args = parser.parse_args()
print(args)
