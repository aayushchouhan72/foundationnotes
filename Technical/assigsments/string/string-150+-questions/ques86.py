# 86 Print all permutations of a string without repetition. S = "ab" "ab", "ba" 

s= input("Enter the string ...")
i=0
printed=""
while i<len(s):
     j=0
     k=""
     while j<len(s):
          if s[j] not in k:
            k+=s[j]
          j+=1
     if k not in printed:
          print(k,k[::-1])
          printed+=k+k[::-1]
     i+=1
          