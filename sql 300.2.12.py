import sqlite3
connection=sqlite3.connect("Academy.db")
cursor=connection.cursor()
cursor.execute("SELECT Rollno,sname FROM student order BY sname")
result=cursor.fetchall()
print(*result,sep="\n")
