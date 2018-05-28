#!/usr/bin/env python3.5

# List comprehension

import argparse

parser = argparse.ArgumentParser(description='Search for the word')
parser.add_argument('snippet', help='partial or complete string to search for words')

args = parser.parse_args()
snippet = args.snippet.lower()

with open('/usr/share/dict/words') as F:
    words = F.readlines()

#matches = []

#for word in words:
#    if snippet in word.lower():
#        matches.append(word)
#print(matches)

'''
instead of above 4 line code we have short version as below single line code
'''

#matches=[word for word in words: if snippet in word.lower()]

#Modified version of above to remove \n interpretion

#matches=[word.strip() for word in words if snippet in word.lower()]
#print(matches)

############ Again modified version of above two readlines

print([word.strip() for word in words if snippet in word.lower()])
