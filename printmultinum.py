a = "+","-","*","/"

result = 0
class sum:
    def fun(n):
        result = 0
        for i in range(n):
            num=int(input("Enter number:  "))
            a = input("plz choise operator: ")
            if a == "+":
                if i == 0:
                    num = result = num
                else:   
                    result = result+num
            print("sum",result)
Sum = sum   #Sum is object
# Sum.fun(50,20)
# Sum.fun(30,5)

class sub:
    def subtract(n):
        result = 0
        for i in range(n):
            num=int(input("Enter number:  "))
            a = input("plz choise operator: ")
            if a == "-":
                if i == 0:
                    num = result = num
                else:
                    result = result-num
            print("sub",result)
Sub = sub
# Sub.subtract(50,10)

class mul:
    def multiply(n):
        result = 0
        for i in range(n):
            num=int(input("Enter number:  "))
            a = input("plz choise operator: ")
            if a == "*":
                if i == 0:
                    num = result = num
                else:
                    result = result*num
            print("mul",result)
Mul = mul
# Mul.multiply(50,2)

class div:
    def divide(n):
        result = 0 
        for i in range(n):
            num=int(input("Enter number:  "))
            a = input("plz choise operator: ")
            if a == "/":
                if i == 0:
                    num = result = num
                else:
                    result = result/num
            print("div",result)
Div = div
# Div.divide(50,2)
