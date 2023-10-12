#stack in list
l=[]
def push(a):
    l.append(a)
def pop():
    p=l.pop(-1)
    return p
def view():
    print("Stack elements are: \n")
    for i in l:
        print(i,end='\t')
    print('\n')    
while(True):
    P=len(l)
    print("STACK OPERATIONS".center(50,'#'))
    print("\n1. PUSH\n2. POP\n3. VIEW\n4. QUIT\n")
    ch=int(input("Choose the operation to perform:    "))
    print('\n')
    if(ch==1):
        if(P==5):
            print("STACK IS OVERFLOW".center(30,'#'),'\n')
        else:
            a=int(input("Enter the element to push:   "))
            push(a)
    elif(ch==2):
        if(P==0):
            print("STACK IS UNDERFLOW".center(30,'#'),'\n')
        else:
            print("The poped element is",pop())
    elif(ch==3):
        if(P!=0):
            view()
        else:
            print("STACK IS EMPTY".center(30,'#'),'\n')
    elif(ch==4):
        print("End of the program")
        break
    else:
        print("Invalid program")
