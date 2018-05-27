#!/usr/bin/env python3.5

import time
# OR
#from time import localtime, strftime, mktime
'''
We can just import required functins from the modules, and use them without module.name
e.g mktime(start_time)
'''


start_time = time.localtime()
print("Timer started at", time.strftime('%X', start_time))

#Wait for user to stop timer
input("Press any key to stop timer")
stop_time = time.localtime()

difference = time.mktime(stop_time) - time.mktime(start_time) # minus start time from stop_time

print("Timer stopped at", time.strftime('%X', stop_time))
print("Total time:", difference, "seconds")
