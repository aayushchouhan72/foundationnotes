# 3.
# =========================================
# WEBSITE VISITOR TRACKING SYSTEM
# =========================================

# A website stores unique visitor IDs.

# Menu:
# 1. Add Visitor
# 2. Remove Visitor
# 3. Check Visitor
# 4. Display All Visitors
# 5. Count Unique Visitors
# 6. Clear Visitor Data
# 7. Exit

# Requirements:
# - Use a set to store visitor IDs.
# - Duplicate visitor IDs should not be stored.
# - Use add(), remove(), and memwhobership operations.

visitors=set()
while True:
    print("1. Add Visitor\n2. Remove Visitor\n3. Check Visitor\n4. Display All Visitors\n5. Count Unique Visitors\n6. Clear Visitor Data\n7. Exit")
    choice = input("Enter the your choice")
    match choice:
       case "1":
            visitors.add(int(input("Enter the visitor id add")))
       case "2":
            visitors.discard(int(input("Enter the visitor id remove")))
       case "3":
            print("All visitor till now",visitors)
       case "4":
              print("All visitor till now",visitors)     
       case "5":
              print("Count Unique Visitors",len(visitors))
       case "6":
              visitors.clear()
       case "7":
            break