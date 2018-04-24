#!/bin/python3.6
## File operations
## Escape character 'r'
## eg F=open(r'c:\training\log\out.txt',w)

# 'r' - read only
# 'w' - write only
# 'a' - append
# 'w+' - read/write mode
# 'r+' - RW (overwrite)
# 'a+' - Append and read

F=open(r'/home/user/test.txt','w') ## Open file for writing and escaped '/'
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

## 3 methods to read
result=F.read()
print(result)

F.seek(0) ## without this - at first read, read pointer is set to end on the file so need to rest the pointer to begining of the file in order to read with second function - now you can see two read results
result2=F.read()
print(result2)

#F.seek(0,2) ## 2 set point to the end of file

result3=F.readline()
print(result3)

result4=F.readlines()  ## will read all lines at time and provide as list (array) of lines
print(result4)
