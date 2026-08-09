# Remove occurrences of a word. S = "a test b test c", Word = "test", Remove All "a b c"

s= input("Enter the string ").split()
word = input("Enter the word ..")

final=""

for i in s:
     if word != i:
        final+=i+" "
print(final)
