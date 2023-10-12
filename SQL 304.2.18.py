import sqlite3
connection=sqlite3.connect("Academy.db")
cursor=connection.cursor()
cursor.execute("SELECT COUNT(AVERAGE)FROM Student")
result=cursor.fetchall()
print(result)
