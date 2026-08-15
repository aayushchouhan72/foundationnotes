# 53Remove punctuation. S = "Hello, world!" "Hello world"

#  puncuation ascii range 
# 33–47   → ! " # $ % & ' ( ) * + , - . /
# 58–64   → : ; < = > ? @
# 91–96   → [ \ ] ^ _ `
# 123–126 → { | } ~

s= input("Enter the string ")
final =  ""

for  i in s:
    if not (33<=ord(i)<=46 or 58<=ord(i)<=64 or 91<=ord(i)<=96 or 123<=ord(i)<=126):
        final+=i

print(final)