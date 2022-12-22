rows=int(input("Enter number:"))
k = (3 *rows) - 1
for i in range(0, rows):
    for j in range(0, k):
        print(end="-")
    k = k - 3
    for j in range(0, (i + 1)* 2):
        print("* ",end=" ")
    print(" ")

# num = 6
# factorial = 1    
# if num < 0:    
#    print(" Factorial does not exist for negative numbers")    
# elif num == 0:    
#    print("The factorial of 0 is 1")    
# else:    
#    for i in range(1,num + 1):    
#        factorial = factorial*i    
#    print("The factorial of",num,"is",factorial)

