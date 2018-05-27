#!/usr/bin/env python3.5

import argparse

# Build the parser
parser = argparse.ArgumentParser()  # constructing objects from class
parser.add_argument('filename', help='pass file to read')

args = parser.parse_args()
print(args)

#Parse the Arguments


#read the file, reverse the contents and Print
