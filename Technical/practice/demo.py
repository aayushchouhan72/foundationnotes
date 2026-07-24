'''s= input("Enter the string ...")
final=prev=""

for x in s:
      if x.isdigit():
           final+=prev*int(x)
      else:
           prev=x
print(final)

count=0
for x in s:
      if x.isalpha():
            final+=x+chr(ord(x)+int(s[count+1]))   
      count+=1    
print(final)



s= input("Enter the string ...")
final=""
mid =""
i=0
while i<len(s):
      if s[i] == " ":
            mid=" "
      else:
         mid+=s[i]
      if i != len(s)-1:
             break
      if s[i+1] == " ":
             final+=mid[::-1]
      i=i+1
print(final,i)
		


s= input("Enter the string ...")
final=""
for word in s.split():
         rev=""
         for i in range(len(word)-1,-1,-1): 
                     rev+=word[i]
         print(rev,end=" ")

'''
s= input("Enter the string ...")
for word in s.split():
         rev=""
         for i in range(len(word)-1,-1,-1): 
                     rev+=word[i]
         print(rev,end=" ")


print()
for word in s.split():
         print(word[::-1],end=" ")



        
               
    



	

			