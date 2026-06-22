'''

10. Online Exam System
    System evaluates exam conditions:

* If marks ≥ 40 → Pass
* If attendance ≥ 75 → Eligible for certificate

Input:
Enter marks: 60
Enter attendance: 80

Output:
Pass
Eligible for certificate

'''

mark = int(input("Enter your marks :- "))
if mark >=40:
     if mark >=75:
           print("Eligible for certificate")
     else:
         print("You pass  the exam")

else:
   print("You are unable to clear exam")