'''2. Student Performance Analyzer
   A school wants to evaluate students based on marks.

* If marks ≥ 40 → Pass
* If marks ≥ 75 → Distinction

Input:
Enter marks: 80

Output:
Pass
Distinction

'''


marks = int(input("Enter your marks"))

if marks>=40:
   if marks>=75:
       print("Your pass with distinction")
   else:
       print("You are just Pass")
else:
   print("your are fail")



