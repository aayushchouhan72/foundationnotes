# 4. Reverse a Number
# A security system stores OTP codes in reverse format for encryption to increase data safety. Reversing a number means extracting digits and rebuilding it in reverse order.
# Write a program to *reverse a given integer using loops*.
#while lppo
# Input: 1234
 #Output: 4321
num=int(input("enter any number"))
rev=0
while num>0:
    rev=num%10
    print(rev,end="")
    num=num//10


#forloop
# print(rev)  
#num=int(input("enter any number"))
#rev=0   
#for i in range(len(str(num))):
 #   rev=rev*10+num%10
  #  num=num//10
#print(rev)  