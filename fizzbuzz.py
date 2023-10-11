def fuck(i):
    if(i%3==0 and i%5==0):
        print('FizzBuzz')
    elif(i%3==0 and i%5!=0):
        print('Fizz')
    elif(i%5==0 and i%3!=0):
        print('Buzz')
    else:
        print(i)

a=int(input())
for j in range(1,a+1):
    fuck(j)
