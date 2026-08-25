userdata = "ayush@gmail.com,ayush|demoapp@gmail.com,demo|" 
noteswithtitle = "Python,Basic language,ayush@gmail.com,1|Java,OOP language,ayush@gmail.com,2|HTML,Markup language,ayush@gmail.com,3|CSS,Styles web pages,ayush@gmail.com,4|SQL,Database language,ayush@gmail.com,5|"

logineduser = ""

global_note_id = 0
for note in noteswithtitle.split("|"):
    if note.strip():
        parts = note.split(",")
        if len(parts) == 4:
            current_id = int(parts[3])
            if current_id > global_note_id:
                global_note_id = current_id

while True:
    print("\n" + "="*60)
    print("🎉 WELCOME TO THE TODO & NOTES APPLICATION 🎉".center(60))
    print("="*60)
    print("  1. 🔑 Login")
    print("  2. 📝 Register")
    print("  3. 🚪 Exit")
    print("-"*60)
    
    choice_input = input("👉 Enter Your Choice: ")
    if not choice_input.isdigit():
        print("\n⚠️  Please enter a valid number.")
        continue
    choice = int(choice_input)

    access_granted = False

    match choice:
       
        case 1:
            email = input("\n📧 Enter Your Email: ").lower().strip()
            pas = input("🔒 Enter Your Password: ").strip()
            
            if "@gmail.com" not in email and "@yahoo.com" not in email:
                print("\n❌ Error: Please enter a valid Gmail or Yahoo address.")
                continue
                
            records = userdata.split("|")
            for record in records:
                if not record.strip():
                    continue
                useremail, userpass = record.split(",")
                if useremail == email and pas == userpass:
                    access_granted = True
                    logineduser = email
                    print("\n✅ Logged in Successfully!")
                    break
            
            if not access_granted:
                print("\n❌ Invalid username or password. Please try again.")

       
        case 2:
            email = input("\n📧 Enter Your Email: ").lower().strip()
            password = input("🔒 Enter Your Password: ").strip()
            
            if "@gmail.com" not in email and "@yahoo.com" not in email:
                print("\n❌ Error: Valid Gmail or Yahoo address required.")
                continue
                
            recs = userdata.split("|")
            email_exists = False
            for rec in recs: 
                if not rec.strip():
                    continue
                idd, _ = rec.split(",")
                if idd == email:
                    print("\n⚠️  Email already exists! Try logging in.")
                    email_exists = True
                    break

            if email_exists:
                continue
            
            # Save account details & authorize access
            userdata += f"{email},{password}|"
            logineduser = email
            access_granted = True
            print("\n✅ Account Created Successfully!")

        
        case 3:
            print("\n" + "="*40)
            print("👋 Application closing... Goodbye!".center(40))
            print("="*40)
            break
            
        case _:
            print("\n⚠️  Invalid option selection. Choose 1, 2, or 3.")
            continue

    if access_granted:
        while True:
            print("\n" + "~"*40)
            print(f"📱 DASHBOARD | User: {logineduser}".center(40))
            print("~"*40)
            print("  1. 📝 Create Note")
            print("  2. 📖 Read Notes")
            print("  3. 🗑️  Delete Note")
            print("  4. ✏️  Edit Note")
            print("  5. 🚪 Logout")
            print("-"*40)
            
            sub_choice_input = input("👉 Enter your choice: ")
            if not sub_choice_input.isdigit():
                print("\n⚠️  Please enter a number.")
                continue
            sub_choice = int(sub_choice_input)
                
            match sub_choice:
                case 1:  # Create Note
                    title = input("\n🏷️  Enter The Note Title: ").strip().title()
                    notedata = input("🖊️  Enter The Note Content: ").strip()
                    
                    global_note_id += 1
                    noteswithtitle += f"{title},{notedata},{logineduser},{global_note_id}|"
                    
                    print("\n" + "-"*40)
                    print("🎉 Your Note Has Been Created!".center(40))
                    print(f"🆔 ID: {global_note_id}\n📌 Title: {title}\n📄 Content: {notedata}")
                    print("-"*40)

                case 2:  # Read Notes
                    datas = noteswithtitle.split("|")
                    has_notes = False
                    
                    print("\n" + "-"*50)
                    print(f"📖 YOUR SAVED NOTES".center(50))
                    print("-"*50)
                    print(f"{'ID':<6}{'TITLE':<15}{'CONTENT'}")
                    print("-"*50)
                    
                    for data in datas:
                        if not data.strip():
                            continue
                        parts = data.split(",")
                        if len(parts) == 4:
                            title, content, idd, notenum = parts
                            if idd == logineduser:
                                print(f"{notenum:<6}{title:<15}{content}")
                                has_notes = True
                    
                    if not has_notes:
                        print("🚫 No notes found. Create your first note!")
                    print("-"*50)

                case 3:  # Delete Note
                    datas = noteswithtitle.split("|")
                    target_input = input("\n🗑️  Enter the Note ID to delete: ")
                    if not target_input.isdigit():
                        print("⚠️  Invalid ID format.")
                        continue
                    target_id = int(target_input)
                        
                    noteswithtitle = ""
                    deleted = False
                    
                    for data in datas:
                        if not data.strip():
                            continue
                        parts = data.split(",")
                        if len(parts) == 4:
                            title, content, idd, notenum = parts
                            if idd == logineduser and int(notenum) == target_id:
                                print(f"\n🗑️  Removed: [{title}]")
                                deleted = True
                            else:
                                noteswithtitle += data + "|"
                                
                    if deleted:
                        print("✅ Note deleted successfully.")
                    else:
                        print("❌ Note ID not found or unauthorized.")

                case 4:  # Edit Note
                    target_input = input("\n✏️  Enter the Note ID you want to edit: ")
                    if not target_input.isdigit():
                        print("⚠️  Invalid ID format.")
                        continue
                    target_id = int(target_input)
                        
                    datas = noteswithtitle.split("|")
                    noteswithtitle = ""
                    updated = False
                    
                    for data in datas:
                        if not data.strip():
                            continue
                        parts = data.split(",")
                        if len(parts) == 4:
                            title, content, idd, notenum = parts
                            if idd == logineduser and int(notenum) == target_id:
                                print(f"\nEditing Note: {title}")
                                new_title = input("🏷️  New Title (Leave blank to keep): ").strip() or title
                                new_content = input("🖊️  New Content (Leave blank to keep): ").strip() or content
                                
                                noteswithtitle += f"{new_title.title()},{new_content},{logineduser},{notenum}|"
                                updated = True
                            else:
                                noteswithtitle += data + "|"
                                
                    if updated:
                        print("\n✅ Note updated successfully.")
                    else:
                        print("\n❌ Note ID not found or unauthorized.")

                case 5:  # Logout
                    print("\n👋 Logged out successfully!")
                    break
                case _:
                    print("\n⚠️  Invalid choice. Please select from options 1-5.")