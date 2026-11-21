from dao.studentdao import Studentdao
class Studentservice:
    def __init__(self):
        self.daoobj=Studentdao()
    def add_student(self,conn,data):
        if (data.age>0 or 0<=data.marks<=100):
             return "Invalid Age or marks "
        if not( data.name and  data.age and data.marks and data.roll):
            return "All field are required "
        if self.daoobj.add_student(conn,data):
            return "User is added sucessfully ✅"
    def get_all_student(self,conn):
         student=self.daoobj.get_all_student(conn)
         if student:
             for stu in student:
                 print(f"""
Roll Number :- {stu.roll}
Name        :- {stu.name}
Age         :- {stu.age}
Marks       :- {stu.marks}

""")
             return "Required Student data"   
         else:
             return "Users not found"
    def get_by_name(self,conn,name):
         student=self.daoobj.get_by_name(conn,name)
         if student:
             for stu in student:
                 print(f"""
Roll Number :- {stu.roll}
Name        :- {stu.name}
Age         :- {stu.age}
Marks       :- {stu.marks}

""")
             return "Required Student data"   
         else:
             return "Users not found"
    def delete_by_name(self,conn,name):
        if not name.strip():
            return "Enter Valid Name .."
        if self.daoobj.delete_by_name(conn,name):
             return "User is delted sucessfully"
        else:
            return "User is not found or other probleam"
    def update_student(self,conn,user,roll):
        if not roll:
            return "Roll number is required ..."

        if self.daoobj.update_student(conn,user,roll):
            return "User is updated sucessfully ..."
        else:
            return "user updating probleam"