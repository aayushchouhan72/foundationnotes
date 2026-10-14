'''
6.

Product Code Verification System

An e-commerce company wants to verify whether two product codes are rearranged versions of each other.

Conditions:
- Ignore spaces
- Ignore case sensitivity

Input:
Enter first product code: Dormitory
Enter second product code: Dirty Room

Output:
Both Product Codes are Matching
'''

firstst=input("Enter product One_- ").lower()
secondst=input("Enter product second_-").lower()


i=-1
k=0
j=0
while i<len(firstst)-1:
   i+=1
   if firstst[j] == " ":
            j+=1
            continue   
   else:
        if  firstst.count(firstst[j]) == secondst.count(firstst[j]) :
            j+=1
            continue
        else:
            print("both codes are not Matching ...")
            break


else:
    print("both codes are Matching ...")

                