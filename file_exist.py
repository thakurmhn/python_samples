#!/bin/python3.6
import os
if os.path.isdir("/tmp"):
  print('/tmp is directory')
else:
  print('/tmp does not exit')
