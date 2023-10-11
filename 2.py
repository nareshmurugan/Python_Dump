n=15
def fizzBuzz(n):
    # Write your code here
     i=0  
     while(i<n):
         print("alan") if (n%3==0 and n%5==0) else print(n)
         print("alan") if (n%3==0) else print(n)
         print("alan") if (n%5==0) else print(n)
         break
if __name__ == '__main__':
    fizzBuzz(n)
