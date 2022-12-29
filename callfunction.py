from newcal import Calcy

class Calculation:
    def get():
        print('calculations')
calculator = Calculation
calculator.get()

print("Enter Number: " )
n = int(input())

z = "+","-","*","/"

result = 0

for i in range(n):

    num = int(input('Numbers: '))
    z = input('Operator: ')
    if z == '+':
        if i == 0:
            result = num
        else:
            result =  Calcy.add(result,num)
       
    if z == '-':
        if i == 0:
            result = num
        else:
            result = Calcy.sub(result,num)
        
    if z == '*':
        if i == 0:
            result = num
        else:
            result = Calcy.multi(result,num)
        
    if z == '/':
        if i == 0:
            result = num
        else:
            result = Calcy.divide(result,num)
print(result)   

