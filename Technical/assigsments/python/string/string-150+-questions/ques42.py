# 42 Check if two strings are equal without using equals(). S1 = "abc", S2 = "abc" TRUE

s1 =input("Enter the First String ...")
s2 =input("Enter the second String ...")

if len(s1) == len(s2):
    issame=True
    i=0
    while i<len(s1):
        if s1[i]!=s2[i]:
            issame=False
            break
        i+=1
    if issame:
        print("Both Strings are Same..")
    else:
        print("Both Strings are not  Same..")
else:
    print("Both string are not Equal ..")