#!/bin/python3.6

## while works on booleans like if ; true/false 
## for works on lists
x=10
while x>0:
  print(x)
  x-=1  #x=x-1
line='+'*40
print(line)

## While with strings
S='Hello'
i=0
while i<len(S):
  print(S[i])
  i+=1
print(line)

## While with lists

L=[10,20,30]
while L:   ## if there elements in List means true else false
  x=L.pop()
  print('x=',x)
print(line)

## Dictionary

D={'A':10,'B':20}
while D:
    x=D.popitem()
    print('x=',x)
print(line)



cart=[]
while True:
  item=input ('Enter Item:')
  cart.append(item)
  ch=input('Do you want to quit?(y/n)')
  ch=ch.upper()
  if ch=='Y':
    print('cart=',cart)
    break
