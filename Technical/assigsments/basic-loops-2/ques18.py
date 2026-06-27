'''
8. E-Commerce Dynamic Pricing System

An e-commerce system gives discount based on demand, stock, user type, and festival.

If demand is 80 or above, then check stock. If stock is less than 50, then check user type. If user is premium, then check festival. If festival is yes, give 20% discount; otherwise 10%. If user is not premium, no discount. If stock is 50 or more, give 5% discount.

If demand is between 40 and 79, then check festival. If yes, give 10% discount; otherwise no discount.

If demand is below 40, then check stock. If stock is greater than 200, give 15% discount; otherwise no discount.

Input:
Demand = 85
Stock = 40
User Type = premium
Festival = yes

Output:
Discount = 20%
'''
dem = int(input("Enter the demand.."))
sto = int(input("Enter the Stock status .."))
ustyp = input("Enter the user type ..").lower()
fes = input("Enter the festival or not in yes / no ..").lower()

if dem >=80:
     if sto <50 :
          if ustyp == "premium":
                    if fes == "yes":
                         print("20%")
                    else:
                         print("10%")
          else:
              print("YOu will not get discount ..")
     elif sto>=50:
              print("You will get 5% dicount") 
elif dem>40 and dem<=79:
                if fes == "yes":
                     print("10%")
                else:
                   print("You will get no discount")
else:
     if sto >200:
             print("You will get 15% discount..")
     else:
         print("You will not get any kind of discount ..")