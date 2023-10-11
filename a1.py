import csv
England_data= 'D:/PYTHON/England.csv';Scotland_data= 'D:/PYTHON/Scotland.csv'
NorthernIreland_data= 'D:/PYTHON/Northern Ireland.csv';Wales_data= 'D:/PYTHON/Wales.csv'
Files=['D:/PYTHON/England.csv','D:/PYTHON/Scotland.csv','D:/PYTHON/Northern Ireland.csv','D:/PYTHON/Wales.csv']
for i in Files:
    with open(i,'r')as f:
        reader=csv.reader(f)
        for row in reader:
            print(row)
f.close()

