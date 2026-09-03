# 91 Check if two strings are interleaving of another string. S1 = "aab", S2 = "axy", S3 = "aaxaby" TRUE

s1 =  input("Enter the first string ...")
s2 = input("Enter the second string ...")
s3 = input("Enter the third string ...")

def checkstring(s1,s2,s3):
    s1preindex=-1
    for i in s1:
            if s1preindex<=s3.index(i):     
                  s1preindex =s3.index(i)
            else:
                 return False
    s2preindex=-1
    for i in s2: 
            if s2preindex<=s3.index(i):
                  s2preindex =s3.index(i)
            else:
                 return False
    return True

print(checkstring(s1,s2,s3))

              


