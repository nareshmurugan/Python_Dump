import sqlite3
connection=sqlite3.connect("Academy.db")
cursor=connection.cursor()
cursor.execute("SELECT * FROM Student")
print("fetchall:")
result=cursor.fetchall()
for r in result:
    print(r)
