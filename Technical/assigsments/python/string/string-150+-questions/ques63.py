# 63Count frequency of each character. S = "aabcc" a: 2, b: 1, c: 2


st = input("Enter the string ....").lower()

conted=''
for i in st:
    if  i not in conted:
        print(i,":",st.count(i),end=",")
        conted+=i