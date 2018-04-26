#!/bin/python3.6
import re
F=open(r"/opt/python_samples/training/log/log_sample.txt")
data=F.readlines()
F.close()
for line in data:
  M=re.match('(\d{3}\.\d{1,3}\.[0-9]{3}\.\d{3})\s+.*(\d{2}/[A-za-z]{3}/\d{4}).*pics/(\w+\.\w+).*http://(\w+\.\w+\.\w+).*',line)
  M2=re.match('(\d{3}\.\d{1,3}\.[0-9]{3}\.\d{3})\s+.*(\d{2}/[A-za-z]{3}/\d{4}).*http://(\w+\.\w+\.\w+).*',line)
  if M!=None:
    ip=M.group(1)
    dt=M.group(2)
    img=M.group(3)
    wb=M.group(4)
    print(ip,dt,img,wb)
  elif M2!=None:
    ip=M2.group(1)
    dt=M2.group(2)
    img='No Image'
    wb=M2.group(3)
    print(ip,dt,img,wb)

# {3} numberof characters to be matched
# .* match evrything after .*
# \s match space
# \s+ match one or more spaces
# \d = match digit
# \D = anything not digit
# \S = non space, will match word till its find space eg - ancdef jktl
# \W = match non word characters

