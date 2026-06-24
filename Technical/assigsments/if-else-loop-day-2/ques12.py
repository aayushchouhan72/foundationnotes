'''
2. Multiplication of Digits*
A puzzle game calculates a score by multiplying all digits of a number together. After calculating the score, the game also checks whether the final score is even or odd to assign a bonus.
Write a program to *find the product of all digits of a number using loops and then check whether the result is even or odd*.

Input: 1234
Output: 24
Even
'''


num = input("Enter number :- ")

product = 1;
for i in num:
    i = int(i)
    product *=i

if product%2 == 0:
    print(f"Your product number is {product} which is even")
else:
     print(f"Your product number is {product} which is odd")
    
      
