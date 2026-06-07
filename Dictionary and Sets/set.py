collection={1,2,3,4,5,4,3,2,1}

print("The set is: ",collection," ",len(collection)," ",type(collection))

collection.add(6)
print("After Adding: ",collection)

collection.remove(3)
print("After Removing: ",collection)
collection.discard(10) # Does not raise an error if the element is not found
print("After Discarding: ",collection)

empty_set=set()
print("Empty Set: ",empty_set," ",type(empty_set))

# Union and Intersection
set1={1,2,3,4,5}
set2={4,5,6,7,8}
print("Union of set1 and set2: ",set1.union(set2))
print("Intersection of set1 and set2: ",set1.intersection(set2))
