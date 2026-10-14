# 70 Compare the number of times 'the' and 'is' appear. S = "the cat is on the mat" the: 2, is: 1 (theis)

st = input("Enter the string ...").split()
thiscount=0
iscount=0
for i in st:
    i=i.strip()
    if i ==  'is':
        thiscount+=1
    elif i == 'this':
        iscount+=1
    else:
         pass
         

print(f"is count is {iscount} and this count is {thiscount}")
