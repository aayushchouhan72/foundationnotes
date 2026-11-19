from model.student import Student
from database.connet import Database
from service.studentservice import Studentservice
conn= Database()
stu=Studentservice()
db=conn.connectdb()
while True:
    try:
        print("""
1. To add an student
2. Get All students
3. Get By Name
4. Delete By Name
5. Update  Student

""")
        choice = int(input("Enter the choice"))
        match choice:
            case 1:
                roll=int(input("Enter the roll number :-"))
                name=input("Enter the name :-").strip()
                age= int(input("Enter the age :-"))
                marks=float(input('Enter the marks :- '))
                user =  Student(roll,name,age,marks)
                print(stu.add_student(db,user))
            case 2:
                print(stu.get_all_student(db))
            case 3:
                name = input("Enter the name :- ")
                stu.get_by_name(db,name)
            case 4:
                name = input("Enter the name :- ")
                print(stu.delete_by_name(db,name))
            case 5:
                roll=int(input("Enter the roll number :-"))
                name=input("Enter the name :-").strip()
                age= int(input("Enter the age :-"))
                marks=float(input('Enter the marks :- '))
                user =  Student(roll,name,age,marks)
                print(stu.update_student(db,user,roll))
            case 6:
                db.close()
                print("Thankyou for using an application")
                break
            case _:
                print("Enter valid choice ")
    except Exception as e:
        print("Exception:- ",e)



