# 84 Print ASCII value of each character. S = "A" A: 65

s= input("Enter the string ...")

for i in s:
    print(f"{i}:{ord(i)}")