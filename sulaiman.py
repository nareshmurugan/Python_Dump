class Item:
    def __init__(self,name,price):
        self.name=name
    	self.price=price
    def getname(self):
        return self.name
    def getprice(self):
        return self.price
n=int(input())
l=[]
for i in range(n):
    l.append(input().split())
    
