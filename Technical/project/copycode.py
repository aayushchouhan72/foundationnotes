"""
LIBRARY MANAGEMENT SYSTEM - STAGE 1
Built using ONLY: variables, loops, if/else, and strings.
No lists, no dictionaries, no files, no functions yet.

Data storage strategy:
- Books are stored as one string with format:  name,quantity|name,quantity|...
- Students are stored as one string with format: id,name,password,borrowed|...
  ("None" means the student hasn't borrowed anything)
"""

# ---------- INITIAL DATA ----------

books = "Python Basics,5|C Programming,3|Java,2"
students = "ST101,Aayush,1234,None"

admin_password = "admin123"


# ---------- MAIN PROGRAM LOOP ----------

while True:
    print("\n========= LIBRARY =========")
    print("1. Admin")
    print("2. Student")
    print("3. Exit")
    main_choice = input("Choose: ")

    # ================= ADMIN =================
    if main_choice == "1":
        entered_pass = input("Enter admin password: ")

        if entered_pass == admin_password:
            while True:
                print("\n----- ADMIN MENU -----")
                print("1. Add Book")
                print("2. View Books")
                print("3. Search Book")
                print("4. Update Quantity")
                print("5. Total Books")
                print("6. Logout")
                admin_choice = input("Choose: ")

                # ---- ADD BOOK ----
                if admin_choice == "1":
                    new_name = input("Enter new book name: ")
                    new_qty = input("Enter quantity: ")

                    if books == "":
                        books = new_name + "," + new_qty
                    else:
                        books = books + "|" + new_name + "," + new_qty

                    print("Book added successfully!")

                # ---- VIEW BOOKS ----
                elif admin_choice == "2":
                    print("\n--- Book List ---")
                    remaining = books
                    while remaining != "":
                        pipe_pos = remaining.find("|")

                        if pipe_pos == -1:
                            record = remaining
                            remaining = ""
                        else:
                            record = remaining[0:pipe_pos]
                            remaining = remaining[pipe_pos + 1:]

                        comma_pos = record.find(",")
                        book_name = record[0:comma_pos]
                        book_qty = record[comma_pos + 1:]
                        print(book_name + " - Qty: " + book_qty)

                # ---- SEARCH BOOK ----
                elif admin_choice == "3":
                    search_name = input("Enter book name to search: ")
                    remaining = books
                    found = "no"

                    while remaining != "":
                        pipe_pos = remaining.find("|")

                        if pipe_pos == -1:
                            record = remaining
                            remaining = ""
                        else:
                            record = remaining[0:pipe_pos]
                            remaining = remaining[pipe_pos + 1:]

                        comma_pos = record.find(",")
                        book_name = record[0:comma_pos]
                        book_qty = record[comma_pos + 1:]

                        if book_name == search_name:
                            print("Found! " + book_name + " - Qty: " + book_qty)
                            found = "yes"

                    if found == "no":
                        print("Book not found.")

                # ---- UPDATE QUANTITY ----
                elif admin_choice == "4":
                    update_name = input("Enter book name to update: ")
                    change_type = input("Type 'add' to increase or 'remove' to decrease: ")
                    change_amount = int(input("Enter amount: "))

                    updated_books = ""
                    remaining = books
                    found = "no"

                    while remaining != "":
                        pipe_pos = remaining.find("|")

                        if pipe_pos == -1:
                            record = remaining
                            remaining = ""
                        else:
                            record = remaining[0:pipe_pos]
                            remaining = remaining[pipe_pos + 1:]

                        comma_pos = record.find(",")
                        book_name = record[0:comma_pos]
                        book_qty = int(record[comma_pos + 1:])

                        if book_name == update_name:
                            found = "yes"
                            if change_type == "add":
                                book_qty = book_qty + change_amount
                            elif change_type == "remove":
                                if book_qty - change_amount >= 0:
                                    book_qty = book_qty - change_amount
                                else:
                                    print("Not enough quantity to remove!")

                        new_record = book_name + "," + str(book_qty)

                        if updated_books == "":
                            updated_books = new_record
                        else:
                            updated_books = updated_books + "|" + new_record

                    books = updated_books

                    if found == "yes":
                        print("Quantity updated successfully!")
                    else:
                        print("Book not found.")

                # ---- TOTAL BOOKS ----
                elif admin_choice == "5":
                    remaining = books
                    total_titles = 0
                    total_copies = 0

                    while remaining != "":
                        pipe_pos = remaining.find("|")

                        if pipe_pos == -1:
                            record = remaining
                            remaining = ""
                        else:
                            record = remaining[0:pipe_pos]
                            remaining = remaining[pipe_pos + 1:]

                        comma_pos = record.find(",")
                        book_qty = int(record[comma_pos + 1:])

                        total_titles = total_titles + 1
                        total_copies = total_copies + book_qty

                    print("Total distinct titles: " + str(total_titles))
                    print("Total copies (all books): " + str(total_copies))

                # ---- LOGOUT ----
                elif admin_choice == "6":
                    print("Logging out of admin...")
                    break

                else:
                    print("Invalid choice, try again.")

        else:
            print("Wrong password!")

    # ================= STUDENT =================
    elif main_choice == "2":
        print("\n1. Login")
        print("2. Register")
        student_action = input("Choose: ")

        # ---- REGISTER ----
        if student_action == "2":
            new_id = input("Enter new Student ID: ")
            new_name = input("Enter your name: ")
            new_pass = input("Set a password: ")
            new_record = new_id + "," + new_name + "," + new_pass + ",None"

            if students == "":
                students = new_record
            else:
                students = students + "|" + new_record

            print("Registration successful! You can now login.")

        # ---- LOGIN ----
        elif student_action == "1":
            login_id = input("Enter Student ID: ")
            login_pass = input("Enter Password: ")

            remaining = students
            logged_in = "no"
            current_name = ""
            current_borrowed = ""

            while remaining != "":
                pipe_pos = remaining.find("|")

                if pipe_pos == -1:
                    record = remaining
                    remaining = ""
                else:
                    record = remaining[0:pipe_pos]
                    remaining = remaining[pipe_pos + 1:]

                c1 = record.find(",")
                c2 = record.find(",", c1 + 1)
                c3 = record.find(",", c2 + 1)

                s_id = record[0:c1]
                s_name = record[c1 + 1:c2]
                s_pass = record[c2 + 1:c3]
                s_borrowed = record[c3 + 1:]

                if s_id == login_id and s_pass == login_pass:
                    logged_in = "yes"
                    current_name = s_name
                    current_borrowed = s_borrowed

            if logged_in == "yes":
                print("Welcome, " + current_name + "!")

                while True:
                    print("\n----- STUDENT MENU -----")
                    print("1. View Books")
                    print("2. Borrow Book")
                    print("3. Return Book")
                    print("4. My Book")
                    print("5. Logout")
                    student_choice = input("Choose: ")

                    # ---- VIEW BOOKS ----
                    if student_choice == "1":
                        remaining_books = books
                        while remaining_books != "":
                            pipe_pos = remaining_books.find("|")

                            if pipe_pos == -1:
                                record = remaining_books
                                remaining_books = ""
                            else:
                                record = remaining_books[0:pipe_pos]
                                remaining_books = remaining_books[pipe_pos + 1:]

                            comma_pos = record.find(",")
                            book_name = record[0:comma_pos]
                            book_qty = record[comma_pos + 1:]
                            print(book_name + " - Qty: " + book_qty)

                    # ---- BORROW BOOK ----
                    elif student_choice == "2":
                        if current_borrowed != "None":
                            print("You already have a borrowed book: " + current_borrowed)
                            print("Return it first before borrowing another.")
                        else:
                            borrow_name = input("Enter book name to borrow: ")

                            updated_books = ""
                            remaining_books = books
                            success = "no"

                            while remaining_books != "":
                                pipe_pos = remaining_books.find("|")

                                if pipe_pos == -1:
                                    record = remaining_books
                                    remaining_books = ""
                                else:
                                    record = remaining_books[0:pipe_pos]
                                    remaining_books = remaining_books[pipe_pos + 1:]

                                comma_pos = record.find(",")
                                book_name = record[0:comma_pos]
                                book_qty = int(record[comma_pos + 1:])

                                if book_name == borrow_name and book_qty > 0:
                                    book_qty = book_qty - 1
                                    success = "yes"

                                new_record = book_name + "," + str(book_qty)

                                if updated_books == "":
                                    updated_books = new_record
                                else:
                                    updated_books = updated_books + "|" + new_record

                            books = updated_books

                            if success == "yes":
                                current_borrowed = borrow_name
                                print("Book Borrowed Successfully")

                                # update the students string with new borrowed value
                                updated_students = ""
                                remaining_students = students

                                while remaining_students != "":
                                    pipe_pos = remaining_students.find("|")

                                    if pipe_pos == -1:
                                        record = remaining_students
                                        remaining_students = ""
                                    else:
                                        record = remaining_students[0:pipe_pos]
                                        remaining_students = remaining_students[pipe_pos + 1:]

                                    c1 = record.find(",")
                                    c2 = record.find(",", c1 + 1)
                                    c3 = record.find(",", c2 + 1)
                                    s_id = record[0:c1]
                                    s_name = record[c1 + 1:c2]
                                    s_pass = record[c2 + 1:c3]
                                    s_borrowed = record[c3 + 1:]

                                    if s_id == login_id:
                                        s_borrowed = current_borrowed

                                    new_record = s_id + "," + s_name + "," + s_pass + "," + s_borrowed

                                    if updated_students == "":
                                        updated_students = new_record
                                    else:
                                        updated_students = updated_students + "|" + new_record

                                students = updated_students
                            else:
                                print("Book Not Available")

                    # ---- RETURN BOOK ----
                    elif student_choice == "3":
                        if current_borrowed == "None":
                            print("You have no book to return.")
                        else:
                            return_name = current_borrowed

                            updated_books = ""
                            remaining_books = books

                            while remaining_books != "":
                                pipe_pos = remaining_books.find("|")

                                if pipe_pos == -1:
                                    record = remaining_books
                                    remaining_books = ""
                                else:
                                    record = remaining_books[0:pipe_pos]
                                    remaining_books = remaining_books[pipe_pos + 1:]

                                comma_pos = record.find(",")
                                book_name = record[0:comma_pos]
                                book_qty = int(record[comma_pos + 1:])

                                if book_name == return_name:
                                    book_qty = book_qty + 1

                                new_record = book_name + "," + str(book_qty)

                                if updated_books == "":
                                    updated_books = new_record
                                else:
                                    updated_books = updated_books + "|" + new_record

                            books = updated_books
                            current_borrowed = "None"
                            print("Book Returned Successfully")

                            # update students string
                            updated_students = ""
                            remaining_students = students

                            while remaining_students != "":
                                pipe_pos = remaining_students.find("|")

                                if pipe_pos == -1:
                                    record = remaining_students
                                    remaining_students = ""
                                else:
                                    record = remaining_students[0:pipe_pos]
                                    remaining_students = remaining_students[pipe_pos + 1:]

                                c1 = record.find(",")
                                c2 = record.find(",", c1 + 1)
                                c3 = record.find(",", c2 + 1)
                                s_id = record[0:c1]
                                s_name = record[c1 + 1:c2]
                                s_pass = record[c2 + 1:c3]
                                s_borrowed = record[c3 + 1:]

                                if s_id == login_id:
                                    s_borrowed = "None"

                                new_record = s_id + "," + s_name + "," + s_pass + "," + s_borrowed

                                if updated_students == "":
                                    updated_students = new_record
                                else:
                                    updated_students = updated_students + "|" + new_record

                            students = updated_students

                    # ---- MY BOOK ----
                    elif student_choice == "4":
                        if current_borrowed == "None":
                            print("You haven't borrowed any book.")
                        else:
                            print("Your borrowed book: " + current_borrowed)

                    # ---- LOGOUT ----
                    elif student_choice == "5":
                        print("Logging out...")
                        break

                    else:
                        print("Invalid choice, try again.")

            else:
                print("Invalid ID or password.")

        else:
            print("Invalid choice.")

    # ================= EXIT =================
    elif main_choice == "3":
        print("Thank you for using the Library System. Goodbye!")
        break

    else:
        print("Invalid choice, please select 1, 2 or 3.")