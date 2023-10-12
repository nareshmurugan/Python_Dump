import sqlite3
connection=sqlite3.connect("Academy.db")
cursor=connection.cursor()
cursor.execute("SELECT Rollno,sname FROM Student WHERE(Birth_date>='2001-01-01' AND Birth_date<='2001-12-01')")
result=cursor.fetchall()
print(*result,sep="\n")
