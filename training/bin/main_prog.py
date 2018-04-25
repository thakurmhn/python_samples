#!/bin/python3.6

import add_module

print(add_module.msg)
r=add_module.add(10,20)
print('add=',r)


## method 2 of importing module
import add_module as am
print(am.msg)
r=am.add(20,30)
print('add r2',r)

## method 3 of import 
from add_module import msg
print(msg) # no need fo prefix add_module.msg


##4
from add_module import *
print(msg)
r=add(100,200)
print('r=',r)

##5
from add_module import msg as m
print(m)

## Package
import net.cloud.add_module
print(net.cloud.add_module.msg)
r=net.cloud.add_module.add(100,200)
print('r=',r)

##
import net.cloud.add_module as m
print(m.msg)
print(m.add(10,20))

##
from net.cloud.add_module import *
print('r3',msg)
print(add(10,20))
