# 93 Match strings with wildcard characters ($\*$, ?). Pattern = "a?c", Text = "axcde" TRUE
pattern =  input("Enter the pattern ....")
text =  input("Enter the text ....")
checker=''
for i in pattern:
     if 65<=ord(i)<=92 or 97<=ord(i)<=122:
            checker+=i

def stringcheck(checkst,txt):
       i=0
       index=0
       while i<len(checkst):
             l=txt[index:]
             print(l)
             if checkst[i] in  l:
                   index=text.index(text[i])
             else:
                 return False
             i+=1
       return True


print(stringcheck(checker,text))