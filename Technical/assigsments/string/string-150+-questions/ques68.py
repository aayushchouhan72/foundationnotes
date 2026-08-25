# 68 Count the sum of digits present in a string. S = "a1b2c3" 6 (1+2+3)
sum=0 
st = input("Enter the string ....")
for i in st:
    if '1'<=i<="9":
         sum+=int(i)

print("Sum of digit is ",sum)

