def add(a, b, c, d, e):
    return a+b+c+d+e

def subtract(a, b, c, d, e):
    return a-b-c-d-e

def multiply(a, b, c, d, e):
    return a*b*c*d*e

def divide(a, b, c, d, e):
    return a/b/c/d/e

print("Please Select The Operation:")
print("z.add")
print("x.subtraction")
print("c.multiplication")
print("v.division")

choice = input("Your Choice is (z/x/c/v):")

num1 = int(input("Enter Number:"))
num2 = int(input("Enter Number:"))
num3 = int(input("Enter Number:"))
num4 = int(input("Enter Number:"))
num5 = int(input("Enter Number:"))

if choice == 'z':
    print(num1,"+",num2,"+",num3,"+",num4,"+",num5,"=",add(num1,num2,num3,num4,num5))

elif choice == 'x':
    print(num1,"-",num2,"-",num3,"-",num5,"-",num5,"=",subtract(num1,num2,num3,num4,num5))

elif choice == 'c':
    print(num1,"*",num2,"*",num3,"*",num4,"*",num5,"=",multiply(num1,num2,num3,num4,num5))

elif choice == 'v':
    print(num1,"/",num2,"/",num3,"/",num4,"/",num5,"=",divide(num1,num2,num3,num4,num5))

else:
    print("Invalid Number")