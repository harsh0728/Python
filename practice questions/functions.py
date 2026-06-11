list=[1,2,3,4,5]

#1 
def pri_len(nums):
    print ("The length of the list is:",len(nums))
    return len(nums)

pri_len(list)

#2
def pri_ele(list):
    print("The elements of the list are:",list)
    return list

pri_ele(list)

#3
def fact(n):
    factorial=1
    for i in range(1,n+1):
        factorial*=i
    print("The factorial of",n,"is:",factorial)
    return factorial

fact(9)

#4
def conv(usd):
    inr=usd*82.74
    print(usd,"USD is equal to",inr,"INR")
    return inr

conv(100)