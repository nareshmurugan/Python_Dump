class library:
    def __init__(self):
        self.bookname=""
        self.author=""

    def getdata(self):
        self.bookname =input("enter name of the book:")
        self.author =input("enter author of the book:")

    def dispay(self):
        print("name of the book:",self.bookname) 
        print("author of the book:",self.author)
        print("\n")

    book=[]
    ch='y'
    while(ch=='y'):
            print("1.add new book \n 2.dispaly books")
            resp=int(input("enter your choice:"))

        if(resp==1):
            l=library()
        l.getdata()
        book.append(l)
    elif(resp==2):
        for x in book:
            x.display()
    else:
        print("invalid input......")
    ch = input("do you want continue......")
