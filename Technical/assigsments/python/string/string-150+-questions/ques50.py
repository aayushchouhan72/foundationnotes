# 50 Remove all digits. S = "a1b2c3" "abc" 
s=input("Enter the string ...")
final=""

for i in s:
    if not i.isdigit():
        final+=i      
print(final)