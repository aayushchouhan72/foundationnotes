import mysql.connector
class Database:   
    def connectdb(self):
         print("Connecting database .....")
         return mysql.connector.connect(
              host='localhost',
              port=3306,
              user ="root",
              password='ayush',
              database='assigment_pdbc'
    
         )
    def disconnectdb(self,conn):
         print("Disconnecting database ...")
         conn.close()
         