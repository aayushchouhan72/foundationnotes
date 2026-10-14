# 1.
# =========================================
# STUDENT CLUB MEMBERSHIP SYSTEM
# =========================================

# A college has two clubs:
# 1. Coding Club
# 2. Robotics Club

# Store student IDs of both clubs using sets.

# Menu:
# 1. Add Student to Coding Club
# 2. Add Student to Robotics Club
# 3. Display Students in Coding Club
# 4. Display Students in Robotics Club
# 5. Find Students in Both Clubs
# 6. Find Students Only in Coding Club
# 7. Find Students Only in Robotics Club
# 8. Display All Unique Club Members
# 9. Display Total Unique Club Members
# 10. Exit

# Requirements:
# - Use two sets.
# - Apply intersection, difference, and union operations.

set1= set(map(int,input("Enter the student for coding clube").split()))
set2= set(map(int,input("Enter the student for Robotics clube").split()))

print(set1,set2,sep="\n")

print(f"Student are in both clubs {set1&set2}")

print(f"Students Only in Coding Club {set1-set2}")

print(f"Students Only in Robotics Club {set2-set1}")

print(f"Display All Unique Club Members {set(list(set1)+list(set2))}")

print(f"Display Total Unique Club Members {len(set1)+len(set2)}")

