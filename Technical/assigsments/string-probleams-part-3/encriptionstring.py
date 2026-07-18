'''
4.  Instant Messaging Word Encryption System

A messaging application wants to temporarily encrypt messages during
transmission. The encryption rule is to reverse every word individually
while keeping the word positions unchanged.

Input: Enter message: java is powerful

Output: Encrypted Message: avaj si lufrewop

'''
mess = input("Enter Your message ...")

mess+=" "
mid=""
final=""
flag=True
for ch in mess:
    if ch == " ":
         if flag:
              rev = mid[::-1]
              final+=rev+" "
              mid=""
              flag=False
              
    else:
        mid+=ch
        flag=True

print("Rev String is :- s",final)