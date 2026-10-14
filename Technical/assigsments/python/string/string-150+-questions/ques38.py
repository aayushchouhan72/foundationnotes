# 38 Reverse words without split(). S = "a b c" "c b a"
s=input("ENter the string ")
s=s[::-1]
i=0
final=""
while i <len(s):
    word=""
    j=i
    while s[j].:
        print(j)
        word+=s[j]
        i=j
        j+=1
    final+=word
    i+=1 
print(final)