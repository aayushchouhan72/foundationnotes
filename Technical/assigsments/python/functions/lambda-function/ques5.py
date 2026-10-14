# QNO:
# Employee Data Processing System

# A company stores information about its employees in two forms:

# A list of employee ages.
# A string containing employee names separated by spaces.

# The HR department wants a Python application that can perform different operations on this data through a menu-driven system. To make the application modular and easy to maintain, each operation must be implemented using a separate function that accepts data as a parameter and returns the result.

# Problem Statement

# Develop a menu-driven Python application called Employee Data Processing System.

# The program should allow the HR department to perform the following operations:

# Functions on Employee Ages (List)
# 1. find_second_highest_age(age_list)
# Accept a list of employee ages.
# Return the second highest age.
# 2. count_senior_employees(age_list)
# Accept a list of employee ages.
# Consider employees aged 50 years or above as senior employees.
# Return the count of senior employees.
# 3. remove_duplicate_ages(age_list)
# Accept a list of employee ages.
# Return a new list after removing duplicate ages while maintaining the original order.
# Functions on Employee Names (String)
# 4. count_names_starting_with_vowel(names)
# Accept a string containing employee names separated by spaces.
# Return the number of names that start with a vowel (A, E, I, O, U).
# 5. longest_name(names)
# Accept a string containing employee names separated by spaces.
# Return the employee name having the maximum number of characters.
# Menu
# ========== EMPLOYEE DATA PROCESSING SYSTEM ==========
# 1. Find Second Highest Employee Age
# 2. Count Senior Employees
# 3. Remove Duplicate Ages
# 4. Count Names Starting with a Vowel
# 5. Find Longest Employee Name
# 6. Exit
# ====================================================
# Enter your choice:
# Sample Input
# Employee Ages:
# 34 55 29 60 55 42 60 51

# Employee Names:
# Ajay Rahul Esha Omkar Ishita Neha
# Sample Output
# Second Highest Age : 55
# Senior Employees : 4
# Unique Ages : [34, 55, 29, 60, 42, 51]
# Names Starting with Vowel : 3
# Longest Employee Name : Ishita
# Instructions
# Implement all operations using separate functions.
# Each function must accept parameters and return the result.
# Do not print results inside the functions.
# The menu should continue to appear until the user selects Exit.
# Display an appropriate message for an invalid choice.
# Use meaningful function and variable names and follow proper indentation

print("="*25)
print("EMPLOYEE DATA PROCESSING SYSTEM ")
print("="*25)

def  find_second_highest_age(age_list):
     sort_age=  sorted(age_list)
     return sort_age[-2]
# Accept a list of employee ages.
# Return the second highest age.
def count_senior_employees(age_list):
    senior= list(filter(lambda x:x>=50,age_list)) 
    return senior
# Accept a list of employee ages.
# Consider employees aged 50 years or above as senior employees.
# Return the count of senior employees.

def  remove_duplicate_ages(age_list):
    unique= set(age_list)
    return len(unique)
# Accept a list of employee ages.
# Return a new list after removing duplicate ages while maintaining the original order.
# Functions on Employee Names (String)
def  count_names_starting_with_vowel(names):
     return len(list(filter(lambda x: x[0] in "AEIOUaeiou",names)))
# Accept a string containing employee names separated by spaces.
# Return the number of names that start with a vowel (A, E, I, O, U).
def longest_name(names):
     return sorted(names, key=len)

users = []
product=[]   
while True:
  print('''
 1. Find Second Highest Employee Age\n
 2. Count Senior Employees\n
 3. Remove Duplicate Ages\n
 4. Count Names Starting with a Vowel\n
 5. Find Longest Employee Name\n
 6. Exit\n

''')
  choice =  input("Enter the your choice ...")
  match choice:
      case "1":
           ages =  list(map(int,input("Enter the employee Age ").split(" ")))
           print("Second Highest age is ",find_second_highest_age(ages))
      case "2":
          ages =  list(map(int,input("Enter the employee Age ").split(" ")))
          print("Senior employee Age ",count_senior_employees(ages)) 
      case "3":
          ages =  list(map(int,input("Enter the employee Age ").split(" ")))
          print("employee unique Ages ",remove_duplicate_ages(ages)) 
         
      case "4":
          ages =  list(map(str,input("Enter the employee names ").split(" ")))
          print("Employe whose name starts with an vowel  ",count_names_starting_with_vowel(ages)) 
      case "5":
          ages =  list(map(str,input("Enter the employee names ").split(" ")))
          print("Longest employee name :-",longest_name(ages)) 
      case "6":
           print("Thankyou for using an application")
           break
      case _:
           print("Enter the Invalid input")
