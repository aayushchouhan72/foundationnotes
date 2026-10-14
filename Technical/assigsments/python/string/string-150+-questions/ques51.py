# 51 Extract only digits. S = "a1b2c3" "123"
s=input("Enter the string")
final=""

for i in s:
    if i.isdigit():
        final+=i      
print(final)