import sqlite3
connection=sqlite3.connect("Academy.db")
cursor=connection.cursor()
connection.execute("DELETE from student where Rollno='2'")
connection.commit()
print("TOTAL NUMBER OF ROWS DELETED:",connection.total_changes)
cursor=connection.execute("SELECT*FROM student")
for row in cursor:
    print(row)
connection.close()
