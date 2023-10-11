import csv 
with open('C:\\Users\\ELCOT\\Documents\\sample2.csv','r')as f:
    reader=csv.reader(f)
    for row in reader:
        print(row)
f.close()
        
