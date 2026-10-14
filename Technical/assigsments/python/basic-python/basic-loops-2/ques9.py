'''
A company promotes employees based on experience, rating, projects completed, and salary.

If experience is at least 5 years, then check rating. If rating is at least 4, then check projects. If projects are at least 3, then check salary. If salary is up to 50000, promote with 30 percent hike; otherwise 20 percent hike. If projects are less than 3, promote with 10 percent hike. If rating is below 4, no promotion. If experience is less than 5, then check if rating is 5. If yes, fast track promotion; otherwise no promotion.

Input:
Experience = 6
Rating = 4
Projects = 2

Output:
Promotion Status = Promoted with 10% hike

'''

exp = int(input("Enter the your experience :- "))
rat = int(input("Enter your rating :- "))
pro = int(input("Enter the number of project complete by you :-"))
sal = int(input("Enter the salary :-"))


if exp>=5:
      if rat>=4:
              if pro>=3:
                      if sal<=50000:
                               print("Promotion Status = Promoted with 30% hike")
                      else:
                           print("Promotion Status = Promoted with 20% hike")
              else :
                    print("Promotion Status = Promoted with 10% hike")
      else:
          print("No Promotion")
else:
    if rat == 5 :
               print("Fast Track Promotion")
    else:
        print("NO  Promotion ..")