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

usernames = ""
userid = ""
passwords = ""
studentborrowed = ""

booklist = "python-basics c-programming java"
booklistcount = "5 3 2 "

adminpassword = "admin123"

usernumbers = 0

while True:
    print("======================Wellcome to Libary mangement Syteam======================")

    usertype = input("Enter Your user type admin, student or exit :- ").lower()

    # =========================== ADMIN ===========================
    if usertype == "admin":

        enteredpass = input("Enter Admin Password :- ")

        if enteredpass != adminpassword:
            print("Wrong Password ❌")
            continue

        while True:

            print("1 -> Add Book")
            print("2 -> View Books")
            print("3 -> Search Book")
            print("4 -> Update Quantity")
            print("5 -> Total Books")
            print("6 -> Logout")

            choice = int(input("Enter Your Choice :- "))

            match choice:

                # Add a new book to the booklist ...
                case 1:

                    newbook = input(
                        "Enter new book name without space use - to combine two words:- ").lower()
                    newqty = input("Enter quantity (single digit 0-9):- ")

                    booklist += newbook + " "
                    booklistcount += newqty + " "

                    print("Book added Successfully ✅")

                # Print the list of books that are avilable ...
                case 2:
                    count = 0
                    bookindex = 0
                    print("Book Name      Count ")
                    while True:
                        s = ""
                        while count < len(booklist) and booklist[count] == " ":
                            count += 1
                        while count < len(booklist) and booklist[count] != " ":
                            s += booklist[count]
                            count += 1
                        if s == "":
                            break
                        print(s, " ", booklistcount[bookindex * 2])
                        bookindex += 1
                        if count >= len(booklist):
                            break

                # Search a single book by name ...
                case 3:
                    searchname = input("Enter book name to search:- ").lower()
                    count = 0
                    bookindex = 0
                    found = False
                    while True:
                        s = ""
                        while count < len(booklist) and booklist[count] == " ":
                            count += 1
                        while count < len(booklist) and booklist[count] != " ":
                            s += booklist[count]
                            count += 1
                        if s == "":
                            break
                        if s == searchname:
                            print("Found! ", s, " - Qty:", booklistcount[bookindex * 2])
                            found = True
                            break
                        bookindex += 1
                        if count >= len(booklist):
                            break
                    if not found:
                        print("Book not found ❌")

                # Update the quantity of a book (add or remove) ...
                case 4:
                    updatename = input("Enter book name to update:- ").lower()
                    changetype = input(
                        "Type add to increase or remove to decrease:- ").lower()
                    changeamount = int(input("Enter amount (single digit):- "))

                    count = 0
                    bookindex = 0
                    found = False
                    while True:
                        s = ""
                        while count < len(booklist) and booklist[count] == " ":
                            count += 1
                        while count < len(booklist) and booklist[count] != " ":
                            s += booklist[count]
                            count += 1
                        if s == "":
                            break
                        if s == updatename:
                            found = True
                            oldqty = int(booklistcount[bookindex * 2])

                            if changetype == "add":
                                newqty = oldqty + changeamount
                            elif changetype == "remove":
                                if oldqty - changeamount >= 0:
                                    newqty = oldqty - changeamount
                                else:
                                    print("Not enough quantity to remove ❌")
                                    newqty = oldqty
                            else:
                                newqty = oldqty

                            newbooklistcount = ""
                            rebuildindex = 0
                            while rebuildindex < len(booklistcount):
                                if rebuildindex == bookindex * 2:
                                    newbooklistcount += str(newqty)
                                else:
                                    newbooklistcount += booklistcount[rebuildindex]
                                rebuildindex += 1
                            booklistcount = newbooklistcount

                            print("Quantity Updated Successfully ✅")
                            break
                        bookindex += 1
                        if count >= len(booklist):
                            break
                    if not found:
                        print("Book not found ❌")

                # Show total distinct titles and total copies ...
                case 5:
                    count = 0
                    bookindex = 0
                    totaltitles = 0
                    totalcopies = 0
                    while True:
                        s = ""
                        while count < len(booklist) and booklist[count] == " ":
                            count += 1
                        while count < len(booklist) and booklist[count] != " ":
                            s += booklist[count]
                            count += 1
                        if s == "":
                            break
                        totaltitles += 1
                        totalcopies += int(booklistcount[bookindex * 2])
                        bookindex += 1
                        if count >= len(booklist):
                            break
                    print("Total distinct titles:", totaltitles)
                    print("Total copies (all books):", totalcopies)

                case 6:
                    print("Logout Successfully... ✅")
                    break

                case _:
                    print("Enter Valid Choice.")

    # =========================== STUDENT ===========================
    elif usertype == "student":

        whologgedin = None
        currentborrowed = "none"

        while True:

            print("1 -> Register student")
            print("2 -> Login using Student ID")
            print("3 -> View available books")
            print("4 -> Borrow a book")
            print("5 -> Return a book")
            print("6 -> Check borrowed book")
            print("7 -> Logout")

            choice = int(input("Enter Your Choice :- "))

            match choice:

                # New user Register here For First time ...
                case 1:

                    userid += str(usernumbers) + " "

                    name = input("Enter your name (without spaces):- ").lower()
                    usernames += name + " "

                    pas = input("Enter your password :- ").lower()
                    passwords += pas + " "

                    studentborrowed += "none "

                    print(f"You Register Successfully. Your User ID is {usernumbers}")

                    usernumbers += 1

                # User login here multiple times ...
                case 2:

                    username = input("Enter Your Username :- ").lower()
                    password = input("Enter Your Password :- ").lower()
                    number = input("Enter Your User Number :- ")

                    countname = 0
                    countpass = 0
                    countid = 0
                    countborrow = 0

                    login = False

                    while True:

                        # Check Username ..
                        s1 = ""
                        while countname < len(usernames) and usernames[countname] == " ":
                            countname += 1
                        while countname < len(usernames) and usernames[countname] != " ":
                            s1 += usernames[countname]
                            countname += 1

                        # Check password ..
                        s2 = ""
                        while countpass < len(passwords) and passwords[countpass] == " ":
                            countpass += 1
                        while countpass < len(passwords) and passwords[countpass] != " ":
                            s2 += passwords[countpass]
                            countpass += 1

                        # this loop run or userid ..
                        s3 = ""
                        while countid < len(userid) and userid[countid] == " ":
                            countid += 1
                        while countid < len(userid) and userid[countid] != " ":
                            s3 += userid[countid]
                            countid += 1

                        # this loop run for studentborrowed ..
                        s4 = ""
                        while countborrow < len(studentborrowed) and studentborrowed[countborrow] == " ":
                            countborrow += 1
                        while countborrow < len(studentborrowed) and studentborrowed[countborrow] != " ":
                            s4 += studentborrowed[countborrow]
                            countborrow += 1

                        if s1 == "" and s2 == "" and s3 == "":
                            break

                        if s1 == username and s2 == password and s3 == number:
                            login = True
                            whologgedin = s3
                            currentborrowed = s4
                            break

                    if login:
                        print("Login Successfully ✅ Welcome", username)
                    else:
                        print("Invalid Username, Password or User ID ❌")

                # Print the list of books that are avilable ...
                case 3:
                    count = 0
                    bookindex = 0
                    print("Book Name      Count ")
                    while True:
                        s = ""
                        while count < len(booklist) and booklist[count] == " ":
                            count += 1
                        while count < len(booklist) and booklist[count] != " ":
                            s += booklist[count]
                            count += 1
                        if s == "":
                            break
                        print(s, " ", booklistcount[bookindex * 2])
                        bookindex += 1
                        if count >= len(booklist):
                            break

                # Book issue Fuctionality ...
                case 4:
                    if whologgedin is None:
                        print("Please login first ❌")
                    elif currentborrowed != "none":
                        print("You already have a borrowed book:", currentborrowed)
                        print("Return it first before borrowing another.")
                    else:
                        bookname = input(
                            "Enter book name without space use - to combine two words:- ").lower()

                        count = 0
                        bookindex = 0
                        foundbook = False
                        issued = False

                        # Check book is avilable or not ...
                        while True:
                            s = ""
                            while count < len(booklist) and booklist[count] == " ":
                                count += 1
                            while count < len(booklist) and booklist[count] != " ":
                                s += booklist[count]
                                count += 1
                            if s == "":
                                break
                            # Match book name each time
                            if s == bookname:
                                foundbook = True
                                if int(booklistcount[bookindex * 2]) > 0:
                                    newqty = int(booklistcount[bookindex * 2]) - 1
                                    newbooklistcount = ""
                                    rebuildindex = 0
                                    while rebuildindex < len(booklistcount):
                                        if rebuildindex == bookindex * 2:
                                            newbooklistcount += str(newqty)
                                        else:
                                            newbooklistcount += booklistcount[rebuildindex]
                                        rebuildindex += 1
                                    booklistcount = newbooklistcount
                                    currentborrowed = s
                                    issued = True
                                    print("Book issued Successfully ✅")
                                else:
                                    print("Book not Available ❌")
                                break
                            bookindex += 1
                            if count >= len(booklist):
                                break

                        if not foundbook:
                            print("Book not found ❌")

                        # Save the borrowed book against the logged in student ..
                        if issued:
                            countid2 = 0
                            countborrow2 = 0
                            newstudentborrowed = ""
                            while True:
                                s3 = ""
                                while countid2 < len(userid) and userid[countid2] == " ":
                                    countid2 += 1
                                while countid2 < len(userid) and userid[countid2] != " ":
                                    s3 += userid[countid2]
                                    countid2 += 1

                                s4 = ""
                                while countborrow2 < len(studentborrowed) and studentborrowed[countborrow2] == " ":
                                    countborrow2 += 1
                                while countborrow2 < len(studentborrowed) and studentborrowed[countborrow2] != " ":
                                    s4 += studentborrowed[countborrow2]
                                    countborrow2 += 1

                                if s3 == "" and s4 == "":
                                    break

                                if s3 == whologgedin:
                                    newstudentborrowed += currentborrowed + " "
                                else:
                                    newstudentborrowed += s4 + " "

                            studentborrowed = newstudentborrowed

                # Book return functionality ...
                case 5:
                    if whologgedin is None:
                        print("Please login first ❌")
                    elif currentborrowed == "none":
                        print("You have no book to return ❌")
                    else:
                        returnname = currentborrowed

                        count = 0
                        bookindex = 0

                        # Check book is String and bump its count back up ..
                        while True:
                            s = ""
                            while count < len(booklist) and booklist[count] == " ":
                                count += 1
                            while count < len(booklist) and booklist[count] != " ":
                                s += booklist[count]
                                count += 1
                            if s == "":
                                break
                            if s == returnname:
                                newqty = int(booklistcount[bookindex * 2]) + 1
                                newbooklistcount = ""
                                rebuildindex = 0
                                while rebuildindex < len(booklistcount):
                                    if rebuildindex == bookindex * 2:
                                        newbooklistcount += str(newqty)
                                    else:
                                        newbooklistcount += booklistcount[rebuildindex]
                                    rebuildindex += 1
                                booklistcount = newbooklistcount
                                break
                            bookindex += 1
                            if count >= len(booklist):
                                break

                        currentborrowed = "none"
                        print("Book Returned Successfully ✅")

                        countid2 = 0
                        countborrow2 = 0
                        newstudentborrowed = ""
                        while True:
                            s3 = ""
                            while countid2 < len(userid) and userid[countid2] == " ":
                                countid2 += 1
                            while countid2 < len(userid) and userid[countid2] != " ":
                                s3 += userid[countid2]
                                countid2 += 1

                            s4 = ""
                            while countborrow2 < len(studentborrowed) and studentborrowed[countborrow2] == " ":
                                countborrow2 += 1
                            while countborrow2 < len(studentborrowed) and studentborrowed[countborrow2] != " ":
                                s4 += studentborrowed[countborrow2]
                                countborrow2 += 1

                            if s3 == "" and s4 == "":
                                break

                            if s3 == whologgedin:
                                newstudentborrowed += currentborrowed + " "
                            else:
                                newstudentborrowed += s4 + " "

                        studentborrowed = newstudentborrowed

                # Check what book is currently borrowed ...
                case 6:
                    if whologgedin is None:
                        print("Please login first ❌")
                    elif currentborrowed == "none":
                        print("You haven't borrowed any book.")
                    else:
                        print("Your borrowed book:", currentborrowed)

                case 7:
                    print("Logout Successfully... ✅")
                    break

                case _:
                    print("Enter Valid Choice.")

    elif usertype == "exit":
        print("Thank you for using the Library System. Goodbye! ✅")
        break

    else:
        print("Enter Valid User Type.")