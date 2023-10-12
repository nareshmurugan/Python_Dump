import sqlite3
connection=sqlite3.connect("Academy.db")
cursor=connection.cursor()
cursor.execute("SELECT * FROM Student")
ans=cursor.fetchmany()
for i in ans:
    print(i)
