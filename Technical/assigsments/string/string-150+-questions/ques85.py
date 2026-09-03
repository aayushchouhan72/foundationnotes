# 85 Convert string into a char array without built-in functions. S = "test" {'t', 'e', 's', 't'}

s= input("Enter the string ...")

final="{"
for i in s:
     final+=f"'{i}', "
final+="}"

print(final)