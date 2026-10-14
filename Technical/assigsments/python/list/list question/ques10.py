nums=[0,1,0]   
i=0
count=0
for val in nums:
     if val == 0:
         nums.pop(i)
         count+=1
     else:
         pass
     i+=1      
print(nums+[0]*count)