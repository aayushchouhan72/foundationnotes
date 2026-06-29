'''
4. Prime Security Code Checker – Advanced

A high-security lab accepts only prime numbered access codes.

When a user enters a number, the software must:

- Check whether number is prime
- If prime, print next immediate prime number
- If not prime, print previous immediate prime number

Write a program using loops only.

Input:
29

Output:
Prime Number
Next Prime = 31

'''
n = int(input("Enter the number: "))

i = 2
while i<=n//2:
    if n%i == 0:
        break
    i += 1


if i>n//2 and n>1:
    print("Prime Number")

    m = n + 1
    while True:
        k = 2
        while k <= m // 2:
            if m%k==0:
                break
            k+=1

        if k>m//2:
            print("Next Prime =", m)
            break

        m+=1
else:
    print("Not Prime Number")

    m = n - 1
    while m >= 2:
        k = 2
        while k <= m // 2:
            if m % k == 0:
                break
            k += 1

        if k > m // 2:
            print("Previous Prime =", m)
            break

        m -= 1  