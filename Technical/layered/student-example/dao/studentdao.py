from model.student import Student
class Studentdao:
    def add_student(self,conn,data):
       cur = conn.cursor()
       cur.execute(
           "INSERT INTO student(rollno, name, age, marks) VALUES (%s, %s, %s, %s)",
           (data.roll, data.name, data.age, data.marks)
       )
       success = cur.rowcount > 0
       conn.commit()
       cur.close()
       return success
    def get_all_student(self,conn):
       cur = conn.cursor()
       cur.execute(
           "SELECT * FROM student"
       )
       users =[]
       rows = cur.fetchall()
       for  row in rows:
           users.append(Student(row[0],row[1],row[2],row[3]))
       conn.close()
       return users   
    def get_by_name(self,conn,name):
       cur = conn.cursor()
       cur.execute(
           "SELECT * FROM student where name like %s",
           ("%"+name+"%",)
       )
       users =[]
       rows = cur.fetchall()
       for  row in rows:
           users.append(Student(row[0],row[1],row[2],row[3]))
       cur.close()
       return users       
    def delete_by_name(self,conn,name):
       cur = conn.cursor()
       cur.execute(
           "DELETE FROM student where name = %s",
           (name,)
       )

       success = cur.rowcount > 0
       conn.commit()
       cur.close()
       return success
    def update_student(self,conn,data,roll):
       cur = conn.cursor()
       updata=(data.roll,data.name,data.age,data.marks,roll)
       cur.execute(
           "update student set rollno=%s,name=%s,age=%s,marks=%s where rollno= %s",
           updata
       )
       success = cur.rowcount > 0
       conn.commit()
       cur.close()
       return success