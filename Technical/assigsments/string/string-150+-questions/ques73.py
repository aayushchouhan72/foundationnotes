# 73 Find the longest palindromic substring. S = "babad" "bab" (or "aba")
s =input("Enter you String ....")
final=''
for i in range(len(s)):
    temp = ""
    for j in range(i, len(s)):
        temp += s[j]
    # print(temp,temp[::-1])
    if temp == temp[::-1]:
        print(temp)



        