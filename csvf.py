import csv
csvData=[['student','age'],['dhanush','17'],['kalyani','18'],['ram','15']]
with open('C:\\Users\\ELCOT\\Documents\\sample5.csv','w')as CF:
    writer=csv.writer(CF)
    writer.writerows(csvData)
CF.close()
