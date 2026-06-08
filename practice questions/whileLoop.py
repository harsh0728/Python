#1 1 to 50
count=1
while count<=50:
    print(count)
    count+=1

#2 50 to 1
count=50
while count>=1:
    print(count)
    count-=1

#3 Multiplication table
number=int(input("Enter a number: "))
count=1
while count<=10:
    print(number,"x",count,"=",number*count)
    count+=1

#4 Square of numbers from 1 to 10
count=1
lists=[]
while count<=10:
    lists.append(count*count)
    count+=1
print("The squares of numbers from 1 to 10 are: ",lists)

#5 Search for a number in a list
lists=[1,4,9,16,25,36,49,64,81,100]
num=int(input("Enter a number to search: "))
index=0
while index<len(lists):
    if lists[index]==num:
        print("Number found at index: ",index)
        break
    index+=1

#6 sum of first n numbers.
n=int(input("Enter a number: "))

cnt=1
sum=0
while cnt<=n:
    sum+=cnt
    cnt+=1
print("The sum of first ",n," numbers is: ",sum)
