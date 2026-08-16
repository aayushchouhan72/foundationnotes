from collections import namedtuple

book = namedtuple("Book", ["book_id", "title", "author", "price"])

lis = []
number = int(input("Enter the number of books "))

print()
for i in range(number):
    print()
    book_id = input("Enter the book id ....")
    title = input("Enter the book title ....")
    author = input("Enter the author name ....")
    price = int(input("Enter book price ...."))
    lis.append(book(book_id, title, author, price))
    print()

maximum = 0
user = ""
total = 0
author_name = input("Enter Author Name: ")

print()
for i in lis:
    print(i.book_id, i.title, i.author, i.price)

    if maximum < i.price:
        user = i
        maximum = i.price

    total += i.price

print()

print("Most Expensive Book:")
print(user)

print()

print("Average Book Price:")
print(total / number)

print()

print(f"Books Written By {author_name}:")
for i in lis:
    if i.author == author_name:
        print(i)