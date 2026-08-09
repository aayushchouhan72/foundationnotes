# 36 Reverse order of words. S = "one two three" "three two one"

s= input("Enter the string ...").split()
s=s[::-1]
final=""
for i in s:
    final+=" "+i

print(final)
