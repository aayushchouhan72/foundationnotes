11. Railway Ticket Fare System


A railway system calculates ticket fare based on distance and travel class:

* Distance ≤100 km:
  Sleeper → ₹100, AC → ₹200
* Distance 101–500 km:
  Sleeper → ₹300, AC → ₹600
* Distance >500 km:
  Sleeper → ₹500, AC → ₹1000

Write a Python program to calculate ticket fare.

Input:
Enter distance: 350
Enter class: AC

Output:
Total Fare: ₹600


dis = int(input("Enter distance you went to travel in KM..."))
class =  input("Enter the your class :- ").lower()
 


if dis<=100 :
     if class == "ac":
        print("Fair of AC Class is -> 200")
     else : 
        print("Fair of Sleeper Class is -> 100")
         
elif dis>=101 and dis<=500:
     if class == "ac":
        print("Fair of AC Class is -> 300")
     else : 
        print("Fair of Sleeper Class is -> 600")

else:
    if class == "ac":
        print("Fair of AC Class is -> 500")
    else : 
        print("Fair of Sleeper Class is -> 1000")
         



