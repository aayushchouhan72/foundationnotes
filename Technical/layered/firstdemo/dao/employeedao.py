from database.connection import Database
class Employeedao:
    def saveemployee(self,employee):
        print("Getting data ")
        print("id",employee.id)
        print("name",employee.name)
        print("salary",employee.salary)
        db=Database()
        conn=db.connect()
        cursor =  conn.cursor()
        query='insert into dbemp(id,name,salary) values (%s,%s,%s)'
        cursor.execute(query,(employee.id,employee.name,employee.salary))
