
# 3.

# =========================================================
#          MATRIX QUALITY CHECK SYSTEM
# =========================================================

# Scenario

# A manufacturing company records quality inspection values in
# matrix form. The Quality Control team wants a menu-driven
# application to analyze the inspection data and generate reports.

# The application should allow the user to:

# 1. Count Armstrong Numbers Row-wise
# 2. Count Palindrome Numbers Column-wise
# 3. Display Average of Each Row
# 4. Exit

# ---------------------------------------------------------
# Requirements
# ---------------------------------------------------------

# 1. Display the following menu repeatedly until the user selects Exit.

#    1. Count Armstrong Numbers Row-wise
#    2. Count Palindrome Numbers Column-wise
#    3. Display Average of Each Row
#    4. Exit

# 2. Read the number of rows and columns from the user.

# 3. Read all matrix elements from the user.

# 4. Based on the user's choice:

#    Choice 1 - Count Armstrong Numbers Row-wise
#    -------------------------------------------
#    Count and display the number of Armstrong numbers
#    present in each row.

#    Examples:
#    153, 370, 371, 407

# 5. Choice 2 - Count Palindrome Numbers Column-wise
#    -----------------------------------------------
#    Count and display the number of palindrome numbers
#    present in each column.

#    Examples:
#    121, 131, 444, 1221

# 6. Choice 3 - Display Average of Each Row
#    --------------------------------------
#    Calculate and display the average of each row.

# 7. Choice 4 - Exit
#    --------------------------------------
#    Display:
#    "Thank You for Using Matrix Quality Check System"

# ---------------------------------------------------------
# Sample Input/Output
# ---------------------------------------------------------

# Menu
# 1. Count Armstrong Numbers Row-wise
# 2. Count Palindrome Numbers Column-wise
# 3. Display Average of Each Row
# 4. Exit

# Enter your choice: 1

# Enter rows: 3
# Enter columns: 3

# Enter matrix elements:
# 153 121 10
# 370 22 44
# 407 15 131

# Output:
# Row 1 Armstrong Count = 1
# Row 2 Armstrong Count = 1
# Row 3 Armstrong Count = 1

# ---------------------------------------------------------

# Enter your choice: 2

# Output:
# Column 1 Palindrome Count = 0
# Column 2 Palindrome Count = 3
# Column 3 Palindrome Count = 2

# =========================================================


while True:
    print("Menu")
    print("\n1. Count Armstrong Numbers Row-wise \n2. Count Palindrome Numbers Column-wise  \n3. Display Average of Each Row \n4. Exit")
    choice=input("Enter the choice >.")
    match choice:
        case "1":
             r1 =  int(input("Enter the number of rows in  list  "))
             c1 = int(input("Enter the number of coloum in list  "))
             mat1=[]
             print("Enter the first matrix")
             for i in range(r1):
                  row=[]
                  for j in range(c1):
                       row.append(int(input()))
                  mat1.append(row)
             armestrong=[]
             for rows in mat1:
                 count=0
                 for valu in rows:
                      st = str(valu)
                      l= len(st)
                      sum = 0
                      for  i in st:
                          sum+=int(i)**l
                      if sum  == valu:
                            count+=1   
                 else:
                     armestrong.append(count)
             row=1
             for i in armestrong:
                   print(f"Prime count in {row} is {i}")
                   row+=1
                                   
        case "2":
            r1 =  int(input("Enter the number of rows in  list  "))
            c1 = int(input("Enter the number of coloum in list  "))
            mat1=[]
            print("Enter the first matrix")
            for i in range(r1):
                 row=[]
                 for j in range(c1):
                      row.append(int(input()))
                 mat1.append(row)
            palindrome=[]
            for rows in mat1:
                count=0
                for valu in rows:
                   if str(valu)[::-1] == str(valu):
                        count+=1   
                else:
                   palindrome.append(count)       
            row=1
            for i in palindrome:
                  print(f"Prime count in {row} is {i}")
                  row+=1
        case "3":
              r1 =  int(input("Enter the number of rows in  list 1 "))
              c1 = int(input("Enter the number of coloum in list 1 "))

              mat1=[]
              print("Enter the first matrix")
              for i in range(r1):
                   row=[]
                   for j in range(c1):
                        row.append(int(input()))
                   mat1.append(row)

              final=[]
              for i in range(r1):
                    sum=0
                    for j in range(c1):
                         sum+=mat1[i][j]
                    final.append(sum/len(mat1[i]))
              row=1
              for i in final:
                    print(f"Prime count in {row} is {i}")
                    row+=1
        case "4":
            print("Thankyou for using an Applcation 😎😎✅✅")
            break
        case _:
             print("ENter the valid choice ")
