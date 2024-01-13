import mysql.connector

mydb=mysql.connector.connect(host="localhost", user="root", password="123456789", database="library")
c=mydb.cursor()
c.execute("select * from books")
for r in c:
    print(r)