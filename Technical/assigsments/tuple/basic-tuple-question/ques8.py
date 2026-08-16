matrix = []
row = int(input("Enter number of rows ...."))
column = int(input("Enter number of columns ...."))

for i in range(row):
    lis = []
    print()
    for j in range(column):
        value = int(input("Enter matrix element ...."))
        lis.append(value)
    matrix.append(lis)

while True:
    print()
    print("1. Count Even Numbers Above Main Diagonal")
    print("2. Count Odd Numbers Below Main Diagonal")
    print("3. Display Boundary Elements")
    print("4. Exit")

    choice = int(input("Enter your choice ...."))

    if choice == 1:
        count = 0
        print()
        print("Even Numbers Above Main Diagonal:")
        for i in range(row):
            for j in range(column):
                if j > i and matrix[i][j] % 2 == 0:
                    print(matrix[i][j], end=" ")
                    count += 1
        print()
        print(f"Even Numbers Above Main Diagonal = {count}")

    elif choice == 2:
        count = 0
        print()
        print("Odd Numbers Below Main Diagonal:")
        for i in range(row):
            for j in range(column):
                if i > j and matrix[i][j] % 2 != 0:
                    print(matrix[i][j], end=" ")
                    count += 1
        print()
        print(f"Odd Numbers Below Main Diagonal = {count}")

    elif choice == 3:
        print()
        print("Boundary Elements:")

        for j in range(column):
            print(matrix[0][j], end=" ")

        for i in range(1, row):
            print(matrix[i][column - 1], end=" ")

        for j in range(column - 2, -1, -1):
            print(matrix[row - 1][j], end=" ")

        for i in range(row - 2, 0, -1):
            print(matrix[i][0], end=" ")

        print()

    elif choice == 4:
        break

    else:
        print("Invalid Choice")
        