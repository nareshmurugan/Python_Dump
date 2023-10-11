import csv
# other way of declaring the filename
l={'England_data': 'D:/PYTHON/England.csv','Scotland_data': 'D:/PYTHON/Scotland.csv'
,'NorthernIreland_data': 'D:/PYTHON/Northern Ireland.csv','Wales_data': 'D:/PYTHON/Wales.csv'}
pathfor i in enumerate(l):
    F=open(i,'r')
reader = csv.reader(F)
# declaring array
arrayValue = []
# displaying the content of the list
for row in reader:
    arrayValue.append(row)
    print(row)
F.close()
#a=[l[3] for l in l]
