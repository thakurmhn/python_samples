#!/usr/bin/python3.5
x=10
if x==10:
  print('Equal')

if x>10:
  print('Greater')

if x<10:
  print('lesser')

print('END')

import sys
a=10
if a>0 and a==10:
  print('a is equal')
#  sys.exit()  ## Commented in order to execute further code
elif a>10:
	print('a is greater')
print('End 2')

## If with strings

S='python'
if 'py' in S:
	print('py found')

if S=='python':
	print('S is equal')


L1=['Hello','python']
L2=['Hello','python']

if L1==L2:
  print('L1 and L2 are equal')

if L1 is L2:
  print('L1 and L2 are same')
else:
  print('L1 and L2 are pointing to differrent')

## if with Dictionary

D={'A':10, 'B':20}
if 'A' in D:
  print('Key A found')
##OR
if 'A' in D.keys():
  print('Key A found')
if 10 in D.values():
  print('value 10 found')

if 100 not in D.values():
  print('100 not found')

## If with tupples

if ('A',10) in D.items():  ## assigned tuple on the fly
  print('K values found')

name="mohan"
if len(name) >= 6:
    print("name is long")
elif len(name) <= 5:
    print("Name is 5 character")
elif len(name) >= 4:
    print("name is 4 char")
else:
    print("name is short")

