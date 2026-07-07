usernames = ""
userid = ""
booklist = "the-book java-basic python-basic c++ sql-database oprating-syteam"
booklistcount="1 3 5 6 8 9"
avilablebook = ""
loginusers = ""
loginstatus = ""

passwords = ""

#  Issue Book related 
issuedbook=""
issuedbookidto=""

usernumbers = 0

while True:
    print("======================Wellcome to Libary mangement Syteam======================")

    usertype = input("Enter Your user type admin or student:- ").lower()

    if usertype == "student":

        usernum = usernumbers
        whologgedin=None
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

                    name = input(
                        "Enter your name (without spaces):- ").lower()

                    usernames += name + " "

                    pas = input("Enter your password :- ").lower()

                    passwords += pas + " "

                    print(
                        f"You Register Successfully. Your User ID is {usernumbers}")

                    usernumbers += 1
                # User login here multiple times ...
                case 2:

                    username = input("Enter Your Username :- ").lower()
                    password = input("Enter Your Password :- ").lower()
                    number = input("Enter Your User Number :- ")

                    countname = 0
                    countpass = 0
                    countid = 0

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

                        #  this loop run or userid 
                        s3 = ""

                        while countid < len(userid) and userid[countid] == " ":
                            countid += 1

                        while countid < len(userid) and userid[countid] != " ":
                            s3 += userid[countid]
                            countid += 1

                        if s1 == "" and s2 == "" and s3 == "":
                            break

                        if s1 == username and s2 == password and s3 == number:
                            login = True
                            break

                    if login:
                        loginusers+=s3
                        whologgedin=number
                    else:
                        print("Invalid Username, Password or User ID ❌")
                #  Print the list of books that are avilable ...
                case 3:
                    count=0
                    printcount=0
                    print("Book Name      Count ")
                    while True:
                        s=""
                        while count<len(booklist) and booklist[count] == " ":
                               count+=1
                               break
                        
                        while count<len(booklist)and booklist[count] != " ":
                                  s+=booklist[count]  
                                  count+=1   
                        print(s," ",booklistcount[printcount])
                        printcount+=2
                        if count >=len(booklist):
                             break
                #Book issue Fuctionality ...
                case 4:
                    #  Take book name as input from user ... 
                    bookname = input("Enter book name without space use - to combine two words:-").lower()
                    isavilable=False
                    bookcounindex=0 
                    bookcount=0
                    print(bookname)
                    #  Check book is avilable or not ...
                    while True:
                        s='' 
                        while bookcount<len(booklist) and booklist[bookcount] == " ":
                            bookcount+=1
                            break
                        while bookcount<len(booklist) and booklist[bookcount] !=" ":
                            s+=booklist[bookcount]
                            bookcount+=1
                        #  Match book name each time 
                        if s == bookname:
                            if int(booklistcount[bookcounindex])>0 and s:
                                issuedbook+=s
                                issuedbookidto+=whologgedin
                                print("Book issue Successfully")
                            break
                        else:
                            bookcounindex+=2
                        if bookcount>=len(booklist):
                               break
                # Book return functionality ...  
                case 5:
                    bookname= input("Enter book you went to return ..")
                    #  Check book is String ..
                    while True:
                        s='' 
                        while bookcount<len(booklist) and booklist[bookcount] == " ":
                            bookcount+=1
                            break
                        while bookcount<len(booklist) and booklist[bookcount] !=" ":
                            s+=booklist[bookcount]
                            bookcount+=1
                        #  Match book name each time 
                        if s == bookname:
                            if int(booklistcount[bookcounindex])>0 and s:
                                issuedbook+=s
                                issuedbookidto+=whologgedin
                                print("Book issue Successfully")
                            break
                        else:
                            bookcounindex+=2
                        if bookcount>=len(booklist):
                               break
                    print("Functionality to be built in future.")

                case 6:
                    print("Functionality to be built in future.")

                case 7:
                    print("Logout Successfully... ✅")
                    break

                case _:
                    print("Enter Valid Choice.")

    elif usertype == "admin":
        print("Functionality to be built in future.")

    else:
        print("Enter Valid User Type.")
        
        