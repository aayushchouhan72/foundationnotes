# 88 Rearrange a string so that identical characters are at least d distance apart. S = "aaabc", d = 2 "abaca"

s=  input("Enter the string ...")
n= int(input("Enter the apart distance ..."))
rep='' 
for i in s:
    if i not in rep:
        rep+= i*s.count(i) if s.count(i)>1 else ""
final=''
j=0
while j<len(s):
    if s[j] not in rep:
         final+=s[j]
    j+=1

k=0
l=0
j=0
next=0
res=''
while j<len(s):
     if i == next:
          res+=rep[k]
          k+=1
          next+=n
     else:
           
           print(res)
           res+=final[l]
           l+=1
     j+=1

#  Incomplete




     


