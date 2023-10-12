import sqlite3
connection=sqlite3.connect("Academy.db")
cursor=connection.cursor()
cursor.execute("SELECT * FROM Student where grade<>'A' and Grade<>'B'")
result=cursor.fetchall()
print(*result,sep="\n")
