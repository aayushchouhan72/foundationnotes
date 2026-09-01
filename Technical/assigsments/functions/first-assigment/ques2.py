# 2.
# NUMBER ANALYSIS SYSTEM

# Scenario:

# A software company wants to develop a Number Analysis System. The application should be menu-driven and perform different mathematical operations on a given number.

# MENU

# 1. Check Perfect Number
# 2. Check Prime Number
# 3. Find Reverse of a Number
# 4. Calculate Factorial
# 5. Display Factors of a Number
# 6. Exit

# Requirements

# Choice 1 – Check Perfect Number

# * Accept a number from the user.
# * Pass the number to a function.
# * The function should return True if the number is Perfect, otherwise False.
# * Display an appropriate message based on the returned value.

# Choice 2 – Check Prime Number

# * Accept a number from the user.
# * Pass the number to a function.
# * The function should return a message such as "Prime Number" or "Not a Prime Number".
# * Display the returned message.

# Choice 3 – Find Reverse of a Number

# * Accept a number from the user.
# * Pass the number to a function.
# * The function should return the reversed number.
# * Display the returned value.

# Choice 4 – Calculate Factorial

# * Accept a number from the user.
# * Pass the number to a function.
# * The function should return the factorial value.
# * Display the returned value.

# Choice 5 – Display Factors of a Number

# * Accept a number from the user.
# * Pass the number to a function.
# * The function should return all factors of the given number.
# * Display the returned factors.

# Choice 6 – Exit

# Sample Output

# Enter Choice : 1

# Enter Number : 28

# 28 is a Perfect Number

# ---

# Enter Choice : 2

# Enter Number : 17

# Prime Number

# ---

# Enter Choice : 3

# Enter Number : 1234

# Reverse Number : 4321

# ---

# Enter Choice : 4

# Enter Number : 5

# Factorial : 120

# ---

# Enter Choice : 5

# Enter Number : 12

# Factors : 1 2 3 4 6 12

# ---

# Important Instructions

# 1. Create separate functions for each operation.
# 2. Use parameters to pass values to functions.
# 3. Use return statements appropriately.
# 4. Different functions should return different types of values such as Boolean, String, Integer, and Collection/List.
# 5. Avoid using global variables.
# 6. Implement the solution using a menu-driven approach.
# 7. Write meaningful function names and maintain proper code readability.
print("="*25)
print("NUMBER ANALYSIS SYSTEM")
print("="*25)


def checkprime(n):
    if n <2:
          return
    for  i in range(2,n):
          if n%i == 0:
                return False
    else:
          return True

def checkperfect(n):
     sum =0
     for i in range(1,n//2+1):
           if n%i ==  0:
                 sum+=i
     if sum  == n:
           return True
     return False

def revnumber(n):
    rev=0
    while n:
        rev =rev*10 + n%10
        n//=10
    return rev

def factorial(n):
      fac = 1
      for i in range(1,n+1):
            fac*=i
      return fac

def factors(n):
     sum =""
     for i in range(1,n//2+1):
           if n%i ==  0:
                 sum+=str(i)+" "
     return sum
      
while True:
  print('''
1. Check Perfect Number\n
2. Check Prime Number\n
3. Find Reverse of a Number\n
4. Calculate Factorial\n
5. Display Factors of a Number\n
6. Exit

''')
  choice =  input("Enter the your choice ...")
  match choice:
     case "1":
            print("Check perfect number ...")
            num =  int(input("Enter the number to check "))
            if checkperfect(num):
                  print("Given  number is perfect number ..")
            else:
                  print("Given  number is not perfect number ..")
     case "2":
            print("Check prime ...")
            num =  int(input("Enter the number to check "))
            if checkprime(num):
                  print("Prime number ..")
            else:
                  print("Not prime number ..")
     case "3":
         print("find reverse of a number ...")
         num =  int(input("Enter the number to check "))         
         print("Reverse of Given  number",revnumber(num))
     case "4":
         print("find factorial of a number ...")
         num =  int(input("Enter the number to check "))         
         print("factorial of Given  number",factorial(num))
     case "5":
             print("Display factors  of a number ...")
             num =  int(input("Enter the number to check "))         
             print("factors of Given  number is ",factors(num))
     case "6":
           print("Thankyou for using an application")
           break
     case _:
           print("Enter the Invalid input")
