'''
5. Smart Exam Evaluation System

A student’s result depends on marks, attendance, and internal score.

If marks are 40 or above, then check attendance. If attendance is 75 or above, then check internal marks. If internal is 20 or above, result is Pass; otherwise Grace Pass. If attendance is below 75, result is Detained.

If marks are below 40, then check if marks are at least 35 and internal is at least 25. If yes, result is Reappear; otherwise Fail.

Input:
Marks = 38
Attendance = 80
Internal = 26

Output:
Result = Reappear

'''

mark = int(input("Enter the marks :- "))
att = int(input("Enter the attendance percent "))
int = int(input("Enter the internal marks "))


if mark >=40 :
           if att>=75:
                  if int>=20:
                        print("you are pass in exam")
                  else:
                       print("pass with grace")
           else :
                print("result is detained.")
else:
     if marks>=35 and int>=25:
                print("You need to reappear in exam ")

     else:
         print("You fail in exam..")              