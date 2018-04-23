#!/bin/python3.6

## List Operations

# List is mutable, you can add modify objects in the list


L=list()   # Create empty list
L=[ 10, 12.5, 'python', ['a','b']]
print ('LIST=',L)

## Accessing Elements

print ('element 0 is',L[0])
print ('slice is',L[1:3])


## Modifying Elements
L[0]='Hello'
print ('Updated list ',L)

print (L[2])
print (L[2][2])  # will print 't' within list item 'python'

## Adding Elements

L.append(100)
print('append =',L)
L.insert(2,200)
print ('Insert =',L)


M=[1,2,3]
N=['a','b','c']
K=M+N
print ('K =',K)

M.extend(N)
print ('Extend =',M)

## Remove Element
item1=M.pop()   #Remove last item in the list
item2=M.pop(1)
item3=M.remove('a')

print ('M =','Items',item1,item2,item3)

## Getting Index 

M=[10, 20, 30]
i=M.index(20)
c=M.count(10)

print ('Index and Count is', i,c)

## Empty the list
L.clear()
print ('L=',L)

## Reverse the list
M.reverse()
print ('Reverse =', M)

## Sorting 

P=[20,9,10]
Q=['c', 'a', 'b']

P.sort()
Q.sort()
print ('P =', P)
print ('Q =',Q)

P.sort(reverse=True)  ## Sort decending order
print ('Reverse P =', P)
## Copy objject
R=['a', 'b', [10, 20]]
T=R.copy()
R.append('c')
print ('T =',T, 'R =', R)

### Copy object 
# to use shallowcopy and deepcopy functions need to import Module Copy

import copy
L1=[10, 20, ['a', 'b']]
L2=copy.copy(L1) # shallowcopy will copy the objects to both list, will keep another list updated when object upated in 1st list

L1[2].append('c')
print (L1,L2)

## DeepCopy - will create and maintain separate lists
L3=copy.deepcopy(L1)
L1[2].append('d')
print ('L1 =', L1, 'L3 =', L3)

