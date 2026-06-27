'''
10. Smart Restaurant Order Processing System

A restaurant offers discounts and benefits based on order amount, customer type, and payment method.

If order amount is at least 2000, then check customer type. If VIP, then check payment method. If online, give free dessert and 20 percent discount; otherwise only free dessert. If not VIP, then check if amount is at least 5000. If yes, give 15 percent discount; otherwise 10 percent discount. If order amount is less than 2000, then check if it is at least 1000. If yes, then if customer is VIP, give 10 percent discount; otherwise 5 percent discount. If below 1000, no offer.

Input:
Order Amount = 2500
Customer Type = VIP
Payment Method = online

Output:
Offer = Free Dessert + 20% Discount

'''

ord =  int(input("Enter order amount >>"))
custyp=  int(input("Enter customer type >>")).lower()
paymode= int(input("Enter the payment mode >>")).lower()

if ord >=2000:      
      if custyp == "vip":
                  if paymode == "online":
                         print("You get free desert and 20 per discount..")
                  else:
                       print("Free desert ..")
      else: 
          if ord >=5000:
                  print("You get flat 15% discount..")
          else:
                  print("you get flat 10% discount..")
          
elif ord<2000 and ord>=1000:
         if custype == "vip":
                print("You get free desert and 10 per discount..")
         else:
              print("you will get 5 discount ..")
else:
     print("YOu will not get offer ..")
            

