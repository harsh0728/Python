#1
def calc(n):
    if (n==1):
        return 1
    return calc(n-1)+n

print("The sum of first 5 natural numbers is:",calc(5))

#2
def print_list(list,idx):
    if (idx == len(list)):
        return
    print(list[idx])
    print_list(list,idx+1)

list=[1,2,3,4,5]
print_list(list,0)