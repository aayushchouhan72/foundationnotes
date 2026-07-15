adminpassword = "admin123"
books = "python-basics,5|c-programming,3|java,2|"
users = ""
userid = 1

while True:
    print("\n========== 📚 LIBRARY MANAGEMENT SYSTEM 📚 ==========")
    print("1. 👤 Admin")
    print("2. 🎓 Student")
    print("3. ❌ Exit")

    main = int(input("Enter Choice 🔢 : "))

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
                    # Add Book functionality
                    case 1:
                        name = input("📖 Book Name : ").lower().strip()
                        qty = input("🔢 Quantity : ")
                        books += f"{name},{qty}|"
                        print("✅ Book Added Successfully!")
                        
                    # View Book functionality
                    case 2:
                        print("\n📖 Book Name\t 🔢 Quantity")
                        for rec in books.split("|"):
                            if rec == "":
                                continue
                            b, q = rec.split(",")
                            print(f"📘 {b}\t\t {q}")
                            
                    # Search Book functionality
                    case 3:
                        s = input("🔍 Search Book Name : ").lower().strip()
                        found = False
                        for rec in books.split("|"):
                            if rec == "":
                                continue
                            b, q = rec.split(",")
                            if b == s:
                                print(f"🔍 Found -> 📖 {b} | 🔢 Qty: {q}")
                                found = True
                                break
                        if not found:
                            print("❌ Book Not Found")
                            
                    # Update book functionality
                    case 4:
                        s = input("📖 Book Name : ").lower().strip()
                        op = input("➕ add / ➖ remove : ").lower().strip()
                        amt = int(input("🔢 Amount : "))
                        newbooks = ""
                        found = False

                        for rec in books.split("|"):
                            if rec == "":
                                continue
                            b, q = rec.split(",")
                            q = int(q)

                            if b == s:
                                found = True
                                if op == "add":
                                    q += amt
                                elif op == "remove":
                                    q = max(0, q - amt)

                            newbooks += f"{b},{q}|"

                        books = newbooks
                        print("✅ Updated Successfully!" if found else "❌ Book Not Found")
                        
                    # Logout Admin
                    case 5:
                        print("🚪 Logged out from Admin Panel.")
                        break

        case 2:
            login = ""
            borrowed = "none"

            while True:
                print("\n1. 📝 Register")
                print("2. 🔑 Login")
                print("3. 📋 View Books")
                print("4. 📥 Borrow Book")
                print("5. 📤 Return Book")
                print("6. 🧐 My Borrowed Book")
                print("7. 🚪 Logout")

                ch = int(input("Choice 🔢 : "))

                match ch:
                    # Register user functionality
                    case 1:
                        name = input("👤 Name : ").lower().strip()
                        pw = input("🔒 Password : ")
                        users += f"{userid},{name},{pw},none|"
                        print("🎉 Registration Successful!")
                        print(f"🪪 Your ID : {userid}")
                        userid += 1
                        
                    # Login user functionality
                    case 2:
                        uid = input("🪪 ID : ")
                        name = input("👤 Name : ").lower().strip()
                        pw = input("🔒 Password : ")

                        ok = False

                        for rec in users.split("|"):
                            if rec == "":
                                continue
                            i, n, p, br = rec.split(",")

                            if i == uid and n == name and p == pw:
                                login = i
                                borrowed = br
                                ok = True
                                print("✅ Login Successful!")
                                break

                        if not ok:
                            print("❌ Invalid Credentials")
                            
                    # View Books functionality
                    case 3:
                        print("\n📖 Book Name\t 🔢 Quantity")
                        for rec in books.split("|"):
                            if rec == "":
                                continue
                            b, q = rec.split(",")
                            print(f"📘 {b}\t\t {q}")
                            
                    # Borrow Books Functionality
                    case 4:
                        print("💡 Borrow feature placeholder.")
                        print("🛠️ Extend using the same string-record logic.")
                        
                    # Return Books functionality
                    case 5:
                        print("💡 Return feature placeholder.")
                        print("🛠️ Extend using the same string-record logic.")
                        
                    # Check my Borrowed functionality
                    case 6:
                        print(f"🧐 Borrowed Book : 📘 {borrowed}")
                        
                    # Logout Student
                    case 7:
                        print("🚪 Logged out from Student Panel.")
                        break

        case 3:
            print("👋 Thank You for using the Library System!")
            break

        case _:
            print("❌ Invalid Choice! Please select a valid option.")