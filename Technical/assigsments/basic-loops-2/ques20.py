'''
10. Military Recruitment Fitness System

Selection is based on age, BMI, running time, and medical condition.

If age is between 18 and 25, then check BMI. If BMI is between 18 and 25, then check running time. If running time is less than or equal to 15 minutes, then check medical. If medical is fit, select; otherwise medical reject. If running time is more than 15, physical fail. If BMI is not in range, BMI fail.

If age is between 26 and 30, then check running time and medical. If running time is less than or equal to 14 and medical is fit, conditional selection; otherwise reject.

If age is above 30 or below 18, not eligible.

Input:
Age = 23
BMI = 22
Running Time = 14
Medical = fit

Output:
Selection Status = Selected

'''
bmi = int(input("Input enter your bmi :- "))
age = int(input("Enter your age :- "))
rtime =  int(input("Enter your running time :- "))
med = input("Enter the medical ..").lower()

if age >=18 and age<=25:
             if bmi>=18 and bmi<=25:
                       if rtime >=15:
                              if med == 'fit':
                                     print("YOu are selected ..")
                              else:
                                  print("You are rejected ..") 
                       elif rtime>15:
                                 print("You fail Physical .. ")
                     
             else:
                 print("You fail in BMI")
elif age>=26 and age<=30 :
                  if rtime>=14 and medical == 'fit'   
                       print("Conditional selected ..")
elif age>30 or age<18:
              print("Yout not elgible for selection ..")     