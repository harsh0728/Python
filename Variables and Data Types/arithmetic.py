#arithmetic operators

a=10
b=5

print("a+b=",a+b)
print("a-b=",a-b)
print("a*b=",a*b)
print("a/b=",a/b)
print("a//b=",a//b) #floor division
print("a%b=",a%b) #modulo
print("a**b=",a**b) #exponentiation a^b

#relational operators
a=50
b=20

print("a==b",a==b)
print("a!=b",a!=b)
print("a>b",a>b)
print("a<b",a<b)
print("a>=b",a>=b)
print("a<=b",a<=b)

#Assignment operators
a=10
a+=5 #a=a+5
print("a=",a)
a-=3 #a=a-3
print("a=",a)
a*=2 #a=a*2
print("a=",a)
a/=4 #a=a/4
print("a=",a)
a//=2 #a=a//2
print("a=",a)

#Logical operators
x=True
y=False
print("x and y =",x and y)
print("x or y =",x or y)
print("not x =",not x)


# Type conversion
a=2
b=4.23

print (a+b) #5.23
print (a+int(b)) #6

#Inputs
num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
print("Type of sum: ",type(num1+num2),"Sum:",num1+num2)
