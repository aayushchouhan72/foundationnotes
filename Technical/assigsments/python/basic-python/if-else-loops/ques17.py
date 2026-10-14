'''
2. University Admission System

A university decides admission based on marks, entrance score, and category of the student.

If marks are 70 or above, then check entrance score. If entrance score is 80 or above, then check category. If general, admit; otherwise admit with scholarship. If entrance score is less than 80, then check if marks are 85 or above. If yes, admit under management quota; otherwise reject. If marks are below 70, then check if category is not general and marks are at least 60. If yes, check entrance score. If it is 70 or above, waitlist; otherwise reject. If none of these conditions match, reject.

Input:
Marks = 72
Entrance Score = 85
Category = general

Output:
Admission Status = Admitted


'''

mark = int(input("Enter your marks :- "))
score = int(input("Enter your entrance score :- "))
category = input("Enter your category type like GEN ,OBC,SC").lower


if mark > 70 :
     if score >80: 
        if category = 'gen':
             print("Your are selected for admission")
        else:
             print("yout are admitted with scholarship")
     else:
         if mark>=85 :
             print("Your admission through mangment quota..")
         else:
             print(" your profile was rejected ..")
else: 
   if category != "gen" and 60<=mark:
          if score >=70: 
              print("You are in waiting list ...")
          else:
             print(" your profile was rejected ..") 
   else:
       print(" your profile was rejected ..")
             

