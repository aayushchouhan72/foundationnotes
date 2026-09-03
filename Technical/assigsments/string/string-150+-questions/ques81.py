# 81 Generate a hash code or UUID. S = "test" Hash: 3556498 (Example hash code)

s=input("Enter the number ...")
prev=0
for i in s:
     ordval=  ord(i)
     prev=prev*31+ordval

print(prev)