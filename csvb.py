import csv

csv.register_dialect('myDialect',delimiter='|')
with open('C:\\Users\\ELCOT\\Documents\\sample1.csv','r')as F:
    reader=csv.reader(F,dialect='myDialect')
for row in reader:
    print(row)
F.open()
