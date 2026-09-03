# 80 Print list items containing all characters of a given word. List = ["apple", "plea"], Word = "pal" "apple", "plea"

s=  input("Enter the string ...").split()
w = input("Enter the word")



for word in s:
    st=0
    for i in word:
        
        if i in w:
             
             st+=1  
        
    if not st >= len(word):   
         print(word)