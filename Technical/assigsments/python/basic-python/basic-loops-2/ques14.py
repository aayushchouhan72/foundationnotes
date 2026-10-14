'''
4. Airline Ticket Pricing Engine

An airline calculates ticket price based on class, distance, and booking time.

If class is business, then check distance. If distance is greater than 1000, price is 8000; otherwise 5000.

If class is economy, then check distance. If distance is greater than 1000, then check booking time. If booking is early, price is 4000; otherwise 5000. If distance is less than or equal to 1000, price is 2500.

Input:
Class = economy
Distance = 1200
Booking = early

Output:
Ticket Price = 4000

'''

class = input("Enter the travel class :- ").lower()
dis = int(input("Enter the distance in KM :- "))
book = input("Enter the booking type :-").lower()

if class == "economy":
      if dis >1000:
            if book == "early":
                        print("Ticket price is 4000 ..")
            else: 
                print("ticket price is 5000")
     else:
         print("ticket price is 2500")