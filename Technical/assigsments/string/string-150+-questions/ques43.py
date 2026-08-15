# 43 Check if two strings are rotations of each other. S1 = "abcde", S2 = "cdeab" TRUE

s1 =input("Enter the First String ...")
s2 =input("Enter the second String ...")

counted=""

if len(s1) == len(s2):
    i=0
    while i <len(s1):
        if s1[i] not in counted:
            count1 = s1.count(s1[i])
            count2 = s2.count(s1[i])
            if count1 != count2:
                print("Not  rotation")
                break
            counted+=s1[i]
        i+=1
    else:
        print("String is rotaion")  
      
else:
    print(" Not a Rotaion  ..")
