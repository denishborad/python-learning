# read only
# f = open("massage.txt","r+")
# print(f.read())
# print(f.readline(5))
# for line in f:
    # print(line)

# write line

# f = open("massage.txt","w")
# f.write("First name\n")
# f.write("Second name\n")
# f.write("This is New Line\n")
# f.write("Another new line")

# append only

f = open("new massage.txt","a")
f.write("The new line")

f.close()

