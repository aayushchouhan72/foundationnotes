# 83 Create a string from a byte array. Byte[] = {72, 101, 108} (ASCII for H, e, l) "Hel"

s =input("Enter an char array by ,").split(",")
final =""
for i in s:
     i=int(i)
     final+=chr(i)
print(final)