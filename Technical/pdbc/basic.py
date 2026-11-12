import mysql.connector


conn = mysql.connector.connect(
        host='localhost',
    port=3306,
    user='root',
    password='komal',
    database='exam'
)

if conn.is_connected():
    print("Connected to MySQL database")

cursor = conn.cursor()

# cursor.execute("CREATE TABLE bt19(id int primary key auto_increment,name varchar(20))")
cursor.execute("INSERT INTO bt19(name) VALUES ( 'komal')")
conn.commit()
print("Table created table ")
cursor.close()
conn.close()


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
