#!/bin/python3.6

## Strings Operations

# Store sting with '  ' or " " or  '''   ''' or """   """

s='persion'

print (s)
s="person's"
print (s)

s='''persion's hight is 50"'''

print (s)

## print sting lenghth 

print (len(s))

s='Welcome'
print (s[0])
print (s[2])
print (s[3])

## Print part of Sring
# Slice 
print (s[1:6])
print (s[ :6])
print (s[2: ])
print (s[ : ])

## Concatination of Srint
x='hello'
y='python'
z=x+y
print (z)

##Repetition
w=y*10
print (w)
line=''*40
print (line)

s2='WEL COME'
s3=s2[4: ]+s2[ :3]
print (s3)

print (s[::1])
print (s[::2])
print (s[::3])

## Negative 


print (s[::-1])
print (s[::-2])
print (s[::-3])

a=s2.startswith('WEL')  # Print sting start with WEL
b=s2.endswith('ME') # print string ends with

print (a)
print (b)

c=s2.isupper()  # Return true or false
d=s2.lower() # Convert into lowercase

print (c, d)

e=s2.islower()
f=s2.lower()

print ('lower=', e,f)

g=s2.istitle()
h=s2.title()

print ('Title =', g,h)
i=s2.index('L')
j=s2.find('L')

print ('index of L =', i,j)

l=s2.strip()   # Remove space
m=s2.lstrip() # Remove space left
n=s2.rstrip() # remove space right

print ('l=',l, 'm=',m, 'n=',n)


## Other strings ##

v='123'
o=v.isdigit()

v='123abc'
p=v.isalnum()

s='abc'
q=s.isalpha()
 
s='wel come'
q=s.split()   # wel come
t=s.split('e')
print ('q=',q, 't=',t) 

### More strings

s='[welcome]'
l=s.strip('[]')
m=s.lstrip('[')
n=s.rstrip(']')
print ('l=',l, 'm=',m, 'n=',n)
x=s.replace('[','x')
print ('Replace =',x)

x=10
y=20
z=x+y
res='additionof{}&{}is{}'.format(x,y,z)
print ('res =',res)

res='addition of {1} and {2} is {0}'.format(z,x,y)
print ('Res2=',res)

#Check join function
