from service.employeeservice import EmployeeService
from model.Employee import Employee

print("welcome to our software")
service= EmployeeService()
while True:
    print("1.Add Employee")
    print("2.Display All employees")
    print("3.Search employee by ID")
    print("4.Update Employee")
    print("5.Delete Employee")
    print("6.Exit")
    try:
        choice = int(input("enter your choice:"))
    except ValueError:
        print("please enter a number")
        continue
    if choice==1:
        try:
            eid = int(input("enter id:"))
            name = input("enter name:")
            salary = float(input("enter salary:"))
        except ValueError:
            print("please enter a valid numeric ID and salary")
            continue
        employee=Employee(eid,name,salary)
        service.addemployee(employee)
    elif choice==2:
        service.displayallemployees()
    
    elif choice==6:
        print("Application Close")
        break
    elif choice==3:
        try:
            eid = int(input("enter Id to search: "))
        except ValueError:
            print("please enter a valid employee ID")
            continue
        service.search_employee(eid)
    elif choice==4:
        try:
            eid = int(input("enter id: "))
            name = input("enter name: ")
            salary = float(input("enter salary: "))
        except ValueError:
            print("please enter a valid numeric ID and salary")
            continue
        employee = Employee(eid, name, salary)
        service.modify_employee(employee)
    elif choice==5:
        try:
            eid = int(input("enter id to delete: "))
        except ValueError:
            print("please enter a valid employee ID")
            continue
        service.remove_employee(eid)
        


    else:
        print("invalid choice")




