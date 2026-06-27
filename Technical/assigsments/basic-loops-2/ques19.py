'''
9. Smart Loan Eligibility System

A bank approves loans based on salary, age, credit score, and EMI.

If salary is 40000 or above, then check age. If age is between 21 and 60, then check credit score. If credit score is 750 or above, then check EMI. If EMI is less than or equal to 40% of salary, approve at 8%; otherwise approve at 10%. If credit score is below 750, then check if it is at least 650. If yes, approve at 12%; otherwise reject.

If salary is below 40000, then check if salary is at least 25000 and credit score is at least 700. If yes, approve at 13%; otherwise reject.

Input:
Salary = 50000
Age = 30
Credit Score = 760
EMI = 18000

Output:
Loan Status = Approved at 8%


'''

sal = int(input("Enter your salary :- "))
age = int(input("Enter your age :- "))
cs = int(input("ENter your credit score :- "))
emi = int(input("Enter the EMI Amount you went to pay mounthly :- "))


if sal >= 40000 :
      if age>=21 and age<=60:
                  if cs >= 750 :
                        if emi<(sal*0.40)
                              print("Your loan is approved at 8% ... ")
                        else: 
                            print("Your loan is approved at 10% ..")

                  elif cs < 750:
                          if cs >=650 :
                                 print("Your loan is approved at 12% ..")
                          else:
                              print("Loan is rejected ..")
else:
    if sal >=25000 and cs>=700:
               print("your loan is approved at 13% ..")
    else: 
        print("your loan appplication is rejected ..")