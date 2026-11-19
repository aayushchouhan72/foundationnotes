from database.connection import Database
from model.Employee import Employee

class Employeedao:
    def saveemployee(self,employee):
        print("DAO: saving employee")
        db = Database()
        connection=db.connect()
        cursor=connection.cursor()
        query="insert into dbemployee2(id,name,salary) values(%s,%s,%s)"
        values=(employee.id,employee.name,employee.salary)
        cursor.execute(query,values)
        connection.commit()
        print("emp saved successfully")
    def getallemployees(self):
        db = Database()
        connection=db.connect()
        cursor=connection.cursor()
        query="select id,name,salary from dbemployee2"
        cursor.execute(query)
        r=cursor.fetchall()
        employees=[]
        for i in r:
            employee=Employee(i[0],i[1],i[2])
            employees.append(employee)
        cursor.close()
        connection.close()
        return employees
    def getemployeebyid(self,id):
        db = Database()
        connection=db.connect()
        cursor=connection.cursor()
        query="select * from dbemployee2 where id=%s"
        cursor.execute(query,(id,))
        row=cursor.fetchone()
        cursor.close()
        connection.close()
        if row is not None:
            employee=Employee(row[0],row[1],row[2])
            return employee
        return None
    def update_employee(self,employee):
        db = Database()
        connection=db.connect()
        cursor=connection.cursor()
        query="update dbemployee2 set name=%s,salary=%s where id=%s"
        values=(employee.name,employee.salary,employee.id)
        cursor.execute(query,values)
        connection.commit()
        affectedrows=cursor.rowcount
        cursor.close()
        connection.close()
        return affectedrows
    def delete_employee(self,id):
        db = Database()
        connection=db.connect()
        cursor=connection.cursor()
        query="delete from dbemployee2 where id=%s"
        cursor.execute(query,(id,))
        connection.commit()
        affectedrows=cursor.rowcount
        cursor.close()
        connection.close()
        return affectedrows
    










    
