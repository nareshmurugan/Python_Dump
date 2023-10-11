n=int(input())
def fizzBuzz(n):
    # Write your code here
    for i in range(1,n+1):
        print("FrizzBuzz") if (i%3==0 and i%5==0) else print('Frizz') if(i%3==0) else print('Buzz') if (i%5==0) else print(i)
if __name__ == '__main__':
    fizzBuzz(n)
