#!/bin/python3.6

import sqlite3

F=open(r'/opt/python_samples/training/log/log_sample.txt')
data=F.readlines()
F.close()
ip=[L.split()[0] for L in data if len(L.split('.'))>0 and L.split('.')[0].isdigit()]
dt=[L.split()[3][1:].split(':')[0] for L in data if len(L.split('.'))>0 and L.split('.')[0].isdigit()]

con=sqlite3.connect('my_db')
#con=pymysql.connect(user= , password= , database= , host= , port= ,)  ## To connect mysqldb

cur=con.cursor()
cur.execute('create table if not exists log_data(ip varchar(100), dt varchar(100))')

for i,j in zip(ip,dt):
  query="insert into log_data values('{}','{}')".format(i,j)
  cur.execute(query)
con.commit()

F2=open(r'/opt/python_samples/training/log/somequery.txt')
queries=F2.readlines()
F2.close()
for q in queries:
  cur.execute(q)
  q=cur.fetchall()
  print(q)

import os
os_dir=r'/opt/python_samples/training/'
r=os.walk(os_dir)
print(r)

for r,s,f in os.walk(os_dir):
  print('file=',r,s,f)


