# Get the Unicode code point before index.
st  =  input("Enter the string ...").strip()
index=  int(input("Enter the index ..."))

if 1 <=index<=len(st)-1:
    print(f"Unicode of the charcter at a given index is {ord(st[index-1])}")
else:
    print("Enter the valid index ...")
