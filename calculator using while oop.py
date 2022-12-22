while True:
        b = int(input("first num: "))
        c = input('operator: ')
        d = int(input('second num: '))
        if c == '+':
            print(b,"+",d,"=",b + d)
        elif c == '-':
            print(b,"-",d,"=",b - d)
        elif c == '*':
            print(b,"*",d,"=",b * d)
        elif c == '/':
            print(b,"/",d,"=",b / d)
        q = input('do you want to continue?: ')
        if q == 'y':
            continue
        else:
            break

# menu ="""
#  0. chose 0 to quit
#  1. chose + to add
#  2. chose - to sub
#  3. chose * to multi
#  4. chose / to div
# """
# chose= None


# while(chose != 0):
#     print(menu)
#     num1 =int(input('first num is: '))
#     num2 =int(input('second num is: '))
#     chose=(input("plz enter your chose: "))
#     if(chose == "+"):
#         print(num1, " + ",num2," = ",num1+num2)
#     elif(chose == "-"):
#         print(num1, " - ",num2," = ",num1-num2)
#     elif(chose == "*"):
#         print(num1, " * ",num2," = ",num1*num2)
#     elif(chose == "/"):
#         if(num2 == 0):
#             print("You can not divide by zero")
#         else:
#             print(num1, " / ",num2," = ",num1/num2)
#     else:
#         print('plz enter a correct oprator')