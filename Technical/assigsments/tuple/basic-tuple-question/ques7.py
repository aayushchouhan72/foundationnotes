lis = []
number = int(input("Enter the number of players "))

print()
for i in range(number):
    print()
    player_id = int(input("Enter the player id ...."))
    player_name = input("Enter the player name ....")
    runs_scored = int(input("Enter the runs scored ...."))
    lis.append((player_id, player_name, runs_scored))
    print()

maximum = lis[0]
minimum = lis[0]
total = 0

print("All Players:")
for i in lis:
    print(i)

    if maximum[2] < i[2]:
        maximum = i

    if minimum[2] > i[2]:
        minimum = i

    total += i[2]

print()

print("Highest Scorer:")
print(maximum)

print()

print("Lowest Scorer:")
print(minimum)

print()

print("Total Runs:")
print(total)

print()

print("Average Runs:")
print(total / number)

print()

print("Players Scoring More Than 50 Runs:")
for i in lis:
    if i[2] > 50:
        print(i)