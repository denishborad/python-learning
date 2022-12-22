# rows=6
# k = (2 * rows) - 2
# for i in range(0, rows):
#     for j in range(0, k):
#         print(end="-")
#     k = k - 2
#     for j in range(0, i + 1):
#         print("* ",end=' ')
#     print(" ")

# n = 10
# m = (2 * n) - 2
# for i in range(0, n):
#     for j in range(0, m):
#         print(end="-")
#     m = m - 1
#     for j in range(0, i  + 1):
#         print("* ", end=' ')
#     print(" ")

size = 8
m = (size) - 1
for i in range(0, size):
    for j in range(0, m):
        print(end="-")
    m = m - 1
    for j in range(0, i + 1):
        print("* ",end="")
    print("")