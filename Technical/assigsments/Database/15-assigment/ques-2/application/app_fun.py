class application_function:
    def add_dep(self,conn,data):
           cur = conn.cursor()
           cur.execute("Insert into  department_pdbc values(%s,%s,%s)",(data.did,data.dname,data.dlocation))
           conn.commit()
           cur.close()
           print("Department inserted successfully.")
    def add_emp(self,conn,data):
              cur = conn.cursor()
              cur.execute(
                     "INSERT INTO employee_pdbc "
                     "(emp_id, emp_name, salary, job_title, dept_id, manager_id) "
                     "VALUES (%s, %s, %s, %s, %s, %s)",
                     (data.eid, data.ename, data.esalary, data.etitle, data.edep, data.manager_id)
              )
              conn.commit()
              cur.close()
              print("Employee inserted successfully.")
    def display_emp_dep(self ,conn):
            cur = conn.cursor()
            cur.execute("""
SELECT e.* ,d. dept_name  from  employee_pdbc e join department_pdbc d on e.dept_id = d.dept_id
""") 
            rows = cur.fetchall()
            print("Emp ID  Employee Name  Job Title          Salary     Department")
            for row in rows :
                   print(f"{row[0]}\t\t{row[1]}\t\t{row[0]}\t\t{row[1]}\t\t{row[0]}")
            cur.close()
    def searchbyname(self,conn,name):
            cur = conn.cursor() 
            cur.execute('select * from employee_pdbc e where emp_name like %s',("%"+name+"%",))
            rows = cur.fetchall()
            print("Emp ID  Employee Name  Job Title          Salary     ")
            for row in rows :
                   print(f"{row[0]}\t\t{row[1]}\t\t{row[3]}\t\t{row[2]}")
            cur.close()
    def update_salary(self,conn,sal,id):
           cur =conn.cursor()
           cur.execute('update employee_pdbc set salary=%s where emp_id=%s',(sal,id))
           print("Salary Updated sucessfully >>")
           cur.close() 
    def update_dep(self,conn,newdep,id):
           cur =conn.cursor()
           cur.execute('update employee_pdbc set dept_id=%s where emp_id=%s',(newdep,id))
           print("dep Updated sucessfully >>")
           cur.close() 
    def delete_emp(self,conn,emp_id):
           cur =conn.cursor()
           cur.execute('delete from employee_pdbc  where emp_id=%s',(emp_id,))
           print("dep Updated sucessfully >>")
           cur.close()
    def dep_wiseemp_count(self,conn):
           cur = conn.cursor()
           cur.execute("""
SELECT  d.dept_name , count(*)from  employee_pdbc e join department_pdbc d on e.dept_id = d.dept_id group by d.dept_name
""") 
           rows = cur.fetchall()
           print("Department                Count")
           for row in rows :
                  print(f'{row[0]}\t\t\t {row[1]}')
           cur.close()

    def dep_wiseavg_sal(self,conn):
           cur = conn.cursor()
           cur.execute("""
SELECT  d.dept_name , avg(salary)from  employee_pdbc e join department_pdbc d on e.dept_id = d.dept_id group by d.dept_name
""") 
           rows = cur.fetchall()
           print("Department                salary ")
           for row in rows :
                  print(f'{row[0]}\t\t\t {row[1]}')
           cur.close()

    def emp_earn_more_avg_sal(self,conn):
           cur = conn.cursor()
           cur.execute("""
select e.* from employee_pdbc e where salary>(select avg(salary) from employee_pdbc)
""") 
           rows = cur.fetchall()
           for row in rows :
                  print(row)
           cur.close()
    def emp_sal_greter_then_own_dep(self,conn):
           cur =  conn.cursor()
           cur.execute("""
select e.emp_name,e.emp_name,d.dept_name,e.salary from employee_pdbc as e inner join department_pdbc as d on e.dept_id = d.dept_id where salary >(select avg(salary) from employee_pdbc)
""") 
           rows = cur.fetchall()
           for row in rows :
                  print(row)
           cur.close()
    def emp_it_display(self,conn):
           cur =  conn.cursor()
           cur.execute("""
select e.* from employee_pdbc  e where dept_id=(select dept_id from department_pdbc where dept_name='it')
""") 
           rows = cur.fetchall()
           for row in rows :
                  print(row)
           cur.close()
    def emp_count_1_display(self,conn):
           cur =  conn.cursor()
           cur.execute("""
select d.dept_name ,count(*) from employee_pdbc e join department_pdbc d on e.dept_id=d.dept_id group by d.dept_name having count(*)>1
""") 
           rows = cur.fetchall()
           for row in rows :
                  print(row)
           cur.close()
    def emp_with_manger(self,conn):
           cur =  conn.cursor()
           cur.execute("""
SELECT
    e.emp_name AS employee,
    m.emp_name AS manager
FROM employee_pdbc e
JOIN employee_pdbc m
    ON e.manager_id = m.emp_id;
""") 
           rows = cur.fetchall()
           for row in rows :
                  print(row)
           cur.close()  

    def dep_no_emp(self,conn):
           cur =  conn.cursor()
           cur.execute("""
select d.dept_name from department_pdbc d left join employee_pdbc e d.dept_id=e.dept_id
""") 
           rows = cur.fetchall()
           for row in rows :
                  print(row)
           cur.close()  
    def constraint():
           pass       
           