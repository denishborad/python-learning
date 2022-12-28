from newcal import calcy

class calculation:
    def get():
        print('calculations')

n = int(input('Enter:'))
print('Enter ' + str(n) + ' Numbers:')

z = '+','-','*','/'

result = 0

for i in range(n):

    num = int(input('Numbers: '))
    z = input('Operator: ')
    # b = int(input('Numbers: '))
    if z == '+':
        if i == 0:
            num = result = num
        else:
            result =  calcy.add(result,add)
        print(result)
       
    if z == '-':
        if i == 0:
            result = num
        else:
            result = calcy.sub(result,sub)
        print(result)
        
    if z == '*':
        if i == 0:
            result = num
        else:
            result = calcy.multi(result,multi)
        print(result)
        
    if z == '/':
        if i == 0:
            result = num
        else:
            result = calcy.divide(result,divide)
        print(result)
        

