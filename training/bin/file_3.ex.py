#!/bin/python3.6

## Another method to write into file

F1=open(r'/opt/python_samples/training/log/mylog.out', 'w')
F2=open(r'/opt/python_samples/training/log/mylog2.out', 'w')

print(10,20,'Hello',file=F1,flush=True)
print(10,20,'Hello',sep=',',file=F2,flush=True)

F1.close()
F2.close()
