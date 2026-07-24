s= input("Enter the string ...")
final=prev=""

for x in s:
      if x.isdigit():
           final+=prev*int(x)
      else:
           prev=x
print(final)