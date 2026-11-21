from DAO.employeedao import Employeedao


class EmployeeService:
    def addemployee(self,employee):
        if employee.id<=0:
            print("employee id must be positive")
            return 
        if employee.name.strip()=="":
            print("name cant be empty")
            return 
        print("service: processing employee")
        dao = Employeedao()
        dao.saveemployee(employee)

    def displayallemployees(self):
        dao = Employeedao()
        employees = dao.getallemployees()
        if not employees:
            print("no employee found")
            return 
        for employee in employees:
            print("ID is:",employee.id)
            print("Name is",employee.name)
            print("salary is:",employee.salary)

    def search_employee(self, employee_id):
        dao = Employeedao()
        employee = dao.getemployeebyid(employee_id)
        if employee is None:
            print("no employee found with that ID")
            return
        print("ID is:", employee.id)
        print("Name is:", employee.name)
        print("salary is:", employee.salary)

    def modify_employee(self, employee):
        if employee.name.strip() == "":
            print("employee name can not be empty")
            return
        dao = Employeedao()
        affectedrows = dao.update_employee(employee)
        if affectedrows > 0:
            print("employee updated successfully")
        else:
            print("employee not found")

    def remove_employee(self, employee_id):
        dao = Employeedao()
        affectedrows = dao.delete_employee(employee_id)
        if affectedrows > 0:
            print("employee deleted successfully")
        else:
            print("employee not found")
            
