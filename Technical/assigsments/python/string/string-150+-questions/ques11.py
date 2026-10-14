# Get the character at a given index.
st  =  input("Enter the string ...").strip()
index=  int(input("Enter the index ..."))

if 0 <=index<=len(st):
    print(f"Charcter at given index  {index} is {st[index]} ")
else:
    print("Enter the valid index ...")