# 31 Remove duplicate words. S = "the cat and the dog" "the cat and dog"

s= input("Enter the string ").split()

final=""

for i in s:
     if  i not in  final:
        final+=i+" "
print(final)
