#!/bin/python3.6

## List and touples are same but we cant modify tuple, once assigned items, it remains same

T=(10, 12.5, 'python', ['a', 'b'], (10, 20))
print (T)

print (T[0])
print (T[1:2])

#T[0]=200  # This will not work as trying to update item

i=T.index(12.5)
c=T.count(10)
print ('index is =', i, c)


## Multiple assignment 

x,y=(10,20)
z=(10,)  # use comma while asigning single element

print (type(z))
print (x,y)
a=10
#a=a+1  # will not work
a+=1
x,y=y,x

## We can convert tuples to list and v/s

a=10
b=str(a)
c=int(b)
d=[10,20]
e=tuple(d)
f=list(e)

print ('e =', e)
print ('f =', f)



s='welcome'
l=list(s)
print ('l =', l)

m=''.join(l)
print('m = ',m)
