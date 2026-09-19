# Assignment: Menu-Driven Number Analysis System

# Create a Menu-Driven Number Analysis System in Python.

# The program should continuously display a menu and allow the user to select different operations related to numbers.

# Each operation must be implemented using a separate function.

# The program should continue running until the user selects Exit.

# Main Menu

# When the program starts, display:

# ========================================
#        NUMBER ANALYSIS SYSTEM
# ========================================

# 1. Check Perfect Number
# 2. Check Palindrome Number
# 3. Check Strong Number
# 4. Check Armstrong Number
# 5. Check Prime Number
# 6. Check Even or Odd
# 7. Find Factorial
# 8. Find Sum of Digits
# 9. Reverse a Number
# 10. Find Number of Digits
# 11. Check Automorphic Number
# 12. Check Neon Number
# 13. Check Spy Number
# 14. Check Harshad Number
# 15. Exit

# Enter your choice:

# The program must ask for the required input only after the user selects an operation.

# CASE 1: Perfect Number
# Function

# Create:

# def is_perfect(number):
# What to read from the user?

# Read:

# Enter a number:
# Requirement

# Check whether the given number is a Perfect Number.

# A number is perfect if the sum of its proper divisors is equal to the number itself.

# Example:

# 6

# Proper divisors:

# 1 + 2 + 3 = 6

# Therefore:

# 6 is a Perfect Number
# Sample Output
# Enter a number: 6

# 6 is a Perfect Number

# For:

# Enter a number: 10

# 10 is not a Perfect Number
# CASE 2: Palindrome Number
# Function

# Create:

# def is_palindrome(number):
# What to read from the user?
# Enter a number:
# Requirement

# Check whether the number reads the same from both directions.

# Example:

# 121

# Reverse:

# 121

# Therefore:

# 121 is a Palindrome Number
# Sample Output
# Enter a number: 121

# 121 is a Palindrome Number
# CASE 3: Strong Number
# Function

# Create:

# def is_strong(number):
# What to read from the user?
# Enter a number:
# Requirement

# A number is a Strong Number if the sum of the factorials of its digits is equal to the original number.

# Example:

# 145

# Calculation:

# 1! + 4! + 5!

# 1 + 24 + 120

# = 145

# Therefore:

# 145 is a Strong Number
# Sample Output
# Enter a number: 145

# 145 is a Strong Number
# CASE 4: Armstrong Number
# Function

# Create:

# def is_armstrong(number):
# What to read from the user?
# Enter a number:
# Requirement

# Check whether the given number is an Armstrong Number.

# For a 3-digit number:

# 153

# Calculation:

# 1³ + 5³ + 3³

# 1 + 125 + 27

# = 153

# Therefore:

# 153 is an Armstrong Number
# Sample Output
# Enter a number: 153

# 153 is an Armstrong Number
# Important

# Do not hard-code the number of digits.

# The function should work for numbers having different numbers of digits.

# CASE 5: Prime Number
# Function

# Create:

# def is_prime(number):
# What to read from the user?
# Enter a number:
# Requirement

# Check whether the given number is prime.

# A prime number has exactly two factors:

# 1 and itself

# Example:

# 17

# Factors:

# 1, 17

# Therefore:

# 17 is a Prime Number
# Sample Output
# Enter a number: 17

# 17 is a Prime Number
# CASE 6: Even or Odd
# Function

# Create:

# def check_even_odd(number):
# Input
# Enter a number:
# Requirement

# Determine whether the number is:

# Even

# or

# Odd
# Example
# Enter a number: 24

# 24 is an Even Number
# CASE 7: Factorial
# Function

# Create:

# def factorial(number):
# Input
# Enter a number:
# Requirement

# Find the factorial of the given number.

# Example:

# 5! = 5 × 4 × 3 × 2 × 1
#    = 120
# Output
# Enter a number: 5

# Factorial = 120
# CASE 8: Sum of Digits
# Function

# Create:

# def sum_of_digits(number):
# Input
# Enter a number:
# Requirement

# Calculate the sum of all digits.

# Example:

# Enter a number: 5832

# 5 + 8 + 3 + 2 = 18
# Output
# Sum of digits = 18
# CASE 9: Reverse a Number
# Function

# Create:

# def reverse_number(number):
# Input
# Enter a number:
# Requirement

# Reverse the given number.

# Example:

# Enter a number: 12345

# Reverse = 54321
# CASE 10: Count Number of Digits
# Function

# Create:

# def count_digits(number):
# Input
# Enter a number:
# Requirement

# Find how many digits are present in the number.

# Example:

# Enter a number: 98765

# Number of digits = 5
# CASE 11: Automorphic Number
# Function

# Create:

# def is_automorphic(number):
# Input
# Enter a number:
# Requirement

# A number is Automorphic if its square ends with the same number.

# Example:

# 25² = 625

# 625 ends with:

# 25

# Therefore:

# 25 is an Automorphic Number
# Output
# Enter a number: 25

# 25 is an Automorphic Number
# CASE 12: Neon Number
# Function

# Create:

# def is_neon(number):
# Input
# Enter a number:
# Requirement

# A number is Neon if the sum of the digits of its square is equal to the original number.

# Example:

# 9² = 81

# 8 + 1 = 9

# Therefore:

# 9 is a Neon Number
# Output
# Enter a number: 9

# 9 is a Neon Number
# CASE 13: Spy Number
# Function

# Create:

# def is_spy(number):
# Input
# Enter a number:
# Requirement

# A number is a Spy Number if:

# Sum of digits = Product of digits

# Example:

# 1124

# Sum:

# 1 + 1 + 2 + 4 = 8

# Product:

# 1 × 1 × 2 × 4 = 8

# Therefore:

# 1124 is a Spy Number
# CASE 14: Harshad Number
# Function

# Create:

# def is_harshad(number):
# Input
# Enter a number:
# Requirement

# A number is a Harshad Number if it is completely divisible by the sum of its digits.

# Example:

# 18

# Sum of digits:

# 1 + 8 = 9

# Check:

# 18 % 9 == 0

# Therefore:

# 18 is a Harshad Number
# CASE 15: Exit

# When the user selects:

# 15

# Display:

# Thank you for using Number Analysis System!
# Program terminated.

# Then terminate the program.

# Important Programming Requirements

# Students must follow all of these rules.

# 1. Separate Function for Every Operation

# Do not write all logic directly inside the menu.

# For example:

# def is_prime(number):
#     # logic
# def is_palindrome(number):
#     # logic
# def factorial(number):
#     # logic
# 2. Functions Must Receive Input Through Parameters

# Correct:

# def is_prime(number):

# Incorrect:

# def is_prime():
#     number = int(input("Enter number: "))

# For this assignment, the main program should read the input and pass it to the function.

# 3. Functions Should Return Results

# For example:

# result = is_prime(number)

# Then use:

# if result:
#     print("Prime Number")
# else:
#     print("Not Prime Number")
# 4. Menu Must Run Continuously

# Use:

# while True:

# The menu should appear again after every operation.

# Example:

# 1. Perfect
# 2. Palindrome
# 3. Strong
# ...
# 15. Exit

# Enter choice: 1

# Enter number: 6

# 6 is a Perfect Number


# ========================================
#        NUMBER ANALYSIS SYSTEM
# ========================================

# 1. Perfect
# 2. Palindrome
# ...
# 5. Invalid Choice

# If the user enters:

# 20

# Display:

# Invalid Choice!
# Please select a choice between 1 and 15.

# Then display the menu again.

# 6. Input Should Be Taken According to the Selected Case

# For example, if the user selects:

# 1

# then:

# Enter a number:

# should be displayed.

# Do not take input for all 14 operations at the beginning.

# Expected Program Flow
# ========================================
#        NUMBER ANALYSIS SYSTEM
# ========================================

# 1. Check Perfect Number
# 2. Check Palindrome Number
# 3. Check Strong Number
# 4. Check Armstrong Number
# 5. Check Prime Number
# 6. Check Even or Odd
# 7. Find Factorial
# 8. Find Sum of Digits
# 9. Reverse a Number
# 10. Find Number of Digits
# 11. Check Automorphic Number
# 12. Check Neon Number
# 13. Check Spy Number
# 14. Check Harshad Number
# 15. Exit

# Enter your choice: 4

# Enter a number: 153

# 153 is an Armstrong Number

# ----------------------------------------

# Press Enter to continue...

# ========================================
#        NUMBER ANALYSIS SYSTEM
# ========================================

# 1. Check Perfect Number
# 2. Check Palindrome Number
# 3. Check Strong Number
# 4. Check Armstrong Number
# 5. Check Prime Number
# 6. Check Even or Odd
# 7. Find Factorial
# 8. Find Sum of Digits
# 9. Reverse a Number
# 10. Find Number of Digits
# 11. Check Automorphic Number
# 12. Check Neon Number
# 13. Check Spy Number
# 14. Check Harshad Number
# 15. Exit

# Enter your choice: 15

# Thank you for using Number Analysis System!
# Program terminated.


# # 

def perfectnumber(x):
    '''Check Perfect Number'''
    sum=0
    for i  in range(1,x//2+1):
          if x%i == 0:
                sum+=i
    if sum ==  x:
           return True
    else:
          return False

def palindromenumber(x):
       '''Check the palindrom number ...'''
       num =str(x)
       return num == num[::-1]

def strongnumber(x):
      num=0 
      def factorial(y):
            fac=1
            for i in range(y+1):
                  fac*=i
            return fac   
      for i in str(x):
             num+=factorial(int(i))
      return num
def armstrongnumber(x):
      sum = 0
      for i in str(x):
          sum += int(i)**len(str(x))  
      if sum ==  x:
             return True
      return False

def primenumber(x):
    isprime=False
    for i in range(2,x):
           if x%i ==  0:
                  return isprime
    else:
          isprime=True
    return isprime

def evenoddcheck(x):
    
    if x%2:
           return True
    return False
def factorail(y):
      fac=1
      for i in range(y+1):
            fac*=i
      return fac 
<<<<<<< HEAD
def digitsum(x):
       sum =0
       for i  in str(x):
              sum += int(i)
       return sum 
=======

>>>>>>> b797c5bf1c17733765b2cdb48c3ae77a9cfec689

def digitrev(x):
       return int(str(x)[::-1])

def digitnumber(x):
      return len(str(x))

def Automorphic(x):
       numlen=len(str(x))
       squr=x**2
       removed = str(squr)[-numlen:]
       if removed ==  x:
             return True
       return False

def NeonNumber(x):
      squr=x**2
      dig=0
      for i in str(squr):
            dig += int(i)
      if dig ==  x:
            return True
      return False 

def spyNumber(x):
      pro = 1
      for i in str(x):
            pro*=int(i) 
      sum = digitsum(x)
      if sum == pro:
             return True
      return False
      

def HarshadNumber(x):
    sum = digitsum(x)
    if x%sum == 0:
           return True 
    return False

while True: 
    print("""
========================================
       NUMBER ANALYSIS SYSTEM
========================================

1. Check Perfect Number
2. Check Palindrome Number
3. Check Strong Number
4. Check Armstrong Number
5. Check Prime Number
6. Check Even or Odd
7. Find Factorial
8. Find Sum of Digits
9. Reverse a Number
10. Find Number of Digits
11. Check Automorphic Number
12. Check Neon Number
13. Check Spy Number
14. Check Harshad Number
15. Exit
""")

    choice =  input("Enter the choice ..")
    match choice:
         case "1":
               num = int(input("Enter the number to check .."))
               if perfectnumber(num):
                      print("Given number is an  perfect number ...")
               else:
                      print("Given number is not an pefecr number ...")
         case "2":
                num = int(input("Enter the number to check .."))
                if palindromenumber(num):
                       print("Given number is an palindrom number ...")
                else:
                       print("Given number is not an  palindrom number ...")
         case "3":
                num = int(input("Enter the number to check .."))
                if strongnumber(num) == num:
                       print("Given number is an strong  number ...")
                else:
                       print("Given number is not an  strong  number ...")
         case "4":
               num = int(input("Enter the number to check .."))
               if armstrongnumber(num):
                      print("Given number is an armstrongnumber  number ...")
               else:
                      print("Given number is not an  armstrongnumber  number ...")
         case "5":
               num = int(input("Enter the number to check .."))
               if primenumber(num):
                      print("Given number is an primenumber...")
               else:
                      print("Given number is not an  primenumber...")
             
         case "6":
               num = int(input("Enter the number to check .."))
               if evenoddcheck(num):
                      print("Given number is an even number...")
               else:
                      print("Given number is an odd number...")
         case "7":
               num = int(input("Enter the number to check .."))
               print("Factorail of an number is ",factorail(num))
         case "8":
                 num = int(input("Enter the number to check .."))
                 print("Sum of an digit of an  number is ",digitsum(num))
         case "9":
                 num = int(input("Enter the number to check .."))
                 print("reverse  number is ",digitrev(num))
         case "10":
                 num = int(input("Enter the number to check .."))
                 print("number of digit  is ",digitnumber(num))
         case "11":
               num = int(input("Enter the number to check .."))
               if Automorphic(num):
                      print("Given number is an Automorphic number ...")
               else:
                      print("Given number is an not Automorphic number ...")
         case "12":
               num = int(input("Enter the number to check .."))
               if NeonNumber(num):
                      print("Given number is an Neon number ...")
               else:
                      print("Given number is an not Neon number ...")
         case "13":
               num = int(input("Enter the number to check .."))
               if spyNumber(num):
                      print("Given number is an spy number ...")
               else:
                      print("Given number is an not spy number ...")

         case "14":
               num = int(input("Enter the number to check .."))
               if  HarshadNumber(num):
                      print("Given number is an  Harshad Number ...")
               else:
                      print("Given number is an not  Harshad Number ...")
         case "15":
               pass