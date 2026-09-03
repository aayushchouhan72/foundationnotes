# 87 Print all permutations of a string with repetition. S = "aab" "aab", "aba", "baa"

s= input("Enter the string ...")

i=0
while i<len(s):
     final =  s[i:]+s[:i]
     print(final)
     i+=1
           