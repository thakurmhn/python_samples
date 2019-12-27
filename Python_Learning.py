'''
- Zip Function In Python
Zip function is used to combine two list
Create Dictionary by combining two list
'''

friends = ["Rolf", "Bob", "Jen", "Anne"]
time_since_seen = [3, 7, 15, 11]

D1 = dict(zip(friends, time_since_seen))
print(D1)
