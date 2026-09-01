'''
1.
STUDENT RESULT MANAGEMENT SYSTEM

Scenario:

A college examination department wants to automate the process of generating student results. The staff should be able to
enter student details, calculate marks, determine grades, and display a complete report card using a menu-driven application.

Develop a Python program using multiple user-defined functions and a menu-driven approach to perform the following operations.

MENU

1. Add Student Details
2. Calculate Total Marks
3. Calculate Percentage
4. Find Grade
5. Display Complete Result
6. Find Highest Subject Mark
7. Find Lowest Subject Mark
8. Exit

Functional Requirements

1. Add Student Details

   * Student Name
   * Roll Number
   * Marks of 5 Subjects

2. Calculate Total Marks

3. Calculate Percentage

4. Find Grade

5. Display Complete Result

6. Find Highest Subject Mark

7. Find Lowest Subject Mark

8. Exit

Grade Criteria

Percentage        Grade

90 - 100          A+
80 - 89           A
70 - 79           B
60 - 69           C
50 - 59           D
Below 50          Fail

Constraints

* Marks should be between 0 and 100.
* Display an appropriate message for invalid marks.
* The program should continue until the user chooses Exit.

Sample Input / Output

*** STUDENT RESULT MANAGEMENT ***

1. Add Student Details
2. Calculate Total Marks
3. Calculate Percentage
4. Find Grade
5. Display Result
6. Find Highest Mark
7. Find Lowest Mark
8. Exit

Enter Choice : 1

Enter Student Name : Ajay
Enter Roll Number : 101

Enter Mark 1 : 78
Enter Mark 2 : 85
Enter Mark 3 : 92
Enter Mark 4 : 88
Enter Mark 5 : 77

Student details added successfully.

Enter Choice : 2

Total Marks = 420

Enter Choice : 3

Percentage = 84.0

Enter Choice : 4

Grade = A

Enter Choice : 6

Highest Mark = 92

Enter Choice : 7

Lowest Mark = 77

Enter Choice : 5

----------- RESULT CARD -----------

Name        : Ajay
Roll Number : 101

Marks
Subject 1 : 78
Subject 2 : 85
Subject 3 : 92
Subject 4 : 88
Subject 5 : 77

Total Marks : 420
Percentage  : 84.0
Grade       : A
Highest Mark: 92
Lowest Mark : 77

Enter Choice : 8

Thank You. Program Terminated.

Important Instructions

1. The solution must be developed using multiple user-defined functions.
2. Use appropriate parameters wherever data needs to be passed between functions.
3. Use return statements wherever a function needs to send a result back to the caller.
4. Avoid using unnecessary global variables.
5. Implement the application using a menu-driven approach.
6. Perform proper input validation.
7. Write meaningful function names and maintain proper code readability.


'''

student=[]
def addstudent(name,roll,marks):
          student.append([name,roll,marks])
          print(student)
def calculatemarks():
          return sum(student[0][2])

def calculatepercentage():
          per =  (sum(student[0][2])/5)
          return per
def grade():
      x=calculatepercentage()
      if x>90:
             return "A+"
      elif x>80:
             return "A"
      elif x>70:
             return "B"
      elif x>60:
             return "C"
      elif x>50:
            return "D"
      else:
            return "FAIL"
      
      
def  displayresult():
        print("Name        :",student[0][0])
        print("Roll Number :",student[0][1])

        print("Marks")
        count=1
        for i in student[0][2]:
             print(f"Subject {count} :{i}")

        print(f"Total Marks   :{calculatemarks()}")
        print(f"Percentage    :{calculatepercentage()}")
        print(f"Grade         :{grade()}")
        print(f"Highest Marks :{maxmarks()}")
        print(f"Lowest Marks  :{minmarks()}")

def maxmarks():
       return max(student[0][2])

def minmarks():
       return min(student[0][2])           
while True:
  print('''
1. Add Student Details\n
2. Calculate Total Marks\n
3. Calculate Percentage\n
4. Find Grade\n
5. Display Complete Result\n
6. Find Highest Subject Mark\n
7. Find Lowest Subject Mark\n
8. Exit\n
''')
  choice =  input("Enter the your choice ...")
  match choice:
     case "1":
           print("Add Student Details")
           name =  input("Enter the student name ...")
           roll =  input("Enter the roll number ...")
           marks =[]
           i=0
           while i<5:
                mark =int(input("Enter the marks of "))
                if 0 <= mark <= 100:
                      marks.append(mark)
                else:
                     print("Enter the valid marks")
                     i -= 1
                i+=1
           addstudent(name,roll,marks)
     case "2":
           if student:
               print("Sum is  ", calculatemarks())
           else:
              print("Enter the student details first")
           
     case "3":
          if student:
               print("Percentage is  ", calculatepercentage())
          else:
              print("Enter the student details first")
     case "4":
          r= grade()
          print("Grade is ",r)
     case "5":
           displayresult()
     case "6":
           ma = maxmarks()
           print("maximum marks ",ma)
     case "7":
          print("Minmum marks",minmarks())
     case "8":
           print("Thankyou for using an application")
           break
     case _:
           print("Enter the Invalid input")
