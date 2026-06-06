str1="apna"
str2="college"

print(len(str1))
print(len(str2))
res=str1+" "+str2
print (res)
print (res[7]) # indexing starts from 0

#Slicing
print (res[0:6]) # slicing, last index is not included
print (res[:11]) # slicing, first index is not included
print (res[3:]) # slicing, last index is not included

#Indexing
print (res[-9:-2]) # slicing, negative indexing starts from -1