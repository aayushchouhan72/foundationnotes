# 32 Count frequency of each word. S = "apple banana apple" apple: 2, banana: 1

s= input("Enter the string ").split()

final=""

for i in s:
    if i not in final:
        final+=f"{i}:{s.count(i)},"
print(final)