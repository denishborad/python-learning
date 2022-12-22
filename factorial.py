# n = int(input("Enter Number:"))
# factorial = 1
# if n<0:
#     print("Plz Enter Positive Number")
# elif n==0:
#     print("Factorial of zero is 1")
# else:
#     for i in range(1,n+1):
#         factorial = factorial * i
#     print("The factorial",n,"is",factorial)

# def fact(a):
#     if a < 0:
#         return 0
#     elif a == 1:
#         return 1
#     else:
#         return (a * fact(a - 1))
# n = int(input("Enter Number:"))
# result = fact(n)
# print("The factorial of ", n, "is ",result)

def factorial(n):
    if n < 0:
        return 0
    elif n == 0 or n == 1:
        return 1
    else:
        fact = 1
        while(n > 1):
            fact = fact * n
            n = n - 1
        return fact 
num = int(input("Enter Number:"))
print("Factorial of",num,"is",factorial(num))

# import math
# def factorial(a):
#     print(math.factorial(a))

# n = int(input("Enter Number: "))

# print("The Factorial of ", n, "is ",factorial(n))