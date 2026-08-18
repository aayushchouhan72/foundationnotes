# 64Count frequency of each vowel. S = "programming" o: 1, a: 1 (e, i, u: 0)


st = input("Enter the string ....").lower()

vowels=0
consonants=0
con="aeiou"
vis=""
for i in st:
    if  i in con and i not in vis:
         print(i,":",st.count(i),end=",")
         vis+=i

    