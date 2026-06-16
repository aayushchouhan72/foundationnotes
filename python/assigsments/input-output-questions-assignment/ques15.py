dis1,dis2,dis3,dis4 = map(int,input("Enter all distance you travel max enter is 4").split())
tim1,tim2,tim3,tim4 = map(int,input("Enter all time  you take to  travel max enter is 4").split())

print(f"Average Speed is = {(dis1+dis2+dis3+dis4)/(tim1+tim2+tim3+tim4)} km/h")