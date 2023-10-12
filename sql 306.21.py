import sqlite3
connection=sqlite3.connect("Academy.db")
cursor=connection.cursor()
print("DISPALYING THE HIGHEST AVERAGE ")
cursor.execute("SELECT sname,max(AVERAGE)FROM student")
result=cursor.fetchall()
print(result)
print("DISPLAYING THE NAME OF THE LEAST AVERAGE")
cursor.execute("SELECT sname,min(AVERAGE)FROM student")
result=cursor.fetchall()
print(result)


