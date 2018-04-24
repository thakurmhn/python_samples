#!/bin/python3.6
# print ip, date and web url info in log files txt and csv

F=open(r'/opt/python_samples/training/log/log_sample.txt')
data=F.readlines()
F.close
print(data)

out1=open(r'/opt/python_samples/training/log/report.txt', 'w')
out2=open(r'/opt/python_samples/training/log/report2.csv', 'w')

for each_line in data:   # reading each line
  sp1=each_line.split('.')  # extracting ipaddress by seting . as delimiter
  if len(sp1)>0 and sp1[0].isdigit(): 
    sp2=each_line.split() # Extracting second field date from log file
    ip=sp2[0]
    dt=sp2[3]
    dt=dt[1:]       # slicing to extract date
    dt=dt.split(':') 
    dt=dt[0]
    if sp2[6].find('pics')==-1:
      img='No Image'
    else:
      img=sp2[6].split('/') # spliting '/' to extract pic info from line
      img=img[-1] 

    wb=sp2[10].split('/')
    wb=wb[2]
    print(ip,dt,img,wb,file=out1)
    print(ip,dt,img,wb,sep=',',file=out2)
out1.close()
out2.close()


## List Comprehension
## Shorter version of above code
out1=open(r'/opt/python_samples/training/log/report.txt', 'w')
out2=open(r'/opt/python_samples/training/log/report2.csv', 'w')
L=[i for i in range(10)]
M=[j for j in range(10) if j%2==0]
## above long code sequentially made in one line to print ip, date and wb info from logs
ip=[L.split()[0] for L in data if len(L.split('.'))>0 and L.split('.')[0].isdigit()]
dt=[L.split()[3][1:].split(':')[0] for L in data if len(L.split('.'))>0 and L.split('.')[0].isdigit()]
img=[L.split()[6].split('/')[-1] if L.split()[6].find('pics')!=-1 else 'No Image' for L in data if len(L.split('.'))>0 and L.split('.')[0].isdigit()]
wb=[L.split()[10].split('/')[2] for L in data if len(L.split('.'))>0 and L.split('.')[0].isdigit()]

print(ip)
print(dt)
print(img)
print(wb)

for i,j,k,l in zip(ip,dt,img,wb):
  print(i,j,k,l, file=out1)

for m,n,o,p in zip(ip,dt,img,wb):
 print(n,m,o,p,sep=',',file=out2)
