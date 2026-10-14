runs=int(input("Enter the total runs "))

totalovers = input("Enter the total number of overs should EX 34.5 in this formate :- ")

intover,decover = map(int,totalovers.split("."))

totalball =  decover+intover*6

print(totalball,decover,intover)



totalovers = totalball/6

runrate= runs/totalovers

print(f"Total Balls = {totalball} \nRun Rate = {runrate}")

