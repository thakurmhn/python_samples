#/bin/python3.6

## This is also a collection, has no index, keys, unsorted but have uniq values

S={10,10,20,'Hello','Hello'}
print ('set=', S)

S.add(100)
S.add(100)
print ('add=',S)

## Remove itema

i=S.remove(100)
j=S.pop()
print ('Removed =',i,j)
