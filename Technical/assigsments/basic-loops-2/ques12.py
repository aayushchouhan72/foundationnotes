'''2. Hospital Emergency Priority System

A hospital assigns treatment priority based on age, severity, and insurance.

If severity is critical, then check age. If age is 60 or above, assign Immediate ICU; otherwise assign Emergency Ward.

If severity is moderate, then check insurance. If insured, assign Priority Treatment; otherwise assign General Queue.

If severity is low, then check age. If age is less than 10, assign Pediatric Priority; otherwise assign Wait.

Input:
Age = 65
Severity = critical
Insurance = yes

Output:
Treatment = Immediate ICU
'''

age = int(input("Enter the age :- "))
sev = input("Enter the severity of your case :- ").lower()
ins = input("Enter your insurance status in yes/no").lower()

if sev == "critical":
          if age >=60: 
                 print("You  need ICU Support..")
          else:
                 print("You need to shift in emergency ward..")
elif sev == "moderate":
          if ins == 'yes':
                  print("You will be get priority treatment ..")
          else :
               print("YOu need Genral  Queue ..")
elif sev == 'low':
          if age >10 :
                  print("You will be get pediatric priority..")
          else:
               print("You need to wait..")