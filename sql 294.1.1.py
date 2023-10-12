import sqlite3
connection=sqlite3.connect("Academy.db")
cursor=connection.cursor()
cursor.execute('DROP TABLE Student')
sql_command="""CREATE TABLE student(Rollno INTEGER PRIMARY KEY,Sname VARCHAR(20),Grade CHAR(1),gender CHAR(1),Average DECIMAL(5,2),birth_date DATE);"""
cursor.execute(sql_command)
sql_command="""INSERT INTO student(Rollno,Sname,Grade,gender,Average,birth_date)
    VALUES(NULL,"Akshay","B","M","87.8","2001-12-12");"""
cursor.execute(sql_command)
sql_command="""INSERT INTO student(Rollno,Sname,Grade,gender,Average,birth_date)
    VALUES(NULL,"Aravind","A","M","92.50","2000-08-17");"""
cursor.execute(sql_command)
connection.commit()
connection.close()
print("STUDENT TABLE CREATED")
