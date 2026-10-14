class  Employee:
    def __init__(self,eid,ename,esalary,edep):
         self.employee_id=eid
         self.employe_name=ename
         self.salary=esalary
         self.department=edep
    @classmethod
    def display_employe(cls,employe_list):
         for employe in employe_list:
             print(f"{ employe.employee_id,employe.employe_name ,employe.salary,employe.department}")
    @classmethod
    def display_employe_greter_40000(cls,employe_list):
         for employe in employe_list:
             if employe.salary>40000:
                      print(f"{ employe.employee_id,employe.employe_name ,employe.salary,employe.department}")
    @classmethod
    def display_employe_it_dep(cls,employe_list):
         for employe in employe_list:
             if employe.department=='it':
                      print(f"{ employe.employee_id,employe.employe_name ,employe.salary,employe.department}")
    @classmethod
    def highest_salary_employe(cls,employe_list):
         maxmark=employe_list[0].salary
         st=0
         for employe in employe_list:
             if employe.salary>maxmark:
                    st=employe
         employe=st
         print(f"{ employe.employee_id,employe.employe_name ,employe.salary,employe.department}")
    @classmethod
    def sum_of_employe_salary(cls,employe_list):
         sum=0
         for employe in employe_list:
             sum+=employe.salary
         return sum
    @classmethod
    def average_salary_of_employe(cls,employe_list):
         sum=0
         for employe in employe_list:
             sum+=employe.salary
         return sum/len(employe_list)

  
 
         
         
         
