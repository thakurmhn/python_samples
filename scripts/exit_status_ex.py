#!/usr/bin/env python3.5
## Error handling when file not found
# pass in non exist file to produce error


# Usage :
'''
Problem:
./argparse_ex3.py  unknown_file.txt
if you check 'echo $?' exit status is 0 even after Error
need to get exist status other than 0 use sys.exit method
'''

import argparse
import sys

parser=argparse.ArgumentParser(description='Read the file in reverse')

# Add argument1
parser.add_argument('filename', help='the file to read')
#add argument2
parser.add_argument('--limit', '-l', type=int, help='the number of lines to read')
# Add argument3
parser.add_argument('--version', '-v', action='version', version='%(prog)s 2.0')

args = parser.parse_args()

try:      #  try statement dump into the context where error occurs;
            # equivalant to 'if error found'
    F = open(args.filename)  # things that may cause the error
    limit = args.limit
#except statement
except FileNotFoundError as err:  # assign actual error to variable (err)
    print("Error", err)
    sys.exit(2)  # returns exit status 2
# Optionaly you can print custom messages
#except:
#    print("your customized error message")

#else statement
else:   # what should happen in case of no error caught
    with F:  # using F variable already defined in try: statement; 'with' still works
        lines = F.readlines()  # used reverse function to reverse the lines
        lines.reverse()

        if args.limit:  # Used limit attribute from arg 2
            lines = lines[:args.limit]  # Getting the slice subset of lines assign back to eliminates when -- limit is used

        for line in lines:
            print(line.strip()[::-1])

#final statement
#finally
# print("do some action here")
