# 98 Check if the first 'z' is immediately followed by another 'z'. S1 = "zzyy", S2 = "zyzz" S1: True, S2: False

s=input("Enter the string ..").lower()
if s[0] == 'z' and len(s)>=2:
    if s[:2] == 'zz':
        print(True)
    elif len(s) == 1:
        print("Enter valid string to check")
    else:
        print(False)
