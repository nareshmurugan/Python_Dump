class sample:
    num=0
    def __init__(self,var):
        sample.num+=1
        self.var=var
        print("the object value is =",var)
        print("the value of class variable is =",sample.num)
    def __del__(self):
        sample.num-=1
        print("object with vallie %d is exit from the scope "%self.var)
s1=sample(15)
s2=sample(35)
s3=sample(45)
