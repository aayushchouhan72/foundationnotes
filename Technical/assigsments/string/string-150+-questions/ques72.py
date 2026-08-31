# 72 Print all substrings of length n. S = "abc", n = 2 "ab, bc"

string  = input("Enter the new string ... ")
let =  int(input("Enter the length of char ....."))

for i in range(len(string)):
     temp=''
     for j in range(i,len(string)):
           if temp == let: 
                print(temp)
           print(temp)
           temp+=string[j]
