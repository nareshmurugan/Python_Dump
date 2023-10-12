import sqlite3
connection=sqlite3.connect("Academy.db")
cursor=connection.cursor()
connection.execute("UPDATE Student SET sname ='Priyanka' where Rollno='6'")
connection.commit()
print("TOTAL NUMBER OF ROWS UPDATED:",connection.total_changes)
cursor=connection.execute("SELECT*FROM student")
for row in cursor:
    print(row)
connection.close()
