try:
    file = open('question1/attendance.txt')
    print(file.name)
    print(file.mode)
    print(file.closed)
    file.close()
    print(file.closed)
except FileNotFoundError as e:
    print(e)
except Exception as e:
     print("Other Error ",e)
