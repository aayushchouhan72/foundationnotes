
def get_level():
    while True:
        level =  input("Enter the Level HARD|EASY|MEDIUM :- ").lower().strip()
        if level == "hard" or level == "easy" or level == "medium":
                    return level
        else:
            print("Enter the valid defficulty level")