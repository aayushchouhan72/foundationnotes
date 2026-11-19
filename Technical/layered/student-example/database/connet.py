import mysql.connector as con

class Database:
    def connectdb(self):
        return con.connect(
            host='localhost',
            port=3306,
            user='root',
            password='ayush',
            database='exam'
        )
    