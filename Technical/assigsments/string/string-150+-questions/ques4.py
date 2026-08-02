# 4. Compare two strings (case-sensitive).

st = input("First string :-").strip()
end= input("second string :-").strip()
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