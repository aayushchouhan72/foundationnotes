'''
13. Employee Performance Appraisal System


A company evaluates employees based on performance rating (1–5):

* 5 → 25% salary hike
* 4 → 20% salary hike
* 3 → 10% salary hike
* 2 → 5% salary hike
* 1 → No hike
  If salary is below ₹20000 and rating is 4 or above, an additional ₹2000 bonus is given.

Write a Python program to calculate revised salary.

Input:
Enter salary: 18000
Enter rating: 4

Output:
Revised Salary: ₹23600

'''



rat = int(input("Enter  your rating"))
sal = int(input("Enter your salary"))

if rat==1:
   print("No Hike in salary do some work and come here")
elif rat==2 :
   print(f"Revised salary : {sal+sal*0.05}")
elif rat==3 :
   print(f"Revised salary : {sal+sal*0.10}")
elif rat==4 :
   print(f"Revised salary : {sal+sal*0.20}")
else :
   print(f"Revised salary : {sal+sal*0.25}")