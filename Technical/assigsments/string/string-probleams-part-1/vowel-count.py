'''
1.Vowel Counter in Customer Feedback

 A company wants to analyze customer feedback messages by counting how many vowels are present in the feedback.

Input: Enter feedback message: Hello Customer Service

Output: Total vowels: 8

'''

st = input("Enter your string ...")
count=0

for i in st:
    if i in "aeiou":
         count+=1
      
else:
    print(f"Number of vowel in the string is :- {count}")
