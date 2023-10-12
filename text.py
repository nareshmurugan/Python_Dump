import textwrap
def wrap(string, max_width):
    l=[]
    c=0
    for i in range(0,len(string),max_width):
        aa=string[c:i]
        c+=i
        l.append(aa)
        
    return l
    for i in l:
        print(i,'\n')
    
    
if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)   
#string="alanturing"
#max_width=3    
