l=[]
lo=[1,2,3,4,5]
while True:
    for i in lo:
        for j in range(10):
            l.append([i,j])
    l=lo
    break
        
