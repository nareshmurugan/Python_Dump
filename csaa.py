import csv
csv.register_dialect('myDialect',delimiter=',',quoting=csv.QUOTE_ALL,skipinitialspace=True)
F=open('C:\\Users\\ELCOT\\Documents\\quotes.csv','r')
reader=csv.reader(F,dialect='myDialect')
for row in reader:
    print(row)
F.close()
