items=[]
prod=1
for i in range(5):
    print("ENTER PRICE FOR ITEM []:".format(i+1))
    p=int(input())
    items.append(p)
for j in range(len(items)):
    print("price for item []=Rs.[]".format(j+1,items[j]))
    prod*=items[j]
print("sum of all prices=Rs.",sum(items))
print("product of all prices=Rs.",prod)
print("average of all prices Rs.",sum(items)/len(items))
