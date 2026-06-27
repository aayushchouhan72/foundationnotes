'''
3. Smart Scholarship Allocation System

A scholarship is provided based on marks, family income, and category.

If marks are 85 or above, then check income. If income is less than or equal to 300000, then check category. If category is not general, give Full Scholarship; otherwise give 75% Scholarship. If income is above 300000, give 50% Scholarship.

If marks are between 70 and 84, then check income. If income is less than or equal to 200000, give 50% Scholarship; otherwise give 25% Scholarship.

If marks are below 70, no scholarship is given.

Input:
Marks = 88
Income = 250000
Category = OBC

Output:
Scholarship = Full Scholarship

'''

mark = int(input("Enter your mark :- "))
income  = int(input("Enter your family income :- "))
cat = int(input("Enter your category :- ")).lower()

if mark >= 85:
        if income<=300000:
                  if cat != "gen":
                          print("You will get full scholarship")
                  else: 
                       print("You will get 75% scholarship ")   
        elif income>300000:
             print("You will get 50% scholarchip")
elif mark >=74 and mark<=84:
           if income>2000000:
              print("You will get 50% Scholarship..")
           else:
              print("You will get 25% Scholarship ..")
elif mark>70 :
        print("You are not eligble for scholarship ..")