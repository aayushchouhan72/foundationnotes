adminpassword = "admin123"
books = "python-basics,5|c-programming,3|java,2|"
users = ""
userid = 1

while True:
    print("\n========== 📚 LIBRARY MANAGEMENT SYSTEM 📚 ==========")
    print("1. 👤 Admin")
    print("2. 🎓 Student")
    print("3. ❌ Exit")

    try:
        main = int(input("Enter Choice 🔢 : "))
    except:
        print("Invalid Choice")
        continue

    match main:
        case 1:
            if input("🔒 Enter Admin Password : ") != adminpassword:
                print("❌ Wrong Password")
                continue

            while True:
                print("\n1. ➕ Add Book")
                print("2. 📋 View Books")
                print("3. 🔍 Search Book")
                print("4. 🔄 Update Quantity")
                print("5. 🚪 Logout")

                ch = int(input("Choice 🔢 : "))

                match ch:
                    case 1:
                        name = input("📖 Book Name : ").lower().strip()
                        qty = input("🔢 Quantity : ")
                        books += f"{name},{qty}|"
                        print("✅ Book Added Successfully!")

                    case 2:
                        print("\n📖 Book Name\tQuantity")
                        for rec in books.split("|"):
                            if rec:
                                b,q = rec.split(",")
                                print(f"{b}\t{q}")

                    case 3:
                        s = input("🔍 Search Book : ").lower().strip()
                        found=False
                        for rec in books.split("|"):
                            if rec:
                                b,q=rec.split(",")
                                if b==s:
                                    print(f"Found : {b} Qty={q}")
                                    found=True
                        if not found:
                            print("Book Not Found")

                    case 4:
                        s=input("Book Name : ").lower().strip()
                        op=input("add/remove : ").lower().strip()
                        amt=int(input("Amount : "))
                        newbooks=""
                        found=False
                        for rec in books.split("|"):
                            if rec:
                                b,q=rec.split(",")
                                q=int(q)
                                if b==s:
                                    found=True
                                    if op=="add":
                                        q+=amt
                                    elif op=="remove":
                                        q=max(0,q-amt)
                                newbooks+=f"{b},{q}|"
                        books=newbooks
                        print("Updated" if found else "Book Not Found")

                    case 5:
                        break

        case 2:
            login=""
            borrowed="none"

            while True:
                print("\n1.Register")
                print("2.Login")
                print("3.View Books")
                print("4.Borrow Book")
                print("5.Return Book")
                print("6.My Borrowed Book")
                print("7.Logout")

                ch=int(input("Choice : "))

                match ch:
                    case 1:
                        email=input("Email:-  ").lower().strip()
                        pw=input("Password : ")
                        isexist =False
                        if not ( email.endswith("@yahoo.com") or email.endswith("@gmail.com")):
                             print("Enter Valid email ...")
                             continue
                        for rec in users.split("|"):
                             if rec:
                                 i,n,p,br=rec.split(",")
                                 if i==uid and n==email and p==pw:
                                     isexist=True  
                                     break
                        if isexist:
                              print("User Already with that email")
                              continue
                        users+=f"{userid},{email},{pw},none|"
                        print("Registered. ID =",userid)
                        userid+=1

                    case 2:
                        uid=input("ID : ")
                        name=input("Name : ").lower().strip()
                        pw=input("Password : ")
                        ok=False
                        for rec in users.split("|"):
                            if rec:
                                i,n,p,br=rec.split(",")
                                if i==uid and n==name and p==pw:
                                    login=i
                                    borrowed=br
                                    ok=True
                                    print("Login Successful")
                                    break
                        if not ok:
                            print("Invalid Credentials")

                    case 3:
                        print("\nBook\tQty")
                        for rec in books.split("|"):
                            if rec:
                                b,q=rec.split(",")
                                print(f"{b}\t{q}")

                    case 4:
                        if login=="":
                            print("Login First")
                            continue
                        if borrowed!="none":
                            print("Return previous book first")
                            continue
                        bname=input("Book Name : ").lower().strip()
                        newbooks=""
                        found=False
                        success=False
                        for rec in books.split("|"):
                            if rec:
                                b,q=rec.split(",")
                                q=int(q)
                                if b==bname:
                                    found=True
                                    if q>0:
                                        q-=1
                                        borrowed=b
                                        success=True
                                newbooks+=f"{b},{q}|"
                        books=newbooks
                        if not found:
                            print("Book Not Found")
                            continue
                        if not success:
                            print("Out of Stock")
                            continue
                        newusers=""
                        for rec in users.split("|"):
                            if rec:
                                i,n,p,br=rec.split(",")
                                if i==login:
                                    br=borrowed
                                newusers+=f"{i},{n},{p},{br}|"
                        users=newusers
                        print("Book Borrowed Successfully")

                    case 5:
                        if login=="":
                            print("Login First")
                            continue
                        if borrowed=="none":
                            print("No Book Borrowed")
                            continue
                        newbooks=""
                        for rec in books.split("|"):
                            if rec:
                                b,q=rec.split(",")
                                q=int(q)
                                if b==borrowed:
                                    q+=1
                                newbooks+=f"{b},{q}|"
                        books=newbooks
                        newusers=""
                        for rec in users.split("|"):
                            if rec:
                                i,n,p,br=rec.split(",")
                                if i==login:
                                    br="none"
                                newusers+=f"{i},{n},{p},{br}|"
                        users=newusers
                        borrowed="none"
                        print("Book Returned Successfully")

                    case 6:
                        print("Borrowed Book :",borrowed)

                    case 7:
                        login=""
                        borrowed="none"
                        print("Logged Out")
                        break

        case 3:

            print("Thank You!")
            break

        case _:
            print("Invalid Choice")
