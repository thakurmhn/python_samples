#!/usr/bin/python

ages = {'kevin': 28, 'mark': 40, 'joe': 63}
print (ages)

print (ages['mark'])
print (ages['joe'])

# How to append in list

ages['cathy'] = 21
print (ages)

# HOw to delete dic item
del ages['joe']
print (ages)

# Delete using pop

ages.pop('mark')
print (ages)

# Delete dictionary

del ages


ages = {'kevin': 28, 'mark': 40, 'joe': 63}

# list using below methods
print (ages.values)
print (ages.keys)
print (ages.items())

# Alternative ways of making dictionary

weights = dict(mohan=65, raj=33)
print (weights)


