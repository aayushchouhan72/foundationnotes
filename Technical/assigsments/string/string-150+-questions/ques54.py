# 54 Replace duplicate chars with '$'. S = "hello" "he$lo" 5

s= input("Enter the string ")[::-1]
final =  ""
appended=""

for  i in s:
    if i in appended:
        final+="$"
    else:
         final+=i
         appended+=i
final=final[::-1]
print(final)