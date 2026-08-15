# 46 Check if a substring appears at both the start and end. S = "abcabca", Sub="abca" TRUE

s1 =input("Enter the String ...")
s2 =input("Enter the start and ends String ...")

start =  True if s1.startswith(s2) else False
ends= True if  s1.endswith(s2) else False

print("StartWith ={}\nEndswith ={}".format(start,ends))
