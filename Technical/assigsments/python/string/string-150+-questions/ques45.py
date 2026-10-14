# 45 Check whether a string starts/ends with another string. S = "apple pie", Prefix = "apple", Suffix = "pie" Start: True, End: True

s1 =input("Enter the  String ...")
prefix =input("Enter the prefix ...")
suffix = input("Enter the suffix ...")

start =  True if s1.startswith(prefix) else False
ends= True if  s1.endswith(suffix) else False

print("StartWith ={}\nEndswith ={}".format(start,ends))