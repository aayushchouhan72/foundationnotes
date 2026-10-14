# 44 Check if two strings are anagrams. S1 = "listen", S2 = "silent" TRUE 4

s1 =input("Enter the First String ...")
s2 =input("Enter the second String ...")

visted=""

if len(s1) ==  len(s2):
    for i in s1:
      if i in s1 and i in s2 and s1.count(i) == s2.count(i) :
         continue
      print("They are not anagrams")
      break
    else:
       print("string  is anagram")         
else:
    print("They are not anagrams")
