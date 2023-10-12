marks=[]
subjects=['tamil','english','physics','chemistry','computer.science','maths']
for i in range(6):
    m=int(input("ENTER MARK="))
    marks.append(m)
for j in range(len(marks)):
    print("{}.{} mark={}".format(j+1,subjects[j],marks[j]))
print("TOTAL ,MARKS=",sum(marks))
 
