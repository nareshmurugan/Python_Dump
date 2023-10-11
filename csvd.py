import csv
csv.register_dialect('myDialect',delimiter=',',quoting=csv.QUOTE_ALL,skipinitialspace=True)
F=open('C:\\Users\\ELCOT\\Documents\\sample2.csv','r')
reader=csv.reader(F,dialect='myDialect')
for col in reader:
    print(col[0],col[3])
F.close()
