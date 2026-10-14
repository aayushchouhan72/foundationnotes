# 59Rotate characters right by 3 positions. S = "abcde" "cdeab
st = input("Enter the string ")
final=st[-3:]+st[:-3]
print(final)