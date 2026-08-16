
# 2.
# =========================================
# ONLINE COURSE ENROLLMENT SYSTEM
# =========================================

# An institute offers:
# 1. Python Course
# 2. Java Course

# Store enrolled student email IDs using sets.

# Menu:
# 1. Enroll Student in Python
# 2. Enroll Student in Java
# 3. Display Python Students
# 4. Display Java Students
# 5. Find Students Enrolled in Both Courses
# 6. Find Students Enrolled Only in Python
# 7. Find Students Enrolled Only in Java
# 8. Check Enrollment in Python Course
# 9. Display Total Unique Students
# 10. Exit

# Requirements:
# - Use two sets.
# - Use membership operator (in).
# - Use union, intersection and difference operations.


python= set(map(int,input("student enrole for python").split()))
java= set(map(int,input("student enrole for java").split()))

print(python,java,sep="\n")

print(f"Student are in both course {python&java}")

print(f"Students Only in python course{python-java}")

print(f"Students Only in java course {java-python}")

name = input("Enter the student id to check enrollment ...")
course =  input("Enter the course name >>>")

if name in python and course.lower() == "python":
    print("Your allready enrolled in this course python ...")
elif name in java and course.lower() ==  "java":
    print("Your allready enrolled in this course java ...")
else:
     print("Not enrolled in any kind of course ...")

print(f"Display Total Unique students ... {set(list(java)+list(python))}")


