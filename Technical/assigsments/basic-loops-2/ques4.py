'''
4. E-Learning Course Access System

An online learning platform grants access based on subscription type, course progress, and test score.

If subscription is premium, then check progress. If progress is at least 80, then check test score. If score is at least 70, unlock certificate; otherwise allow retry. If progress is less than 80, ask to complete course. If subscription is basic, then check progress. If progress is at least 50, allow limited access; otherwise lock content. If subscription is neither, deny access.

Input:
Subscription = premium
Progress = 85
Test Score = 65

Output:
Access Status = Retry Test

'''

sus = input("Enter your suscrption type :- ").lower()
progress =  int(input("Enter the progress status :- "))
testscore = int(input("Enter the test score :- "))


if sus == "premium":
     if progress>=80:
          if test>=70:
                   print("This is your certificate..")
          else:
             if progress<=80"
                   print("Please complete the course first ..")
elif sus == "basic":
     if progress >=50:
                print("You have limited access..")
     else:
         print("Locked content")

else:
    print("Deny acess")