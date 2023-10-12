class Item: 
    def __init__(self,name,price):
        self.name=name
        self.price=price
    def getname(self):
        return self.name
    def getprice(self):
        return self.price
class ShoppingCart:
    def __init__(self,items):
        self.items=items
        self.Cart=[]
    def total(self):
        total=0
        for _items in self.Cart:
            price=_items[1]
            total+=price
        return total
    def len(self):
        return len(self.Cart)
    def add(self,input_item):
        for items_ in items:
            if(items_.getname()==input_item[0]):
                self.Cart.append([items_.getname(),items_.getprice()])
n=int(input())
items=[]
for i in range(n):
    product=input().split()
    items.append(Item(product[0],int(product[1])))
q=int(input())
cart=ShoppingCart(items)
for jj in range(q):
    comandLine=input().split()
    comand,item=comandLine[0],comandLine[1:]
    if(comand=='total'):
        print(cart.total())
    elif(comand=='len'):
        print(cart.len())
    elif(comand=='add'):
        cart.add(item)
    else:
        raise ValueError

        
