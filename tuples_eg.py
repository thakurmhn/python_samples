#!/usr/bin/python

# Create an Array

my_list = [1, 'astring', 2.0, True]

print (my_list)

# Print firt index item

print (my_list[0])

print (my_list[2])

# print last item using index number [-1]
print (my_list[-1])


# Know the length of your list

print (len(my_list))

# Slice 
# print 0 to 2 index

print (my_list[0:2])
# OR up to two indexes

print (my_list[:2])

print (my_list[:4])

# More examples
print (my_list[::2])  # will print index 1 and 2
print (my_list[1::2]) # will print index 1 and 3

## Modifying List

my_list[0] = 1.0    # assinged new value index 0
print (my_list)
my_list.append('newitem')  # use append method to to add new item to the end of the lis
print (my_list)

print (my_list + [5, 6])	# concat list, this will actually not modify my_list but print the concat output
print (my_list)

my_list += [5, 6] ## If you want to actually modify the list use += operator
print (my_list)

my_list[1:3] = ['b', 'c']  # will take index item 1 to 3 and will replace with new items b and c
print (my_list)

my_list[1:3] = ['b', 'c', 'd', 'e', 'f']
print (my_list)

my_list[1:4] = []  # take slice 1 to 4 and replace with blank, this will delete 1 to 4 items
print (my_list)
