import sqlite3
connection=sqlite3.connect("Academy.db")
cursor=connection.cursor()
cursor.execute("SELECT * FROM student")
print("fetching firt 3 records:")
result=cursor.fetchmany(3)
print(result)
