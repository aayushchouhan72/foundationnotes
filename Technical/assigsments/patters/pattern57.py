'''
57      *
       * *
      * * *
     * * * *
    * * * * *
'''

n= int(input("Enter n"))
i = 1


while i <= n:
    # Print leading spaces
    j = 1
    while j <= n - i:
        print(" ", end="")
        j += 1

    # Print stars
    k = 1
    while k <= i:
        print("*", end=" ")
        k += 1

    print()
    i += 1