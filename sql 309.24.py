import sqlite3
connection=sqlite3.connect("Academy.db")
cursor=connection.cursor()
cursor.execute("DROP TABLE person")
connection.execute("CREATE TABLE person(name,age,id)")
print("ENTER 5 STUDENTS NAMES")
who=[input()for i in range(1)]
print("ENTER THEIR AGES RESPECTIVELY:")
age=[int(input())for i in range(1)]
print("ENTER THIER IDS RESPECTIVELY:")
p_id=[int(input())for i in range(1)]
n=len(who)
for i in range(n):
    cursor.execute("insert into person values(?,?,?)",(who[i],age[i],p_id[i]))
    cursor.execute("select*from person")
print("DISPALYING ALL TH RECORDS FROM PERSON TABLE")
print(*cursor.fetchall(),sep='\n')

