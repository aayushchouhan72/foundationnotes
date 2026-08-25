# 69 Count how many times 'life' appears in a string. S = "life is life" 2

st = input("Enter the string ...").split()
check=input("Enter the word to check....")
count=0
if check not in st:
     print("Word not in given string ....")
else:  
   for i in st:
        if  i == check:
             count+=1

print("The count of given word in the string is ",count)
