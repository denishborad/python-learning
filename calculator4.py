def add(n):
    return add
def sub(n):
    return sub
def mul(n):
    return mul
def div(n):
    return div

print("a.add")
print("s.sub")
print("m.mul")
print("d.div")

choice = input("chose operation (a/s/m/d): ")

print("Enter the Value of n: ")
n = int(input())
print("Enter " + str(n) + " Numbers: ")

if choice == 'a':
    sum = 0
    # print("Enter the Value of n: ")
    # n = int(input())
    # print("Enter " + str(n) + " Numbers: ")
    for i in range(n):
        num = int(input("Your Number:"))
        sum=sum+num
        print("Sum of " + str(n) + " Numbers:" + str(sum))

elif choice == 's':
    sub=0
#     print("Enter the Value of n: ")
#     n = int(input())
#     print("Enter " + str(n) + " Numbers: ")
    for i in range(n):
        num = int(input("Your Number:"))
        if i == 0:
            sub=num
        else:
            sub = sub-num
        print("Sub of " + str(n) + " Numbers:" + str(sub))

elif choice == 'm':
    mul = 0
    # print("Enter the Value of n: ")
    # n = int(input())
    # print("Enter " + str(n) + " Numbers: ")
    for i in range(n):
        num = int(input("Your Number:"))
        if i == 0:
            mul=num
        else:
            mul=mul*num
        print("Mul of " + str(n) + " Numbers:" + str(mul))

elif choice == 'd':
    # print("Enter the Value of n: ")
    # n = int(input())
    # print("Enter " + str(n) + " Numbers: ")
    result = 0
    for i in range(n):
        num = int(input("enter Number" + (str(i+1)) +":"))
        if i == 0 :
            result = num
        else: 
            result = result/num    
        print(result)
        # print("div of " + str(n) + " Numbers:" + str(div))
    
else:
    print("Number Not Entered")