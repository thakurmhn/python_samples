#!/bin/python3.6

## Dictionary Operations
#Dictionaries are mutable means you can update the values
#Dictionaries are unordered, not in sequence 

L=['python', 5, ['pune', 'blr']]
D={'course': 'python', 'duration': 5, 'location': ['Pune','banglore']}
E=dict(course='python', duration=5, location=['Pune','banglore'])

print (L,D,E,sep='\n')

# To print without '\n' i.e on same line

print (L,D,E,sep='\n',end='.')


## Update and Add
print (D['course'])
D['course']=['java', 'python']
print ('Update =', D)

## Create new Dict
D['author']={'fname': 'Van', 'lname': 'Rose'}
print ('add =', D)

## Remove Items
item1=D.pop('duration')  ## pop always return removed items
item2=D.popitem()
print ('Removed item =', item1, item2, D)


