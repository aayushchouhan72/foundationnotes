# 37 Reverse each word. S = "cat dog" "tac god"

s=input("Enter in string ...").split()
final=""

for i in s:
    final+=i[::-1]+" "

print(final)