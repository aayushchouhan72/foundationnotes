# Create a string from a character array. Char[] = {'h', 'i'} "hi"

s =input("Enter an char array by ,").split(",")
final =""
for i in s:
     final+=i
print(final)