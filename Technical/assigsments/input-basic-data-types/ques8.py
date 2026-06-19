print("Enter the below details to calculate simple intrest\n" )
prin = int(input("Enter the principle amount :-"))
rate=  int(input("Enter the rate at which you borrow :-"))
time= int(input("Enter the time in years :-"))

si= (prin*rate*time)/100

print(f"principle={prin}\nRate={rate}\nTime={time}\nSimple Intrest ={si}")
