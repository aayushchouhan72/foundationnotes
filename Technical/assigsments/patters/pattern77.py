'''
1
1 2
1  3
1   4
1  3
1 2
1
'''

n = int(input("Enter the number of lines: "))


for i in range(1, n + 1):
    if i == 1:
        print(1)
    else:
        print(1, end="")
        print(" " * (i - 2), end="")
        print(i)


for i in range(n - 1, 0, -1):
    if i == 1:
        print(1)
    else:
        print(1, end="")
        print(" " * (i - 2), end="")
        print(i)