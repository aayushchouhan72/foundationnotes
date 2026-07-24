'''
4. Gym Membership Eligibility Checker
   A gym checks multiple conditions:

* If age ≥ 18 → Allowed for gym
* If BMI > 25 → Suggest weight loss program

Input:
Enter age: 25
Enter BMI: 27

Output:
Gym access granted
Enroll in weight loss program
'''


age = int(input("Enter your age :- "))
bmi = float(input("Enter  your BMI :- "))

if age>=18:
   if bmi>27:
      print(" we suggest you to join weight lose program")
   else:
      print("Gym Access is grandted to you")
else:
   print("your not elligble to join gym")