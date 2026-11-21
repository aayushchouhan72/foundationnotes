import mysql.connector
class Database:
    def connect(self):
        connection=mysql.connector.connect(host="localhost",port=3307,user="root",password="Kapil@123",database="batch19")
        return   connection
        