# 5.
# =========================================
# LIBRARY ISBN MANAGER
# =========================================

# A library stores unique ISBN numbers of books.

# Menu:
# 1. Add ISBN
# 2. Remove ISBN
# 3. Search ISBN
# 4. Display ISBN List
# 5. Count Books
# 6. Exit

# Requirements:
# - Use Set.
# - Duplicate ISBNs are not allowed.



visitors=set()
while True:
    print("1. Add ISBN\n2. Remove ISBN\n3. Search ISBN\n4. Display ISBN List\n5. Count Books\n6. Exit"
    )
    choice = input("Enter the your choice")
    match choice:
       case "1":
            visitors.add(input("Enter the  Add ISBN"))
       case "2":
            visitors.discard(input("Enter the Remove ISBN"))
       case "3":
            print("Wellcome in serching part of book section \n")
            bookname= input("Enter the book name ...").lower()
            for i in visitors: 
                  if i == bookname:
                        print("Book is found in libarey")
                        break
            else:
                print("book is not found ...")           
       case "4":
              print("Display ISBN List",*list(visitors))     
       case "5":
              print("Count Books",len(visitors))
       case "6":
              break
       case _:
              print("Enter the valid choice ...")
            