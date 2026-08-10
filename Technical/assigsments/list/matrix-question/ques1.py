# 1.
# =========================================================
#         MATRIX OPERATIONS MANAGEMENT SYSTEM
# =========================================================


# A data analysis company stores numerical information in matrix form.
# To help employees perform matrix-related operations efficiently,
# the company wants a menu-driven application.

# The application should allow the user to:

# 1. Add Two Matrices
# 2. Subtract Two Matrices
# 3. Compare Two Matrices
# 4. Exit

# The user must enter the number of rows, columns, and all matrix
# elements. The program should perform the selected operation and
# display the result.

# ---------------------------------------------------------
# Requirements
# ---------------------------------------------------------

# 1. Display the following menu repeatedly until the user chooses Exit.

#    1. Add Two Matrices
#    2. Subtract Two Matrices
#    3. Compare Two Matrices
#    4. Exit

# 2. Read the number of rows and columns from the user.

# 3. Read all elements of Matrix A and Matrix B from the user whenever
#    required.

# 4. Based on the user's choice:

#    Choice 1 - Add Two Matrices
#    --------------------------------
#    Add corresponding elements of both matrices and display
#    the resultant matrix.

# 5. Choice 2 - Subtract Two Matrices
#    --------------------------------
#    Subtract corresponding elements of Matrix B from Matrix A
#    and display the resultant matrix.

# 6. Choice 3 - Compare Two Matrices
#    --------------------------------
#    Check whether both matrices are equal.

#    Two matrices are considered equal if:
#    - They have the same dimensions.
#    - Corresponding elements are equal.

#    Display:
#    "Matrices are Equal"
#    or
#    "Matrices are Not Equal"

# 7. Choice 4 - Exit
#    --------------------------------
#    Display:
#    "Thank You for Using Matrix Operations Management System"

# ---------------------------------------------------------
# Sample Input/Output
# ---------------------------------------------------------

# Menu
# 1. Add Two Matrices
# 2. Subtract Two Matrices
# 3. Compare Two Matrices
# 4. Exit

# Enter your choice: 1

# Enter number of rows: 2
# Enter number of columns: 2

# Enter Matrix A:
# 1 2
# 3 4

# Enter Matrix B:
# 5 6
# 7 8

# Result Matrix:
# 6 8
# 10 12

# ---------------------------------------------------------

# Menu
# 1. Add Two Matrices
# 2. Subtract Two Matrices
# 3. Compare Two Matrices
# 4. Exit

# Enter your choice: 3

# Enter number of rows: 2
# Enter number of columns: 2

# Enter Matrix A:
# 1 2
# 3 4

# Enter Matrix B:
# 1 2
# 3 4

# Output:
# Matrices are Equal

# ---------------------------------------------------------

# Menu
# 1. Add Two Matrices
# 2. Subtract Two Matrices
# 3. Compare Two Matrices
# 4. Exit

# Enter your choice: 4

# Output:
# Thank You for Using Matrix Operations Management System

# =========================================================

while True:
    print("Menu")
    print("\n1. Add Two Matrices \n2. Subtract Two Matrices  \n3. Compare Two Matrices \n4. Exit")
    choice=input("Enter the choice >.")
    match choice:
        case "1":
             r1 =  int(input("Enter the number of rows in  list 1 "))
             c1 = int(input("Enter the number of coloum in list 1 "))
             mat1=[]
             print("Enter the first matrix")
             for i in range(r1):
                  row=[]
                  for j in range(c1):
                       row.append(int(input()))
                  mat1.append(row)
             r2 =  int(input("Enter the number of rows in  list 2 "))
             c2 = int(input("Enter the number of coloum in list 2 "))
             mat2=[]
             print("Enter the second matrix")
             for i in range(r2):
                  row=[]
                  for j in range(c2):
                       row.append(int(input()))
                  mat2.append(row)
             if(r1 == r2 and c1 == c2):
                  flag=False
                  result=[]
                  for i in range(r1):
                       row=[]
                       for j in range(c1):
                            row.append(mat1[i][j] + mat2[i][j])
                       result.append(row)
 
                  print("Ssubtracted matrix is :- ")
                  for rows in result:
                       print(*rows)                           
             else:
                 print("Invalid matrix for comparison ") 
        case "2":
            r1 =  int(input("Enter the number of rows in  list 1 "))
            c1 = int(input("Enter the number of coloum in list 1 "))
            
            mat1=[]
            print("Enter the first matrix")
            for i in range(r1):
                 row=[]
                 for j in range(c1):
                      row.append(int(input()))
                 mat1.append(row)
            r2 =  int(input("Enter the number of rows in  list 2 "))
            c2 = int(input("Enter the number of coloum in list 2 "))
            mat2=[]
            print("Enter the second matrix")
            for i in range(r2):
                 row=[]
                 for j in range(c2):
                      row.append(int(input()))
                 mat2.append(row)
            if(r1 == r2 and c1 == c2):
                 flag=False
                 result=[]
                 for i in range(r1):
                      row=[]
                      for j in range(c1):
                           row.append(mat1[i][j] - mat2[i][j])
                      result.append(row)

                 print("Ssubtracted matrix is :- ")
                 for rows in result:
                      print(*rows)                           
            else:
                print("Invalid matrix for comparison ")
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

              r2 =  int(input("Enter the number of rows in  list 2 "))
              c2 = int(input("Enter the number of coloum in list 2 "))

              mat2=[]
              print("Enter the second matrix")
              for i in range(r2):
                   row=[]
                   for j in range(c2):
                        row.append(int(input()))
                   mat2.append(row)

              if(r1 == r2 and c1 == c2):
                   flag=False
                   for i in range(r1):
                        if flag:
                             break
                        for j in range(c1):
                             if mat1[i][j] == mat2[i][j]:
                                   pass
                             else:
                                  flag=True
                                  break
                   if flag:
                        print("Both matrix are not same")
                   else:
                        print("Both matrix are same ")                        
              else:
                  print("Invalid matrix for comparison ")
        case "4":
            print("Thankyou for using an Applcation 😎😎✅✅")
            break
        case _:
             print("ENter the valid choice ")
