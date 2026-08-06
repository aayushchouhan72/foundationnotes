# a=[1,2,33,33,2,1]
# unique=[]
# for i in a:
#      if i not in unique:
#           unique.append(i)
# print(unique)
# a=[1,2,33,33,2,1]   
# b=[1,2,3,3,5,1]
# l =[]
# for i in a:
#     if i in a and i in b and  i not in l :
#         l.append(i)

# print(l)

# a=[1,2,3,4,5,6]
# i=0
# j=len(a)-1
# while i<=j:
#     temp=a[j]
#     a[j]=a[i]
#     a[i]=temp
#     i+=1
#     j-=1
# print(a)

# a=[1,2,0,0,3,4,0,5,6]

newlist =[]
count=0
for i in [12,4,0,6,0,36]:
     if i != 0:
            newlist.append(i)
     else:
            count +=1 
print(newlist+[0]*count)