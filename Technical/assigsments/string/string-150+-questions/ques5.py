# Compare two strings ignoring case.

st = input("First string :-").strip().lower()
end= input("second string :-").strip().lower()
flag=False
if len(st) != len(end):
       print("Both string are diffrent ")
       flag=True
else:
      i=0
      while i<len(st):

            if st[i] != end[i]:
                   print("Both string are not Equal")
                   flag=True
                   break
            else:
                   flag=False
            i+=1

if not flag:
        print("Both sting are same ")