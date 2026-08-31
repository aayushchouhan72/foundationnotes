# 71 Print all substrings. S = "abc" "a, b, c, ab, bc, abc"

s =input("Enter you String ....")
final=''
for i in range(len(s)):
    temp = ""
    for j in range(i, len(s)):
        temp += s[j]
        final+=temp+" "
print(final)
        