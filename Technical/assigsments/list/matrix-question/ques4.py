# 4.

# =========================================================
#         MATRIX DIAGONAL ANALYSIS SYSTEM
# =========================================================

# Scenario

# A security company stores surveillance data in matrix form.
# The analyst wants a menu-driven application to examine the
# diagonal elements of the matrix and generate reports.

# The application should allow the user to:

# 1. Display Main Diagonal Elements
# 2. Display Secondary Diagonal Elements
# 3. Compare Main and Secondary Diagonal Sums
# 4. Exit

# ---------------------------------------------------------
# Requirements
# ---------------------------------------------------------

# 1. Display the following menu repeatedly until the user selects Exit.

#    1. Display Main Diagonal Elements
#    2. Display Secondary Diagonal Elements
#    3. Compare Main and Secondary Diagonal Sums
#    4. Exit

# 2. Read the size of a square matrix from the user.

# 3. Read all matrix elements from the user.

# 4. Based on the user's choice:

#    Choice 1 - Display Main Diagonal Elements
#    -----------------------------------------
#    Display all elements present in the main diagonal.

# 5. Choice 2 - Display Secondary Diagonal Elements
#    ----------------------------------------------
#    Display all elements present in the secondary diagonal.

# 6. Choice 3 - Compare Main and Secondary Diagonal Sums
#    ---------------------------------------------------
#    Calculate the sum of both diagonals and display:

#    - Main Diagonal Sum
#    - Secondary Diagonal Sum
#    - Which diagonal has the greater sum
#    - Or whether both sums are equal

# 7. Choice 4 - Exit
#    -----------------------------------------
#    Display:
#    "Thank You for Using Matrix Diagonal Analysis System"

# ---------------------------------------------------------
# Sample Input/Output
# ---------------------------------------------------------

# Enter size of matrix: 3

# Enter matrix elements:

# 1 2 3
# 4 5 6
# 7 8 9

# Menu
# 1. Display Main Diagonal Elements
# 2. Display Secondary Diagonal Elements
# 3. Compare Main and Secondary Diagonal Sums
# 4. Exit

# Enter your choice: 1

# Output:
# Main Diagonal Elements:
# 1 5 9

# ---------------------------------------------------------

# Enter your choice: 2

# Output:
# Secondary Diagonal Elements:
# 3 5 7

# ---------------------------------------------------------

# Enter your choice: 3

# Output:
# Main Diagonal Sum = 15
# Secondary Diagonal Sum = 15
# Both Diagonal Sums are Equal

# =========================================================

while True:
    print("Menu")
    print("\n1.Display Main Diagonal Elements\n2.Display Secondary Diagonal Elements \nCompare Main and Secondary Diagonal Sums\n4. Exit")
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
             maindiagonal=[]
             for i in range(r1):
                  maindiagonal.append(mat1[i][i])
             print(*maindiagonal)                                   
        case "2":
            r1 =  int(input("Enter the number of rows in  list  "))
            c1 = int(input("Enter the number of coloum in list  "))
            mat1=[]
            print("Enter the first matrix")
            for i in range(r1):
                 row=[]
                 print("Enter the element of row ",i+1)
                 for j in range(c1):
                      row.append(int(input()))
                 mat1.append(row)
            max=len(mat1)-1
            secondarydiagonal=[]
            for i in range(r1):
                    secondarydiagonal.append(mat1[i][max])
                    max-=1
                               
            print(*secondarydiagonal)  
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
              secondarydiagonal=[]
              max=len(mat1)-1
              for i in range(r1):
                      secondarydiagonal.append(mat1[i][max])
                      max-=1

              maindiagonal=[]
              for i in range(r1):
                   maindiagonal.append(mat1[i][i])

              if sum(maindiagonal) == sum(secondarydiagonal):
                    print("Some of both diagonal is equal ..") 
              else:
                    print("Some of both diagonal is not equal ..")
            
              

        case "4":
            print("Thankyou for using an Applcation 😎😎✅✅")
            break
        case _:
             print("ENter the valid choice ")
