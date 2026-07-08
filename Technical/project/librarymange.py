usernames = ""
userid = ""
passwords = ""
studentborrowed = ""

booklist = "python-basics c-programming java "
booklistcount = "5 3 2 "

adminpassword = "admin123"

usernumbers = 0

while True:
    print("======================Wellcome to Libary mangement Syteam======================")

    usertype = input("Enter Your user type admin, student or exit :- ").lower()

    match usertype:
        case "admin":
            enteredpass = input("Enter Admin Password :- ")

            match enteredpass == adminpassword:
                case False:
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
                    #  Add new book for the user...
                    case 1:

                        newbook = input("Enter new book name without space use - to combine two words:- ").lower()
                        newqty = input("Enter quantity (single digit 0-9):- ")

                        booklist += newbook + " "
                        booklistcount += newqty + " "

                        print("Book added Successfully ✅")
                    #  View all book as admin ...
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
                            match s == "":
                                case True:
                                    break
                            print(s, " ", booklistcount[bookindex * 2])
                            bookindex += 1
                            match count >= len(booklist):
                                case True:
                                    break
                    #  Search Books as Admin ...
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
                            match s == "":
                                case True:
                                    break
                            match s == searchname:
                                case True:
                                    print("Found! ", s, " - Qty:", booklistcount[bookindex * 2])
                                    found = True
                                    break
                            bookindex += 1
                            match count >= len(booklist):
                                case True:
                                    break
                        match found:
                            case False:
                                print("Book not found ❌")
                    #  Update book quentity
                    case 4:
                        updatename = input("Enter book name to update:- ").lower()
                        changetype = input("Type add to increase or remove to decrease:- ").lower()
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
                            match s == "":
                                case True:
                                    break
                            match s == updatename:
                                case True:
                                    found = True
                                    oldqty = int(booklistcount[bookindex * 2])

                                    match changetype:
                                        case "add":
                                            newqty = oldqty + changeamount
                                        case "remove":
                                            match oldqty - changeamount >= 0:
                                                case True:
                                                    newqty = oldqty - changeamount
                                                case False:
                                                    print("Not enough quantity to remove ❌")
                                                    newqty = oldqty
                                        case _:
                                            newqty = oldqty

                                    newbooklistcount = ""
                                    rebuildindex = 0
                                    while rebuildindex < len(booklistcount):
                                        match rebuildindex == bookindex * 2:
                                            case True:
                                                newbooklistcount += str(newqty)
                                            case False:
                                                newbooklistcount += booklistcount[rebuildindex]
                                        rebuildindex += 1
                                    booklistcount = newbooklistcount

                                    print("Quantity Updated Successfully ✅")
                                    break
                            bookindex += 1
                            match count >= len(booklist):
                                case True:
                                    break
                        match found:
                            case False:
                                print("Book not found ❌")
                    #  Total bools print .. 
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
                            match s == "":
                                case True:
                                    break
                            totaltitles += 1
                            totalcopies += int(booklistcount[bookindex * 2])
                            bookindex += 1
                            match count >= len(booklist):
                                case True:
                                    break
                        print("Total distinct titles:", totaltitles)
                        print("Total copies (all books):", totalcopies)
                    #  Logout ...
                    case 6:
                        print("Logout Successfully... ✅")
                        break

                    case _:
                        print("Enter Valid Choice.")

        case "student":
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
                    #  User register functionality first time..
                    case 1:
                        userid += str(usernumbers) + " "
                        name = input("Enter your name (without spaces):- ").lower()
                        usernames += name + " "
                        pas = input("Enter your password :- ").lower()
                        passwords += pas + " "
                        studentborrowed += "none "
                        print(f"You Register Successfully. Your User ID is {usernumbers}")
                        usernumbers += 1
                    #  User login multiple functionality multiple times..
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
                            #  Search user name in  String ..
                            s1 = ""
                            while countname < len(usernames) and usernames[countname] == " ":
                                countname += 1
                            while countname < len(usernames) and usernames[countname] != " ":
                                s1 += usernames[countname]
                                countname += 1
                            #  Mach corresponding password ...
                            s2 = ""
                            while countpass < len(passwords) and passwords[countpass] == " ":
                                countpass += 1
                            while countpass < len(passwords) and passwords[countpass] != " ":
                                s2 += passwords[countpass]
                                countpass += 1
                            #  Match user id in string ..
                            s3 = ""
                            while countid < len(userid) and userid[countid] == " ":
                                countid += 1
                            while countid < len(userid) and userid[countid] != " ":
                                s3 += userid[countid]
                                countid += 1
                            #  Currecnt book borrow ...
                            s4 = ""
                            while countborrow < len(studentborrowed) and studentborrowed[countborrow] == " ":
                                countborrow += 1
                            while countborrow < len(studentborrowed) and studentborrowed[countborrow] != " ":
                                s4 += studentborrowed[countborrow]
                                countborrow += 1

                            match s1 == "" and s2 == "" and s3 == "":
                                case True:
                                    break

                            match s1 == username and s2 == password and s3 == number:
                                case True:
                                    login = True
                                    whologgedin = s3
                                    currentborrowed = s4
                                    break
                        #  Login in user if above all conditions are True ..
                        match login:
                            case True:
                                print("Login Successfully ✅ Welcome", username)
                            case False:
                                print("Invalid Username, Password or User ID ❌")
                    #  View avilable Book in libarry functionality...
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
                            match s == "":
                                case True:
                                    break
                            print(s, " ", booklistcount[bookindex * 2])
                            bookindex += 1
                            if  count >= len(booklist):
                                break
                   # Issue book fucntionality for user ...
                    case 4:
                        match whologgedin is None:
                            case True:
                                print("Please login first ❌")
                            case False:
                                match currentborrowed != "none":
                                    case True:
                                        print("You already have a borrowed book:", currentborrowed)
                                        print("Return it first before borrowing another.")
                                    case False:
                                        bookname = input("Enter book name without space use - to combine two words:- ").lower()
                                        count = 0
                                        bookindex = 0
                                        foundbook = False
                                        issued = False

                                        while True:
                                            s = ""
                                            while count < len(booklist) and booklist[count] == " ":
                                                count += 1
                                            while count < len(booklist) and booklist[count] != " ":
                                                s += booklist[count]
                                                count += 1
                                            match s == "":
                                                case True:
                                                    break
                                            match s == bookname:
                                                case True:
                                                    foundbook = True
                                                    match int(booklistcount[bookindex * 2]) > 0:
                                                        case True:
                                                            newqty = int(booklistcount[bookindex * 2]) - 1
                                                            newbooklistcount = ""
                                                            rebuildindex = 0
                                                            while rebuildindex < len(booklistcount):
                                                                match rebuildindex == bookindex * 2:
                                                                    case True:
                                                                        newbooklistcount += str(newqty)
                                                                    case False:
                                                                        newbooklistcount += booklistcount[rebuildindex]
                                                                rebuildindex += 1
                                                            booklistcount = newbooklistcount
                                                            currentborrowed = s
                                                            issued = True
                                                            print("Book issued Successfully ✅")
                                                        case False:
                                                            print("Book not Available ❌")
                                                    break
                                            bookindex += 1
                                            match count >= len(booklist):
                                                case True:
                                                    break

                                        match foundbook:
                                            case False:
                                                print("Book not found ❌")

                                        match issued:
                                            case True:
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

                                                    match s3 == "" and s4 == "":
                                                        case True:
                                                            break

                                                    match s3 == whologgedin:
                                                        case True:
                                                            newstudentborrowed += currentborrowed + " "
                                                        case False:
                                                            newstudentborrowed += s4 + " "
                                                studentborrowed = newstudentborrowed
                  # Return book by user...
                    case 5:
                        match whologgedin is None:
                            case True:
                                print("Please login first ❌")
                            case False:
                                match currentborrowed == "none":
                                    case True:
                                        print("You have no book to return ❌")
                                    case False:
                                        returnname = currentborrowed
                                        count = 0
                                        bookindex = 0

                                        while True:
                                            s = ""
                                            while count < len(booklist) and booklist[count] == " ":
                                                count += 1
                                            while count < len(booklist) and booklist[count] != " ":
                                                s += booklist[count]
                                                count += 1
                                            match s == "":
                                                case True:
                                                    break
                                            match s == returnname:
                                                case True:
                                                    newqty = int(booklistcount[bookindex * 2]) + 1
                                                    newbooklistcount = ""
                                                    rebuildindex = 0
                                                    while rebuildindex < len(booklistcount):
                                                        match rebuildindex == bookindex * 2:
                                                            case True:
                                                                newbooklistcount += str(newqty)
                                                            case False:
                                                                newbooklistcount += booklistcount[rebuildindex]
                                                        rebuildindex += 1
                                                    booklistcount = newbooklistcount
                                                    break
                                            bookindex += 1
                                            match count >= len(booklist):
                                                case True:
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

                                            match s3 == "" and s4 == "":
                                                case True:
                                                    break

                                            match s3 == whologgedin:
                                                case True:
                                                    newstudentborrowed += currentborrowed + " "
                                                case False:
                                                    newstudentborrowed += s4 + " "
                                        studentborrowed = newstudentborrowed
                  # Check current borrowed books ...
                    case 6:
                        match whologgedin is None:
                            case True:
                                print("Please login first ❌")
                            case False:
                                match currentborrowed == "none":
                                    case True:
                                        print("You haven't borrowed any book.")
                                    case False:
                                        print("Your borrowed book:", currentborrowed)
                    #  Logout user ...
                    case 7:
                        print("Logout Successfully... ✅")
                        break

                    case _:
                        print("Enter Valid Choice.")
        case "exit":
            print("Thank you for using the Library System. Goodbye! ✅")
            break

        case _:
            print("Enter Valid User Type.")