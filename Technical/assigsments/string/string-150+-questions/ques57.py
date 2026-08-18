# 57 Merge two strings alternatively. S1 = "ABC", S2 = "def" "AdBeCf"
s1 =input("Enter the First String ...")
s2 =input("Enter the second String ...")
final=""
if len(s1) == len(s2):
     i=0
     j=0
     k=0
     while i<len(s1)+len(s2):
          if i%2 == 0:
               final+=s1[j]
               j+=1
          else:
               final+=s2[k]
               k+=1
          i+=1
else:
     print("Enter the same lists ")

print(final)
