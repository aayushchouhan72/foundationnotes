'''

14. Online Course Fee System

An online platform offers courses with fixed fees:

* Programming → ₹5000
* Design → ₹4000
* Marketing → ₹3000
  Discount is applied based on user type:
* Student → 20% discount
* Working Professional → 10% discount
* Others → No discount

Write a Python program to calculate final course fee.

Input:
Enter course category: Programming
Enter user type: Student

Output:
Final Course Fee: ₹4000

'''

course =  input("Enter the course you went to take >> ").lower()
type =  input("Enter your user type like student or etc >> ").lower()

if course == "programming":
        if type  == "student":
               print(f"We have 20% discount for you ")
         
        elif type  == "working professional":
               print(f"We have 10% discount for you ")
        else:
            print(f"We not have discount for you ")



elif course == "desing":
        if type  == "student":
               print(f"We have 20% discount for you ")
         
        elif type  == "working professional":
               print(f"We have 10% discount for you ")
        else:
            print(f"We not have discount for you ")


elif course == "marketinf":
        if type  == "student":
               print(f"We have 20% discount for you ")
         
        elif type  == "working professional":
               print(f"We have 10% discount for you ")
        else:
            print(f"We not have discount for you ")


              
