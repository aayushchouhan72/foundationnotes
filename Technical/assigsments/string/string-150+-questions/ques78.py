# 78 Find the longest mirror-image substring at both ends. S = "aabccbaa" "aab"
s= input("ENter the string ...")
revs =s[::-1]
i=0
maxlen=len(s)/2-1
com=''
while maxlen>i and i<len(s):
    if s[i] == revs[i]:
       com+=s[i]
    i+=1



if not com :
     print("String not contain an mirror image ...")
else:
     print(com)

     