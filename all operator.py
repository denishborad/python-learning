# print("Enter the Value of n: ")
# while True:
#         b = int(input())
#         print("Enter " + str(b) + " Numbers: ")
#         # b = int(input("first num: "))
#         c = input('operator: ')
#         # d = int(input('second num: '))
#         if c == '+':
#             print(b,"+",d,"=",b + d)
#         elif c == '-':
#             print(b,"-",d,"=",b - d)
#         elif c == '*':
#             print(b,"*",d,"=",b * d)
#         elif c == '/':
#             print(b,"/",d,"=",b / d)
#         q = input('do you want to continue?: ')
#         if q == 'y':
#             continue
#         else:
#             break


print("Enter Number: ")
n = int(input())


# Operator = ["+","-","*","/"]
# a = Operator

a = "+","-","*","/"

result = 0


for i in range(n):
    num = int(input("Enter Num: "))
    a   = input("Select Operator: ")
    if a == "+":    
        if i == 0:
            num = result = num
        else:
            result = result + num
        # print("Your Sum",result)
    if a == "-":
        if i == 0:
            result = num
        else:
            result = result - num
        # print("Your Sub",result)
    if a == "*":
        if i == 0:
            result = num
        else:
            result = result * num
        # print("Your Mul",result)
    if a == "/":
        if i == 0:
            result = num
        else:
            result = result / num
        # print("Your Div",result)
    print(result)