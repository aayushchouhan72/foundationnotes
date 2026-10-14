'''
57     1
      1 2
     1 2 3
    1 2 3 4
   1 2 3 4 5


'''

n= int(input("Enter n"))
i = 1


while i <= n:
    # Print leading spaces
    j = 1
    m=1
    while j <= n - i:
        print(" ", end="")
        j += 1

    # Print stars
    k = 1
    while k <= i:
        print(m, end=" ")
        k += 1
        m+=1

    print()
    i += 1