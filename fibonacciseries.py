# def febonacci(n):
#     if(n<0):
#         print("Incorrect Number")
#     elif n == 0:
#         return 0
#     elif n == 1 :
#         return 1
#     else:
#         return febonacci(n)  
# print(febonacci(6))  

def fibonacci(n):
    a = 0
    b = 1
    if n<0:
        print("Incorrect")
    elif n == 0:
        print(0)
        return 0
    elif n == 1:
        print(b)
        return b
    else:
        for i in range(1,n):
            c = a + b
            a = b
            b = c
            print(b)
        return b

print(fibonacci(6))