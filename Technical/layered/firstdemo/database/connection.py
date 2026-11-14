import mysql.connector
class Database:
    def connect(self):
         conn =  mysql.connector.connect(
              host='localhost',
              port=3306,
              user='root',
              password='ayush',
              database='layerarch'
         ) 
         return conn

               