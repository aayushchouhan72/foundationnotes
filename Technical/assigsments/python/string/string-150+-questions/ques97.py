# 97 Check if two given strings appear at the end of each other (ignoring case). S1 = "abc", S2 = "Xabc" TRUE

s1 =  input("Enter the string first ...")
s2 =  input("Enter the string second ...")

def firststrcheck(first,second):
     if len(first)>=len(second):
          return first.endswith(second)
     else:
          return second.endswith(first)
    



if firststrcheck(s1,s2):
     print(True)
else:
    print(False)
