student=["Harsh",24,68.5,"Bangalore"]
print(student)
print(student[0])
student[0]="Chotu"
print(student[:2])
print(student[1:])

# List Methods
list=[1,2,3,4,5]

list.append(9)

list.sort()
print("Ascending: ",list)
list.sort(reverse=True)
print("Descending: ",list)

list.reverse()
print("Reversed: ",list)

list.insert(4,"TCS")
print("After Insertion: ",list)

list.remove("TCS")
print("After Removing: ",list)

list.pop(4)
print("After Popping: ",list)