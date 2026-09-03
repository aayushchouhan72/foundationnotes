# 74 Find the longest substring without repeating characters. S = "abcabcbb" "abc"
s = input("Enter the string ...")

maxs = ""

for i in range(len(s)): 
     temp=''
     for j in range(i,len(s)): 
          temp+=s[j]
          if len(set(temp)) ==  len(temp):
                if  len(temp)>len(maxs):
                     maxs=temp

print(maxs)
          
           
