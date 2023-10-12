import sqlite3
connection=sqlite3.connect("Academy.db")
cursor=connection.cursor()
cursor.execute("SELECT*FROM student")
print("fetching all recods one by one:")
result=cursor.fetchone()
while result is not None:
    print(result)
    result=cursor.fetchone()
