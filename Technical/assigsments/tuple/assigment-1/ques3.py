# .

# MATRIX PERFORMANCE EVALUATION SYSTEM

# A company records the monthly performance scores of employees in a matrix format. Each row represents an employee and each column represents a month.

# The HR department wants a menu-driven application to analyze employee performance.

# Menu
# 1. Find Employee with Highest Total Score
# 2. Find Month with Lowest Average Score
# 3. Display Employee-wise Maximum Score
# 4. Exit
# Requirements
# Choice 1 – Find Employee with Highest Total Score
# Calculate the sum of each row.
# Display the employee number having the highest total score.
# Choice 2 – Find Month with Lowest Average Score
# Calculate the average of each column.
# Display the month having the lowest average score.
# Choice 3 – Display Employee-wise Maximum Score
# Find and display the maximum value present in each row.
# Sample Input
# 10 20 30
# 40 50 60
# 25 35 45
# Output
# Employee 2 has Highest Total Score = 150

# Month 1 Average = 25
# Month 2 Average = 35
# Month 3 Average = 45

# Employee 1 Max Score = 30
# Employee 2 Max Score = 60
# Employee 3 Max Score = 45


while True:
    print("Menu")
    print("\n1.Find Employee with Highest Total Score\n2.Find Month with Lowest Average Score\n3. Display Employee-wise Maximum Score\n4. Exit")
    choice=input("Enter the choice >.")
    match choice:
        case "1":
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
             maxlist=[]

             for row in mat1:
                  max=0
                  for ele in row:
                       if ele>max:
                            max=ele
                  maxlist.append(max)
             row=1
             for i in maxlist:
                  print(f"Month {row} Average = {i}")
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
            min=9999999999999999999999999999999999999999999
            rownum=0
            v=0
            for row in mat1:
                  sum=0
                  for ele in row:
                      sum+=ele
                  if sum/len(row)<min:
                       min = sum/len(row)
                       v=rownum
                  rownum+=1
                              
            row=1
            print(v+1 , "This row is with minimum average value",min)
            
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
              for row in mat1:
                     max=0
                     for ele in row:
                          if ele>max:
                               max=ele
                     maxlist.append(max)
              row=1
              for i in maxlist:
                        print(f"Month {row} Average = {i}")
        case "4":
            print("Thankyou for using an Applcation 😎😎✅✅")
            break
        case _:
             print("ENter the valid choice ")

