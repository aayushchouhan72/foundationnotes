#  89. Remove 'b' and 'ac' from a string. S = "abacbb" "c"

s = input("Enter the string ...").lower()
i=0
final=''
while i<len(s):
     if not (s[i] == 'b' or  s[i:i+2] == 'ac' or s[i] == 'a'):
           final+=s[i]
     i+=1

print(final)