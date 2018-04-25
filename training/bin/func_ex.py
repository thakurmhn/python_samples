#!/bin/python3.6
## Functions are scope - local, enclosed, global, builtins

def add():
	a=10
	b=20
	c=a+b
	print('c=',c)
add()


## Function that takes input
def add2(a, b):
	c=a+b
	print('add2=',c)

add2(10,30)

def add3(a, b):
	c=a+b
#	return  # by default it will return None
	return a+b
# return provides value to use outside of function but need to assign variable to call function
# you can not directly print like 'print(c)'

ret=add3(30,40)
print('add3=',ret)

## Function with default arguments
def add4(a,b=10):
	return a+b
r1=add4(10)
r2=add4(20,30)
r3=add4(40,0)

print('add4=', r1,r2,r3)

## FUnction that accept 0 or more arguments

def add5(a,b=10,*c): #*c is tuple, n no of arguments
	r=a+b
	print('tuple c=',c)
	for i in c:  # for is used to process c'tuple a and b are default arguments
	 r=r+i
	return r
r1=add5(10)    # Argument 1
r2=add5(10,20) # Argument 2
r3=add5(10,20,30) #Argument 3   for lool will start from 3rd argument
r4=add5(10,20,30,40) # Argument 4

print('add5=',r1,r2,r3,r4)

## Function that take only keywords as argument - e.g username, password for auth

def add8(*,kw1,kw2):
	return kw1+kw2
r1=add8(kw1='user',kw2='name')

print('add8=',r1)


## Dictionary variables as argument
def add9(a,b=10,*c,d,e,**f): #**f is dictionary

	r=a+b+d+e  # a b d e are fix arg
	print('tuple=',c) # is tuple means variable
	print('Dict=',f) #f is dictionary
	for i in c: 	# proceing tuple arg
	  r=r+i
	for i in f.values(): #processing dict arg
	  r=r+i
	return r
r1=add9(10,e=20,d=30)
r2=add9(10,20,30,d=40,e=50,f=60,g=70)

print('add9=',r1,r2)


## Passing the ref to functions, above examples are pass by values
x=10 # x is ref 10 is value
y=20

def ref1(a,b):
  return a+b
r1=ref1(x,y)
print('ref1 =',r1,x,y)


L1=[10,20]
L2=['a','b']
def ref2(x,y):
  x.append(30)
  return x+y
r1=ref2(L1,L2)
print('ref2',r1,L1,L2)

## Variable scope in function
z=10
def f1():
  z=20  ## Enclosed scope
def f2():
  z=30  # local 
  print('f2=',z)
f2()
print('f1=',z)
f1()
print('global=',z)

## Functions are scope - local, enclosed, global, builtins
def Account():
  count=0
  def create_acc():
    nonlocal count
    count+=1
    print('your account no is :',count)
  return create_acc
f=Account()
f()
f()
f()
