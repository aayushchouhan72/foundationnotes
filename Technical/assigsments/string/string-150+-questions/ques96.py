# 96 Find the second most frequent word. S = "a b a c b" c'
s= input("Enter the string ....").split()
w=set(s)
print()

count=  [s.count(k) for k in w]
m=max(count)
new =  list(filter(lambda x:s.count(x)!=m ,s))
new.sort()
print(new)
print("second max count ",new[-1])