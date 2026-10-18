# num1="123"
# num2="456"
# lis={
#             "1":1,
#             "2":2,
#             "3":3,
#             "4":4,
#             "5":5,
#             "6":6,
#             "7":7,
#             "8":8,
#             "9":9
#         }
# d1=0

# # num1=num1[::-1]
# # print(num1)
# for i in num1:
#      d1=d1*10+lis[i]
#      print(d1)
# d2=0

# for i in num2:
#      d2=d2*10+lis[i]
#      print(d2)
# res= d1*d2
# print(d1,d2)
# print(res)
s='0-1'
s = s.strip()
n=''
for i in range(len(s)):
    if (s[i].isdigit() or s[i]=="-") and s[i] != "0" :
        j=i
        while j<len(s) and (s[j].isdigit() or s[j] == "-"):
            n+=s[j]
            j+=1
print(n[:-1])



