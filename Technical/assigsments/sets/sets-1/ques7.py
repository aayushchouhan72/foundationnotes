# 7.
# =========================================
# MISSING ALPHABET FINDER
# =========================================

# Enter a sentence and find which
# alphabets are missing.

# Menu:
# 1. Enter Sentence
# 2. Display Missing Alphabets
# 3. Count Missing Alphabets
# 4. Exit

# Requirements:
# - Use Set containing a-z.



common = set(chr(i).lower() for i in range(65, 91))

while True:
    print("1. Enter Sentence\n2. Display Missing Alphabets\n3. Count Missing Alphabets\n4. Exit")
    choice = input("Enter the your choice")
    match choice:
       case "1":
           s1=input("Enter the sentence").lower()
       case "2":
           for i in common:
                if i not in s1:
                     print(i,end=" ") 
       case "3":
              count=0
              for i in common:
                 if i not in s1:
                      count+=1
              print(f"Missing number is {count}")  
       case "4":
              break
       case _:
              print("Enter the valid choice ...")
            
