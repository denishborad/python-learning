from printmultinum import sum,sub,mul,div

class cal:
    def get():
        print("Calculation")
calcu = cal
calcu.get()

print("Enter Number: " )
n = int(input())

for i in range(n):
    sum.fun(n)    
    sub.subtract(n)
    mul.multiply(n)
    div.divide(n)

    # print("calculator")
    # num=int(input("Enter number:  "))
    # a = input("plz choise operator: ")
    # if a == "+":
    # elif a == "-":
    # elif a == "*":
    # elif a == "/":
    # else:
        # print("asdf")