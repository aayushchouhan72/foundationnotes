# Find the longest word. S = "find the longest word" "longest"

s= input("Enter the string ").split()
longestword=""
length=0
final=""

for i in s:
        if length<len(i):
            longestword=i
            length=len(i)
        final+=i+" "
print(longestword)