def show(n):
    if (n==0):
        return
    print(n)
    show(n-1)


show(5)

def fact(n):
    if (n==0 or n==1):
        return 1 
    return n*fact(n-1)
    
print("Factorial of 5 is:",fact(5))