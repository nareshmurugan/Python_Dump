import textwrap
def wrap(string, max_width):
    l=textwrap.wrap(string,max_width)
    i=0
    while(i<=len(l)):
        for i in l:
            if(i==len(l)):
                break
            print(i)
        break
if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)   
#string="alanturing"
#max_width=3    
