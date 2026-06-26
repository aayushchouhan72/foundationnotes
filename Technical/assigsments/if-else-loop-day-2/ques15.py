f8:e1:50:94:e2:1f 50:5a:65:4f:94:df
# 14.Floor Movement System (Elevator)
# An elevator system takes the current floor and destination floor as input.

# If current floor < destination → move upward and display floors
# If current floor > destination → move downward and display floors
# If both are same → display "Already on the same floor"

# Write a program using if-elif-else and loops to simulate elevator movement.

# Input: 1, 5
# Output: 1 → 2 → 3 → 4 → 5

# Input: 7, 3
# Output: 7 → 6 → 5 → 4 → 3

# Input: 4, 4
# Output: Already on the same floor   
 current=int(input("Enter current floor: "))
 destination=int(input("Enter destination floor: "))

 if current<destination:
     while current<=destination:
         print(current,end=" ")
         current=current+1

 elif current>destination:
     while current>=destination:
         print(current,end=" ")
         current=current-1

 else:
     print("Already on the same floor")
if current==dest:
    print("right now you are at correct floor ..")
elif current<dest:
    for i in range(current,dest + 1,1):
         print(i,end="-->")
else:
    for i in range(current,dest-1,-1):
            print(i,end="-->")  
