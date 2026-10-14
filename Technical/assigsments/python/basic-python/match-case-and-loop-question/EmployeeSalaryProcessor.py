'''
2.
 Employee Salary Processor

Scenario:
You are developing an Employee Salary Processing System for a company’s HR department. The system is used to manage and calculate employee salary details such as allowances, tax deductions, and final payable salary.

The HR staff may not always follow the correct sequence while using the system. For example, they might try to calculate net salary or tax before entering the basic salary. Your program must handle such situations properly.

👉 Important Condition:
If the Basic Salary is not entered, the system should display:
"Please enter basic salary first"
and should not perform any further calculations.

The system should be menu-driven and must continue running until the user selects Exit. All operations should be handled using match-case.

Menu Options:
1 → Enter Basic Salary
2 → Calculate HRA (20%) and DA (10%)
3 → Calculate Net Salary
4 → Tax Deduction

* Salary > 50000 → 10% tax
* Otherwise → 5% tax
  5 → Display Salary Slip
  6 → Exit

---

Sample Run 1:
Input:
Enter your choice: 3

Output:
Please enter basic salary first

---

Sample Run 2:
Input:
Enter your choice: 1
Enter Basic Salary: 40000

Output:
Basic Salary recorded successfully

---

Sample Run 3:
Input:
Enter your choice: 2

Output:
HRA: 8000
DA: 4000

---

Sample Run 4:
Input:
Enter your choice: 3

Output:
Net Salary (before tax): 52000

---

Sample Run 5:
Input:
Enter your choice: 4

Output:
Tax Deduction: 5200

---

Sample Run 6:
Input:
Enter your choice: 5

Output:
----- Salary Slip -----
Basic Salary: 40000
HRA: 8000
DA: 4000
Net Salary: 52000
Tax: 5200
Final Salary: 46800

---

Sample Run 7 (Invalid Choice):
Input:
Enter your choice: 9

Output:
Invalid choice. Please try again.

---

Sample Run 8 (Exit):
Input:
Enter your choice: 6

Output:
Exiting program... Thank you!

3.
'''

'''
Menu Options:
1 → Enter Basic Salary
2 → Calculate HRA (20%) and DA (10%)
3 → Calculate Net Salary
4 → Tax Deduction

* Salary > 50000 → 10% tax
* Otherwise → 5% tax
  5 → Display Salary Slip
  6 → Exit
'''

salary=0
tax=0
hra=0
da=0
net_sal=0
final=net_sal-tax

while True:
     print("1 → Enter Basic Salary")
     print("2 → Calculate HRA and DA ")
     print("3 → Calculate Net Salary")
     print("4 → Tax Deduction")
     print("5 → Display Salary Slip")
     print("6 → Exit")      
     choice = int(input("Enter your Choice :- "))
     match choice:
           case 1:
               if salary==0:
                   salary = int(input("\nEnter your Basic salary :- "))
                   print('Basic Salary recorded successfully')
               else:
                   print("Enter the basic salary first :- ")
          
           case 2:
                 if salary !=0:
                    hra=salary*0.20
                    da=salary*0.10
                    print(f"HRA={hra}\nDA={da}")
                 else:
                   print("Enter the basic salary first :- ")   
           case 3:
               if salary !=0 and da>0 and hra>0:
                  net_sal =salary+da+hra
                  print(f"Employee Net Salary is {net_sal}")
               else:
                   print("Calculate HRA and DA First  ")
                  
           case 4:
               if salary !=0 and da>0 and hra>0 and net_sal>0:
                    if net_sal >50000:
                         tax=net_sal*0.90
                         print(f"Tax={tax}")
                         final=net_sal-tax
                    else:
                        tax=net_sal*0.05
                        print(f"Tax={tax}") 
                        final=net_sal-tax        
               else:
                   print("Calculate Net Salary first ")
                 
           case 5:
                 if salary !=0 and da>0 and hra>0 and net_sal>0 and tax>0:
                      print("=====Employee Salary Reciept=====")
                      print(f"\n\tBasic Salary :{salary}\n\tDA :{da}\n\tHRA :{hra}\n\tTax :{tax}\n\tNet Salary :{net_sal}\n\tFinal Salary :{final}")
                 else:
                   print("You need to calculate all the Valuse..")
           case 6:
                 print("Closeing application ...")
                 print("Thankyou 👍👍👍")
                 break
           case __:
                 print("You enter the wrong option or invalid option..")
           
     
     































