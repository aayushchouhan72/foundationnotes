import mysql.connector
from rich import print
3
conn = mysql.connector.connect(
        host='localhost',
    port=3306,
    user='root',
    password='komal',
    database='exam'
    
)

if conn.is_connected():
    print("Connected to MySQL database")

# cursor = conn.cursor()

# # cursor.execute("CREATE TABLE bt19(id int primary key auto_increment,name varchar(20))")
# cursor.execute("INSERT INTO bt19(name) VALUES ( 'komal')")
# conn.commit()
# print("Table created table ")
# cursor.close()
# conn.close()


# try:
#       conn = mysql.connector.connect(
#          host='localhost',
#          port=3306,
#          user='root',
#          password='xyl',
#          database='exam'
#      )
#      if conn.is_connected():
#         print("Connected to MySQL database")
# except Exception as e:
#     print("Mysql probleam",e)

# finally:
#     print("my sql connection is done ..")



cur = conn.cursor(dictionary=True)
# cur.execute('select count(*) from emp')
# print(cur.fetchone())


# cur.execute('select sum(salary) from emp')
# print(cur.fetchone())


# cur.execute('select avg(salary) from emp')
# print(cur.fetchone())

# cur.execute('select max(salary) from emp')
# print(cur.fetchone())

# cur.execute('select min(salary) from emp')
# print(cur.fetchone())


# Primary key and foregin key 

# cur.execute('create table deps(d_id int primary key,d_name varchar(30))')
# cur.execute('create table emps(e_id int primary key ,e_name varchar(20),salary decimal(10,10),dep_id int ,constraint fk_emp_dep_id foreign key (dep_id) references deps(d_id))')

# cur.execute('desc deps')
# print(cur.fetchall())

# cur.execute('desc emps')
# print(cur.fetchall())


# # Joins 

# cur.execute("select * from emp join dep on dept_id=dep_id")
# print('JOIN \n',cur.fetchall())

# #  Right join 
# cur.execute("select * from emp left join dep on dept_id=dep_id")
# print('right JOIN \n',cur.fetchall())

# # Left join 
# cur.execute("select * from emp right join dep on dept_id=dep_id")
# print('left JOIN \n',cur.fetchall())

# #  self join 
# cur.execute("select * from emp self join dep on dept_id=dep_id")
# print('self JOIN \n',cur.fetchall())

# # inner join 
# cur.execute("select * from emp inner join dep on dept_id=dep_id")
# print('inner JOIN \n',cur.fetchall())


# Subquery 
# cur.execute("select * from emp where salary > all (select salary from emp where dept_id=(select dep_id from dep where dep_name='hr'))")
# print(cur.fetchall())

# cur.execute("select * from emp where salary<(select min(salary) from emp where dept_id=(select dep_id from dep where dep_name='sales'))")
# print(cur.fetchall())


# cur.execute("select * from emp where salary > all (select salary from emp where dept_id=(select dep_id from dep where dep_name='hr'))")
# print(cur.fetchall())



#  Bettween 
# query='select * from emp where salary between %s and %s'

# lis = [
#     (10000, 30000),
#     (20000, 30000),
#     (40000, 50000)
# ]

# for data in lis:
#     cur.execute(query, data)
#     result = cur.fetchall()
#     print(result)

#group by 

# cur.execute("select dept_id,count(*) from emp group by dept_id ")
# print(cur.fetchall())

# cur.execute("select dept_id,avg(salary) from emp group by dept_id")
# print(cur.fetchall())

# cur.execute("select dept_id,sum(salary) from emp group by dept_id")
# print(cur.fetchall())

# # Group by + having 

# cur.execute("select dept_id,count(*) from emp group by dept_id having  count(*)>2")
# print(cur.fetchall())

# cur.execute("select dept_id,avg(salary) from emp group by dept_id having  avg(salary)>29000")
# print(cur.fetchall())

# cur.execute("select dept_id,sum(salary) from emp group by dept_id having  sum(salary)>29000")
# print(cur.fetchall())











