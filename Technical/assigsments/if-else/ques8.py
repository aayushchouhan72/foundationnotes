'''
8. Number Property Checker
   A system evaluates number properties:

* If number % 2 == 0 → Even number
* If number % 5 == 0 → Divisible by 5

Input:
Enter number: 20

Output:
Even number
Divisible by 5


'''


num  = int(input("Enter your number to check :- "))

if num%2 ==0:
    if num%5 == 0:
          print("Enter number is even and divisible by 5")
    else:
        print("Enter number is  Even number")
else:
   print("Give number is ODD number ")