access = input("Enter the Membership status :- ")
bookissue = int(input("Enter the number of book is issued"))

if access == "yes":
     if bookissue < 3:
           print("Entry is allowed book will be issued")
     else:
          print("Maximum book issue limit  is reached ")
else:
   print("Invalid access ")
     