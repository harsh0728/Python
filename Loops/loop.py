# while loop
count=1

while count<=5:
    print(count)
    count+=1

# for loop
nums=[1,2,3,4,5]

for num in nums:
    print (num)

str="Hello, World!"

for char in str:
    if (char=='o'):
        print("Found 'o' at index: ",str.index(char))
        break
    print(char)
else:
    print("Character 'o' not found in the string.")

# Range

for i in range(5): #range(stop)
    print(i)

for i in range(2,9): #range(start, stop)
    print(i)

for i in range(1,10,2): #range(start, stop, step)
    print(i)