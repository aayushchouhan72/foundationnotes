'''
6. Weather Monitoring System
   A system checks weather conditions:

* If temperature ≥ 30 → Hot day
* If humidity ≥ 70 → High humidity alert

Input:
Enter temperature: 32
Enter humidity: 75

Output:
Hot day
High humidity alert'''


temp = int(input("Enter the temperature :-"))
humi =  int(input("Enter the humidity in % :-"))


if temp>=30:
      if humi >=70:
           print("Today is hot day and high humidity")
      else:
           print("Today is hot day but has low humidity")
else:
   print("preatiee cool weather for best for fun")



