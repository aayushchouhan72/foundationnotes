# 94 Find the smallest window containing all characters of another string. S1 = "ADOBECODEBANC", S2 = "ABC" "BANC"
mains=  input("Enter the string ...")
checks= input("Enter the string ...")
windowlen=len(checks)
i=0
flag=False
while windowlen != len(mains): 
      s = mains[i:i+windowlen]
      for j in checks:
            print("hii")
            if j  not in s:
                  break
      else:
            print("smallest window is ",s)
            flag=True
      if flag:
             break
      if i+1 ==  len(mains):
             windowlen+=1
      i+=1
      # Incompleat  