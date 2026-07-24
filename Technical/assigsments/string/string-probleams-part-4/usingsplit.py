'''
2. Reverse Sentence + Reverse Each Word

Secret Military Communication Decoder
A defense organization stores highly confidential messages in encrypted form.
To decode the message:

1. Reverse the entire sentence.
2. Reverse every individual word.
3. Store the final result back into the original string variable.

You must use the split() method.
Input:


Python is powerful


Output:


lufrewop si nohtyP

'''
str = input("Enter the string :- ")
 
str =  str.split(" ")
final=""
for ch in str:
    rev = ch[::-1]
    final+=rev+" "

print(final) 