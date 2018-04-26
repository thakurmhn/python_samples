#!/bin/python3.6
a=10
b=0
try:
   c=a/b
   print('c=',c)
except:
  print('Some Error')
line='_'*40
print(line)


g=10
h=0
try:
  r=g/h
except:
  print('Some Error')
  r=g/h
finally:
  print('final block')
line='_'*40
print(line)
