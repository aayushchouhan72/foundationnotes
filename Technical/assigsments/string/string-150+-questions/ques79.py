# 79 Divide a string into n equal parts. S = "abcdef", n = 3 "ab", "cd", "ef"

s= input("Enter the number ...")
n= int(input("Enter the n number of parts ..."))
div=int(len(s)/n)
i=0

while i<len(s):
    k=i+div
    print(s[i:k])
    i+=div

     