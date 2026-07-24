'''
8. Weather Monitoring System

A weather monitoring system classifies the weather condition based on temperature:

* Below 0°C → Freezing
* 0°C to 20°C → Cold
* 21°C to 35°C → Warm
* Above 35°C → Hot

Write a Python program to classify the weather.

Input:
Enter temperature: 38

Output:
Weather Condition: Hot

'''

temp = int(input("Enter the temperature of your area :- "))

if temp<0:
   print("* Below 0°C → Freezing")
elif temp>=0 and temp<=20:
   print("0°C to 20°C → Cold")
elif temp>=21 and temp<=35:
   print("21°C to 35°C → Warm")
else:
   print("Above 35°C → Hot")
