# 95 Find the second most frequent character. S = "aabbccdde"

s= input("Enter the string ...")
final=''
for i in s: 
    if i not in final:
        final+=i

s=sorted(final)
print("Second most repeted chracter is ",s[-2])