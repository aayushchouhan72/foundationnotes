'''
7. Salary Benefits System
   A company provides benefits:

* If salary ≥ 30000 → Eligible for PF
* If salary ≥ 50000 → Eligible for bonus

Input:
Enter salary: 55000

Output:
PF applicable
Bonus applicable

'''

salary = float(input("Enter the mounthly salary :- "))


if salary>=30000:
     if salary >=50000:
         print("You are eligible for the Bonus")
     else:
         print("You are Eligible for the PF")

else:
   print("You need to hard work to get increment in salary")