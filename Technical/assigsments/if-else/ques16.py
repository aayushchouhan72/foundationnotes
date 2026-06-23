'''

6. A movie theatre calculates ticket prices based on age, show time, and day type.
 The system should take age, show time (morning/evening), and day type (weekday/weekend) as input.
If the age is less than 18, then check the show time. If the show time is morning, ticket price is 100; otherwise, ticket price is 150.
 If the age is 18 or above, then check the show time. If the show time is evening,
then check the day type. If it is weekend, ticket price is 300; otherwise, 250.
 If the show time is not evening, ticket price is 200. Display the ticket price.

Input:
Age = 25
Show Time = evening
Day = weekend

Output:
Ticket Price = 300

'''

age = int(input("Enter the age :-"))
timeing = input("Enter show time morning / evening :- ")
daytype= intput("Enter the day type what is it :-")


if age<18:
    if timeing.lower() == "morning":
               print("Ticket price is 100 ")

    else:
        print("Ticket price is 150 ..")

else:
   if timeing.lower() == "evening": 
             if daytype == "weekend"
                     print(" your ticket price is 300")
             else:
                 print("your ticket price is 250")
   else:
       print("your ticket price is 200")
