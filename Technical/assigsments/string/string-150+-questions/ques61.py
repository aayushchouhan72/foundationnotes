# 61Count total alphabets, digits, and special characters. S = "a1b!c2" Alphabets: 3, Digits: 2, Special: 1

st = input("Enter the string ....").lower()

albhacount=0
digitcount=0
specialcount=0

for i in st:
    if 'a'<=i<='z':
         albhacount+=1
    elif '0'<=i<='9':
          digitcount+=1
    else:
        specialcount+=1

print(f"Alphabets: {albhacount}, Digits: {digitcount}, Special: {specialcount}")