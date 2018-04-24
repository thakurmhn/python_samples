#!/bin/python3.6
## File operations
## Escape character 'r'
## eg F=open(r'c:\training\log\out.txt',w)

F=open(r'/home/user/test.txt','w') ## Open file for writing
x=10
y=20
x=str(x)+'\n'  ## Numbers converted into string using 'str' function
y=str(y)+'\n'
F.write(x)
F.write(y)
#F.close() # commented to work/write below code

## Another method to write
x='this is test''\n'
y='hello mohan''\n'
L=[x,y]
F.writelines(L)
F.flush()
F.close()


## Open for read

F=open(r'/home/user/test.txt','r') ## Open file for reading


result3=F.readline()
print(result3)

result4=F.readlines()  ## will read all lines at time and provide as list (array) of lines
print(result4)


## COnvert from string to int or list
a=result4[0]
a=a.strip()
a=int(a)  ## Convert 10 into number, we converted 10 into string before writing to file

L=[10,20]
type(L)
s=str(L)  # converted into string
print(s)
list(s)
eval(s)
t=eval(s) # eval will produce actual datatype - here from string it will produce list 
print(t)
