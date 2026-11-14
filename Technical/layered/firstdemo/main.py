from service.employeeservice import employeeservice
from model.employee import Employee
emp = Employee(101,'deepika',9000)
print("Wellcome")
service = employeeservice()
service.addemployee(emp)