from model.book import Book


books = []

print("=" * 50)
print("        BOOK MANAGEMENT SYSTEM")
print("=" * 50)


for i in range(5):

    print(f"\nEnter details of Book {i + 1}")

    book_id = int(input("Enter Book Id : "))
    book_name = input("Enter Book Name : ")
    author = input("Enter Author : ")
    price = float(input("Enter Price : "))

    book = Book(book_id, book_name, author, price)

    books.append(book)


print("\n" + "=" * 50)
print("All Books:")
print("=" * 50)

for book in books:
    book.display()


search_id = int(input("\nEnter Book Id to Search : "))

found = False

for book in books:

    if book.book_id == search_id:

        print("\nBook Found:")
        book.display()

        found = True
        break

if not found:
    print("\nBook Not Found")



search_author = input("\nEnter Author Name : ")

print(f"\nBooks by {search_author}:")

found = False

for book in books:

    if book.author.lower() == search_author.lower():

        print(book.book_id, book.book_name, book.price)
        found = True

if not found:
    print("No books found by this author.")

print("\nBooks with price greater than 500:")

for book in books:

    if book.price > 500:
        print(book.book_name)


expensive_book = books[0]

for book in books:

    if book.price > expensive_book.price:
        expensive_book = book


print("\nMost Expensive Book:")
print(expensive_book.book_name, "=", expensive_book.price)



total = 0

for book in books:
    total = total + book.price

average = total / len(books)

print("\nAverage Price:")
print(average)