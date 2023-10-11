import csv
csv.register_dialect('myDialect',delimiter=',',skipinitialspace=True)
F=open('D:\\PYTHON\\beautifulsoup.py','r')
reader=csv.reader(F,dialect='myDialect')
for row in reader:
    print(row)
F.close()
