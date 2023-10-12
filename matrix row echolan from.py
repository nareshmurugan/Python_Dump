a=int(input('ENTER A NUMBER OF THE ELEMENT a:''\t'))
b=int(input('ENTER A NUMBER OF THE ELEMENT b:''\t'))
c=int(input('ENTER A NUMBER OF THE ELEMENT c:''\t'))
d=int(input('ENTER A NUMBER OF THE ELEMENT d:''\t'))
e=int(input('ENTER A NUMBER OF THE ELEMENT e:''\t'))
f=int(input('ENTER A NUMBER OF THE ELEMENT f:''\t'))
g=int(input('ENTER A NUMBER OF THE ELEMENT g:''\t'))
h=int(input('ENTER A NUMBER OF THE ELEMENT h:''\t'))
i=int(input('ENTER A NUMBER OF THE ELEMENT i:''\t'))

if(d&g&h==0):
    print(list([a,b,c]))
    print(list([d,e,f]))
    print(list([g,h,i]),'\n')
if(d&e&g==0):
    print(list([a,b,c]))
    print(list([g,h,i]))
    print(list([d,e,f]),'\n')
# zero will be replaced
if(d|g==1):
            print(list([d,e,f]))
            print(list([g,h,i]))
            print(list([a,b,c]),'\n')

#1 will be changed to first row
else:
    print('HENCE WE FIND THE FIRST ROW ECHOLEN FORM')
    
x1=d-g
x2=e-h
x3=f-i

if(x1==1):
            print(list([x1,x2,x3]))
            print(list([a,b,c]))
            print(list([g,h,i]))
if(x1==0):
            print(list([a,b,c]))
            print(list([x1,x2,x3]))
            print(list([g,h,i]))
elif(x1&x2==0):
            print(list([a,b,c]))
            print(list([g,h,i]))
            print(list([x1,x2,x3]))
for i in range(1,10,1):
    if(g*i-x1==0):
            print(list([a,b,c]))
            print(list([g,h,i]))
            print(list([g*i,x1,x3]))
    else:
        print('\n')
