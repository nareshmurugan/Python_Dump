import csv
with open('C:\\Users\\ELCOT\\Documents\\sample 1.csv','w')as f:
    w=csv.writer(f)
    n=1
    while(n<=10):
        name=input("player name?:")
        score=int(input("score:"))
        w.writerow([name,score])
        n+=1
    print("player file created")
    f.close()
    searchname=input("enter the name to be searched")
    f=open('C:\\Users\\ELCOT\\Documents\\sample 1.csv','r')
    reader=csv.reader(f)
    lst=[]
    for row in reader:
        lst.append(row)
    q=0
    for row in lst:
        if searchname in row:
            print(row)
            q+=1
    if(q==0):
        print("string not found")
    f.close()
    

                   
