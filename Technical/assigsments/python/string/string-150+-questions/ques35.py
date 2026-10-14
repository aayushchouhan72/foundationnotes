# Find the first palindrome word. S = "this madam is here" "madam"

s= input("Enter the string ...").split()

for i in s:
    if i == i[::-1]:
        print(i)
        break
