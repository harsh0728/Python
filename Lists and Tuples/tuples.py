tup=(1,2,3,4,5)
print(type(tup),tup)
print(tup[0])
print (tup[1:3])
# Not allowed in python tup[0]=10

# Tuple Methods
tup1=(1,2,3,4,5)
tup2=(6,7,8,9,10)
tup3=tup1+tup2
print("Concatenated Tuple: ",tup3)
print("Length of Tuple: ",len(tup3))
print("Maximum and Minimum Element: ",max(tup3),min(tup3))

print("Index of 8 in tup2: ",tup2.index(8)) # Returns the index of the first occurrence of 8 in tup2
print("Count of 7 in tup2: ",tup2.count(7)) # Returns the number of times 7 appears in tup2