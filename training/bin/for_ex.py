#!/usr/bin/python3.5
colors=['blue', 'red', 'green', 'yellow']
for i in colors:
    print(i)

for i in colors:
    if i == 'blue':
        continue
    elif i == 'red':
        break
    else:
        print(i)

S='welcome'

for i in S:
  print('i =',i)

line='#'*40
print(line)

K=100
L=[10,20,30]
for K in L:
  print('K=',K)

print('Actual K=',K)
print(line)

## for with Dictionary

D={'A':10, 'B':20}
for K in D:
  print('K1=',K)
print(line)
for K in D.keys():
  print('K2=',K)
for V in D.values():
  print('V=',V)
print(line)

for i in D.items():
  print('items =',i)
print(line)

for K,V in D.items():
  print(K,V)
print(line)
## multi Commented lines below to show interactive example
'''
## Zip function to combine list

>>> L1=[10,20,30,40]
>>> L2=['a','b','c']
>>> L3=[100,200,300,400]
>>> z=zip(L1,L2,L3)
>>> list(z)
[(10, 'a', 100), (20, 'b', 200), (30, 'c', 300)]

'''


L1=[10,20,30,40]
L2=['a','b','c']
L3=[100,200,300,400]

for i,j,k in zip(L1,L2,L3):
  print(i,j,k)
print(line)

### Using range function

for i in range(0,10,2):
  print(i)
for i in range(0,len(L3)):
  print(L3[i])

comp=['sap', 'synechron', 'oracle']
for c in comp:
  if c=='synechron':
    print('Syne Found')
    break
##this for else loop not if else
else:
  print('Not found')
print(line)

for c in comp:
  if c=='synechron':
    print('logic-1 here')
  if c=='synechron':
    print('logic-2 here')
## Avoid checking of multiple if statement, instead use 'continue' to break and go back to check next condition in loop
  if c!='synechron':
    continue





