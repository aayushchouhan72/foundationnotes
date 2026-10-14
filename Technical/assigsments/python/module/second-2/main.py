from packages.armstrongnumber import *
from packages.automorphicnumber import *
from packages.evenodd import *
from packages.factorial import *
from packages.harshadnumber import *
from packages.neon import *
from packages.palindromenumber import *
from packages.perfectnumber import *
from packages.reversenumber import *
from packages.spynumber import *
from packages.strongnumber import *
from packages.sumofdigit import *
from packages.primenumber import *

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
                 print("Sum of an digit of an  number is ",digitnumber(num))
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
              break 