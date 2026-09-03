# 73 Find the longest palindromic substring. S = "babad" "bab" (or "aba")
s =input("Enter you String ....")

l = ""
for i in range(len(s)):
     temp=''
     for j in range(i,len(s)):
          temp+=s[j]
          if temp ==  temp[::-1] and len(l)<len(temp):
                  l=temp

print(l)

          
           




        