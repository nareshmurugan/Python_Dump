def print_formatted(n):
    # your code goes here
     for i in range(1,n+1):
        print(i,format(i,'o'),format(i,'x'),format(i,'b'))
        i+=1
 
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
