n=set([x for x in range(1,16)]) 
def fizzBuzz(n):
    # Write your code here
    for i in n:
        print("alan") if (i%3==0 and i%5==0) or (i%3==0) or  (i%5==0) else print(i)
if __name__ == '__main__':
    fizzBuzz(n)
