import math

def add(a, b):
    return a+b

def subtract(a, b):
    return a-b

def multiply(a, b):
    return a*b

def divide(a, b):
    return a/b

def sqrt(a):
    return sqrt


print("Please Select The Operation:")
print("z.add")
print("x.subtraction")
print("c.multiplication")
print("v.division")
print("b.sqrt root")
print("n.sqrt root")
print("m. sqrt root")
choice = input("Your Choice is (z/x/c/v/b/n/m):")

if choice == 'z':
    num1 = int(input("Enter First Number:"))
    num2 = int(input("Enter Second Number:"))
    print(num1,"+",num2,"=",add(num1,num2))

elif choice == 'x':
    num1 = int(input("Enter First Number:"))
    num2 = int(input("Enter Second Number:"))
    print(num1,"-",num2,"=",subtract(num1,num2))

elif choice == 'c':
    num1 = int(input("Enter First Number:"))
    num2 = int(input("Enter Second Number:"))
    print(num1,"*",num2,"=",multiply(num1,num2))

elif choice == 'v':
    num1 = int(input("Enter First Number:"))
    num2 = int(input("Enter Second Number:"))
    print(num1,"/",num2,"=",divide(num1,num2))

elif choice == 'b':
    num3 = int(input("Enter sqrt Number:"))
    squareroot = num3**(1/2)
    print("The squareroot is:",num3,"=",squareroot)
elif choice == 'n':
    n = int(input("Enter Number: "))
    print(math.sqrt(n))

elif choice == 'm':
    a = int(input("Enter Number:"))
    b = int(input("Enter Number:"))
    print(math.sqrt(a ** 2 + b ** 2))

else:
    print("Invalid Number")