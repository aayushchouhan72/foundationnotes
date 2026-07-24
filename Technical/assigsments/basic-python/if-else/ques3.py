'''

3. E-Commerce Offer Engine
   An online store provides multiple offers independently:

* If cart value ≥ 500 → Free delivery
* If cart value ≥ 1000 → 10% discount coupon

Input:
Enter cart value: 1200

Output:
Free delivery applied
Discount coupon unlocked
'''


cartprice=  float(input("enter cart price"))

if cartprice>=500:
    if cartprice>=1000:
           print("your eligble for 10% disconunt coupen")
    else:
        print("Your eligble for free delivery")
else:
   print("Thankyou for shopping")
         