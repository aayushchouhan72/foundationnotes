# 49Replace all consonants with '*' (Example suggests replacing non-vowels). S = "apple" "ap*le" (or similar output depending on implementation) 

s=input("Enter the string ...")
final=""
vowel="aeiouAEIOU"
add=""
for i in s:
     if i not in vowel and  i not in add :
          final+=i  
          add+=i   
     else:
          if i not in vowel:
               final+='*'
          else:
               final+=i
            
print(final)