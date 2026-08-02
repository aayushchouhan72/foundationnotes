'''
4.
Consonant Counter in Student Name Record

A school management system wants to count how many consonants are present in student names.

Input: Enter student name: Ajay Singh Thakur

Output: Total consonants: 11

NOTE:

Ignore case sensitivity (treat A and a same)
Consider only English alphabets for vowel/consonant counting
Vowels: A, E, I, O, U

'''
st = input("Enter your chat Message ::::--->").strip().lower()
print(st)
count=0
ex="aeiou"
vis=""
for i in st:
     if i not in ex and i != " " :
        vis+=i
        count+=1
   
else:
    print(f"Total space :- {count} ")