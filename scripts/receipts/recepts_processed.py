#!/usr/bin/env python3.5
import os
import glob
import json
import shutil

try:
    os.mkdir('./processed', mode=755)
except OSError:
    print("'processed' directory already exist")

reciepts = glob.glob('./new/reciept-[0-9]*.json')
subtotal = 0.0

for path in reciepts:
    with open(path) as F:
        content = json.load(F)
        subtotal += float(content['value'])

    name = path.split("/")[-1]  #  set / delimiter, stored path as list ['.', 'new', reciept-[0-9]*.json, ]
    # and printed last item in the list
    destination = "./processed/%s" % name
    shutil.move(path, destination)
    print("Moved %s to %s" %(path, destination))

print("Reciept subtotal: $%.2f" % subtotal)
