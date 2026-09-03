# 77 Find the longest substring that appears at both ends. S = "abracadabra" "abra"

s1 =  input("Enter the frist string ...")
s2 =  input("Enter the second string ...")
i=-1
com=''
while i>=(-len(s1)) and i>=(-len(s1)): 
    if s1[i] == s2[i]:
         com+=s1[i]
    i-=1

print(com)