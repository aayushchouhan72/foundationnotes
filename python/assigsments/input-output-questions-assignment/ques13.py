prin,rate,dur =  map( int ,input("Enter the principle amount rate and duration").split())

amount =  prin*(1+(rate/100))**dur

print(f"Your compound intrest is {amount}")
