import csv
inFile=('C:\\Users\\ELCOT\\Documents\\sample2.csv')
f=open(inFile,'r')
reader=csv.reader(f)
next(reader)
arrayValue=[]
a=int(input("ENTER THE COLUMN NUMBER W TO 3:-"))
for row in reader:
    arrayValue.append(row[a])
    arrayValue.sort()
for row in arrayValue:
    print(row)
f.close()
