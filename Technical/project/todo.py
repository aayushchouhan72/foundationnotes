userdata="ayush@gmail.com,ayush|demoapp@gmail.com,demo|" 

noteswithtitle = "Python,Basic language,ayush@gmail.com,1|Java,OOP language,ayush@gmail.com,2|HTML,Markup language,ayush@gmail.com,3|CSS,Styles web pages,ayush@gmail.com,4|SQL,Database language,ayush@gmail.com,5|"

logineduser=""
noteid=5
while True:
     print("....................  Wellcome to ToDo applications  .....................")
     print("1. login..\n2. Register..\n2. Exit ..")
     choice = int(input("Enter Your Choice ..."))
     match choice:
           #    Login user fuctionalty..
           case 1:
                email = input("Enter Your email :- ").lower().strip()
                pas = input("Enter your password :- ").strip()
                validemail=False
                uservalid=False
                #  Check valid email or not ...
                if "@gmail.com" in email or "@yahoo.com" in email:
                    validemail = True
                else:
                    print("Enter valid Email ...")
                    continue
                #  email and password match in data string ...
                data=userdata
                records= data.split("|")

                #  Loop to itrate over sting 
                for record in records:
                     if record == " " or record=="":
                           continue
                     useremail,userpass=record.split(",")
                     if useremail == email  and pas == userpass:
                            uservalid=True
                            logineduser=email
                            print("Logged in Sucessfully ✅ ✅ ✅")
                            break
                #  this block is only execute when the user is login ....
                if uservalid:
                    while True:
                        logineduser=email 
                        print("1.create note..\n2.read notes..\n3.delete note..\n4.edit note..\n5.Logout..")
                        choice = int(input("Enter your choice ..."))
                        match choice:
                        #  Create note ...
                         case 1:
                              title = input("Enter The Note Title :- ").strip().title()
                              notedata=  input("Enter The Note Data Here :- ").strip().title()
                              noteid+=1
                              data=f"{title},{notedata},{logineduser},{noteid}|"
                              noteswithtitle+=data
                              print("Your note is created :- ")
                              print(f"{noteid} :- {title} :- {notedata}")
                        #  To print all sotores notes in data stirng ...
                         case 2:
                              notes =  noteswithtitle
                              datas = notes.split("|")
                              flag=True
                              for data in datas:
                                   if data == " " or data == "":
                                        continue
                                   title,content,idd,notenum= data.split(",")
                                   if idd == logineduser:
                                        print(f"{notenum} :- {title} :- {content}")
                                        flag=False
                                   else:
                                        pass
                              if flag:
                                   print("There is not any note please create an note...")
                        #  Delete not functionality build from Here ....
                         case 3:
                               flag=True
                               notesexistflag=False
                               notes =  noteswithtitle
                               noteswithtitle=""
                               datas = notes.split("|")
                              #   first check not are there to delete or not ....
                               for data in datas:
                                   if data == " " or data == "":
                                        continue
                                   title,content,idd,notenum= data.split(",")
                                   if idd == logineduser:
                                        notesexistflag=True
                                        flag=False
                                   else:
                                        pass
                               if flag:
                                   print("There is not any note please create an note...")
                               
                               if notesexistflag:
                                       notid = int(input("Enter the note id to delete "))
                                       
                                       for data in datas:
                                          if data == " " or data == "":
                                               continue
                                          title,content,idd,notnum= data.split(",")
                                          if int(notnum) == notid:
                                              print(f"{notid} :- {title} :- {content}")
                                              flag=False
                                              continue 
                                          else:
                                               noteswithtitle += data+"|"
                                               
                                       if flag == False:
                                             print("Your not deleted sucessfully ✅✅")
                        #   Edit note functionality build from Here ...
                         case 4:
                               notid = int(input("Enter the note id which you wont to edit :- "))
                               notes =  noteswithtitle
                               noteswithtitle=""
                               datas = notes.split("|")
                               priin=""
                               for data in datas:
                                  if data == " " or data == "":
                                       continue
                                  title,content,idd,notnum= data.split(",")
                                  if int(notnum) == notid:
                                       title = input("Enter The Note Title :- ").strip()
                                       notedata=  input("Enter The Note Data Here :- ").strip()
                                       data= f"{title},{notedata},{logineduser},{notenum}"
                                       noteswithtitle+=data+"|"
                                  else:
                                       noteswithtitle += data+"|"
                               else:
                                    print("Note is updated successfully ✅✅...")        
                        #  Logout user functionality build from Here...
                         case 5:  
                              print("You are logged out successfully 😎😎😎...")
                              break
                         # default ...
                         case __:
                                  print("Enter vlaid choice ....😓😓😓")
                else:
                     print("Enter valid password and username❌❌❌ ...")
           #  New user register form here .... 
           case 2:
            loopbreakflag=None
            while True:   
               #   Flag to break the loop ... 
                if  loopbreakflag:
                     print("How are you ...")
                     break
                email = input("Enter Your email :- ").lower().strip()
                password = input("Enter your password :- ").strip()
                validemail=False
                uservalid=False
                # check email in data string ...
                isexistemail=False
               
                
                recs=userdata.split("|")
                
                for rec in recs: 
                    if rec == "" or rec == " ":
                        continue
                    idd,pas=rec.split(",")
                    if idd == email:
                         print("Email already exist ....")
                         isexistemail=True
                         break

                if isexistemail:
                     continue
                #  Check valid email or not ...
                if "@gmail.com" in email or "@yahoo.com" in email:
                    validemail = True
                else:
                    print("Enter valid Email ❌❌ ...")
                    continue
               #   Register the new user in data string ...
                data=f"{email},{password}|"
                userdata+=data
                uservalid=True
                print("Account Created Sucessfully ✅✅...\n")
                if uservalid:
                    while True:
                        logineduser=email 
                        print("1.create note..\n2.read notes..\n3.delete note..\n4.edit note..\n5.Logout..")
                        choice = int(input("Enter your choice ..."))
                        match choice:
                        #  Create note ...
                         case 1:
                              title = input("Enter The Note Title :- ").strip().title()
                              notedata=  input("Enter The Note Data Here :- ").strip().title()
                              noteid+=1
                              data=f"{title},{notedata},{logineduser},{noteid}|"
                              noteswithtitle+=data
                              print("Your note is created :- ")
                              print(f"{noteid} :- {title} :- {notedata}")
                        #  To print all sotores notes in data stirng ...
                         case 2:
                              notes =  noteswithtitle
                              datas = notes.split("|")
                              flag=True
                              for data in datas:
                                   if data == " " or data == "":
                                        continue
                                   title,content,idd,notenum= data.split(",")
                                   if idd == logineduser:
                                        print(f"{notenum} :- {title} :- {content}")
                                        flag=False
                                   else:
                                        pass
                              if flag:
                                   print("There is not any note please create an note...")
                        #  Delete not functionality build from Here ....
                         case 3:
                               flag=True
                               notesexistflag=False
                               notes =  noteswithtitle
                               noteswithtitle=""
                               datas = notes.split("|")
                              #   first check not are there to delete or not ....
                               for data in datas:
                                   if data == " " or data == "":
                                        continue
                                   title,content,idd,notenum= data.split(",")
                                   if idd == logineduser:
                                        notesexistflag=True
                                        flag=False
                                   else:
                                        pass
                               if flag:
                                   print("There is not any note please create an note...")
                               
                               if notesexistflag:
                                       notid = int(input("Enter the note id to delete "))
                                       
                                       for data in datas:
                                          if data == " " or data == "":
                                               continue
                                          title,content,idd,notnum= data.split(",")
                                          if int(notnum) == notid:
                                              print(f"{notenum} :- {title} :- {content}")
                                              flag=False
                                              continue 
                                          else:
                                               noteswithtitle += data+"|"
                                               
                                       if flag == False:
                                             print("Your not deleted sucessfully ✅✅") 
                        #   Edit note functionality build from Here ...
                         case 4:
                               notid = int(input("Enter the note id which you wont to edit :- "))
                               notes =  noteswithtitle
                               noteswithtitle=""
                               datas = notes.split("|")
                               priin=""
                               for data in datas:
                                  if data == " " or data == "":
                                       continue
                                  title,content,idd,notnum= data.split(",")
                                  if int(notnum) == notid:
                                       title = input("Enter The Note Title :- ").strip()
                                       notedata=  input("Enter The Note Data Here :- ").strip()
                                       data= f"{title},{notedata},{logineduser},{notenum}"
                                       noteswithtitle+=data+"|"
                                  else:
                                       noteswithtitle += data+"|"
                               else:
                                    print("Note is updated successfully ✅✅...")        
                        #  Logout user functionality build from Here...
                         case 5:  
                              print("You are logged out successfully 😎😎😎...")
                              loopbreakflag=True
                              break
                else:
                     print("Enter valid password and username❌❌❌ ...")
          # Application closing code ...   
           case 3:
                 print("Thankyou for using application 😊😊")
                 print("Aplication closing ....")
                 break
           case __:
                  print("Enter valid Choice to User application")
