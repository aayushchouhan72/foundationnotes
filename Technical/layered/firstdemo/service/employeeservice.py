from dao.employeedao import Employeedao
class employeeservice():
    def addemployee(self,employee):
        print("Service : processing employee request")
        dao = Employeedao()
        dao.saveemployee(employee)