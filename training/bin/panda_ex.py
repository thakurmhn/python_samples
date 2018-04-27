#!/bin/python3.6
import pandas as pd
## Series
s=pd.Series()
print(s)
s=pd.Series([1,2,3,4,5])
print(s)
s=pd.Series([1,2,3,4,5],index=[100,200,300,400,500])
print(s)
print(s[:3])
print(s[[100,300]])
print(s.axes)
print(s.empty)
print(s.size)
print(s.values)
print(s.head(2))
print(s.tail(2))

## DataFrames
df=pd.DataFrame()
L=[1,2,3,4,5]
df=pd=pd.DataFrame(L)
print(df)

## Below code works in interactive terminal

#L=[['A',10],['B',20],['C',30]]
#df=pd.DataFrame(L)
#print(df)
#df=pd.DataFrame(L,index=['a','b','c'],columns=['Name','Increament'])
#print(df)
#df.to_csv('sample.csv',index=False)
#df.T
#df.axes
#df.head(2)
#df.size
#df.empty
#df.describe

		## Panels
#df.Panel()
#d={'item1':pd.DataFrame(L),
#   'item2':pd.DataFrame(L)
#  }
#df=pd.Panel(d)
#print(df)
