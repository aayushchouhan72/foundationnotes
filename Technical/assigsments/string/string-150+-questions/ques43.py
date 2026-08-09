# 43 Check if two strings are rotations of each other. S1 = "abcde", S2 = "cdeab" TRUE

s1 =input("Enter the First String ...")
s2 =input("Enter the second String ...")

vistedin1=""
vistedin2=""

data1=""
data2=""

if len(s1) == len(s2):
    i=0
    while i<len(s1) and i<len(s2):
        if s1[i] not in vistedin1 or s2[i] not in vistedin2:
            data1+=f"{s1[i]},{s1.count(s1[i])}|"
            data2+=f"{s2[i]},{s2.count(s2[i])}|"
            vistedin1+=s1[i]
            vistedin2+=s2[i]
        i+=1
    d1=data1.split("|")
    d2=data2.split("|")
    i=0
    while i<len(d1) or i<len(d2):
        
else:
    print(" Not a Rotaion  ..")
