# 65 Count palindromic substrings. S = "aaa" 6 (a, a, a, aa, aa, aaa)
st = input("Enter the palindromic string :- ")
count=0
for i in st:
    for j in st:
         if i == j:
            count+=1
             

print(count)







