class MyStore:
    __prod_code=[]
    __prod_name=[]
    __cost_price=[]
    __prod_quant=[]

    def getdata(self):
        self.p=int(input("ENTR NO. OF PRODUCTS YOU NEED TO STORE:"))
        for x in range(self.p):
            self.__prod_code.append(int(input("ENTER PRODUCT CODE:")))
            self.__prod_name.append(str(input("ENTER PRODUCT NAME:"))) 
            self.__cost_price.append(int(input("ENTER COST PRICE:")))
    def display(self):
        print("STOCK IN STORES")
        print("-"*30)
        print("PRODUCT CODE \t PRODICT NAME \t COST PRICE")
        print("-"*30)
        for x in range(self.p):
            print(self.__prod_code[x],'\t\t',self.__prod_name[x],'\t\t',self.__cost_price[x])
        print("-"*30)
    def print_bill(self):
        total_price=0
        for x in range(self.p):
            q=int(input("ENTER THE QUATIFY FOR THE PRODUCT CODE%d:"%self.__prod_code[x]))
        self.__prod_quant.append(q)
        total_price=total_price+self.__cost_price[x]*self.__prod_quant[x]
        print("\t\tINVOICE RECEIPT")
        print("-"*30)
        print("PRODUCT CODE\t PRODUCT NAME \t COST PRICE\t QUANTITY \t TOTAL AMOUNT")
        print("-"*30)
        for x in range(self.p):
            print(self.__prod_code[x],'\t\t',self.__prod_name[x],'\t\t',
            self.__cost_price[x],'\t\t',self.__prod_quant[x],'\t\t',
            self.__prod_quant[x]*self.__cost_price[x])
            print("-"*30)
            print("\t\t\t\t\t\tTOTAL AMOUNT =",total_price)
S=MyStore()
S.getdata()
S.display()
S.print_bill()
                      
            
