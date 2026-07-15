'''
57     A
      A B
     A B C
    A B C D
   A B C D E  



'''

n= int(input("Enter n"))
i = 1


while i <= n:
    # Print leading spaces
    j = 1
    m=65
    while j <= n - i:
        print(" ", end="")
        j += 1

    # Print stars
    k = 1
    while k <= i:
        print(chr(m), end=" ")
        k += 1
        m+=1

    print()
    i += 1