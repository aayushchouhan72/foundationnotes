# 6.

# =========================================
# COMMON CHARACTER FINDER
# =========================================

# Enter two strings and find common characters.

# Menu:
# 1. Enter First String
# 2. Enter Second String
# 3. Display Common Characters
# 4. Count Common Characters
# 5. Exit

# Example:
# String1: python
# String2: typhoon

# Output:
# {p, t, h, o, n}



s1=""
s2=""
common={}
while True:
    print("1. Enter First String\n2. Enter Second String\n3. Display Common Characters\n4. Count Common Characters\n5. Exit")
    choice = input("Enter the your choice")
    match choice:
       case "1":
           s1=input("Enter the first string...")
       case "2":
           s2=input("Enter the second string...")
       case "3":
            if s1 and s2:
                 set1=set(s1)
                 set2=set(s2)
                 common =  set1.intersection(set2)
                 print(common)
            else:
                  print("Enter the strings first")         
       case "4":
               if s1 and s2:
                    set1=set(s1)
                    set2=set(s2)
                    common =  set1.intersection(set2)
                    print(common)
               else:
                    print("Enter the strings first")    
       case "5":
              break
       case _:
              print("Enter the valid choice ...")
            