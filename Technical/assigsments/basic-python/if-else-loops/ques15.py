'''
15. Smart Parking System

A smart parking system charges based on vehicle type and parking duration:

* Bike → ₹10/hour
* Car → ₹20/hour
* Bus → ₹50/hour
  If parking duration exceeds 5 hours, an additional ₹100 penalty is applied.

Write a Python program to calculate total parking fee.

Input:
Enter vehicle type: Car
Enter hours parked: 6

Output:
Total Parking Fee: ₹220

'''

vech =  input("Enter the vehical type :- ").lower
hou = int(input("Enter the number of hours you parked :- "))


if vech == "car" :
    print(f"Total parking fee {hou*20}")
elif vech == "bus":
    print(f"Total parking fee {hou*50}")
elif vec == "bike" :
    print(f"Total parking fee {hou*20}")
else: 
    print("Invalid  vechale type ")
