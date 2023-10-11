class sample:
    num=0
    def __init__(self,var):
        sample.num+=1
        self.var=var
        print("the object value is =",var)
        print("the count of object created=",sample.num)
        
s1=sample(15)
s2=sample(35)
s3=sample(45)
