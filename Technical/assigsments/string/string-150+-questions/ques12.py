# Get the Unicode code point of a character at index

st  =  input("Enter the string ...").strip()
index=  int(input("Enter the index ..."))

if 0 <=index<=len(st):
    print(f"Unicode of the charcter at a given index is {ord(st[index])}")
else:
    print("Enter the valid index ...")