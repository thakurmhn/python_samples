#!/usr/bin/env python3.5

# Usage :
'''
./argparse_ex3.py -h

./argparse_ex3.py -v

./argparse_ex3.py ../files/os_list.txt

./argparse_ex3.py --limit 2 ../files/os_list.txt
'''

import argparse

parser=argparse.ArgumentParser(description='Read the file in reverse')

# Add argument1
parser.add_argument('filename', help='the file to read')
#add argument2
parser.add_argument('--limit', '-l', type=int, help='the number of lines to read')
# Add argument3
parser.add_argument('--version', '-v', action='version', version='%(prog)s 2.0')

args = parser.parse_args()

with open(args.filename) as F:
    '''
    used 'filename' attribute from 1st argument.
    with 'with open' does not explicitely require to close the file
    '''
    lines = F.readlines()  # used reverse function to reverse the lines
    lines.reverse()  ## Reverse lines from bottom to top

    if args.limit:  # Used limit attribute from arg 2
        lines = lines[:args.limit]  # Getting the slice subset of lines assign back to eliminates when -- limit is used

    for line in lines:
        print(line.strip()[::-1])
        '''
        strip() eliminates printing of '\n'
        [::-1] reverse the sring
        '''
