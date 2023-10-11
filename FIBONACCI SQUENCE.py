#1. START PROGRAMME.
def fibo(n):                # 2. 
    a=0                     # 3.
    b=1                     # 4. 
    while(a<n):             # 5.  
        print(a,end='\n')    # 6.  
        a,b=b,a+b           # 7.       
i=int(input("ENTER THE LIMIT OF FIBONACCI SQUENCE:\t"))# 8.
n=fibo(i)
print("THIS ARE THE FIBONACCI SEQUENCE  ")# 9. 
# 10. 


#ALGORITHM OF THE CODE 

# 1. START PROGRAMME.
# 2. creating a user defined fuction fibo(n) as a recursion fuction.
# 3. assigning a as 0.
# 4. assigning b as 1.
# 5. creating a while loop to limit the recursion size
#    if the condition is true go to line 6, 7, 8, 9 and 10 untitle the i is equal to n loop runs.
# 6. printing a.
# 7. assigning a as b and b as a+b.
# 8. getting input as i for the limit, go to the line (2-3-4-5-6-7-8-9 and again go to line 2 
#    for n times )funtion fibo() and run the loop as per the order of line in the bracket.
# 9. assigning n as the user defined recursive function,
#    returning the value n as fibonacci squence, printing the final ouput.
# 10. STOP PROGRAMME.
