#1
nums=[1,4,9,16,25,36,49,64,81,100]

for num in nums:
    print(num)

#2
x=int (input("Enter a number to search in nums: "))
for num in nums:
    if num == x:
        print("Number found in the list.")
        break
else:
    print("Number not found in the list.")