#1
n=int(input("How many terms?"))  #2
a1,b2=0,1                        #3 
count = 0                        #4               
if (n<= 0):                      #5
   print("Please enter a positive integer")  #6
elif (n == 1):                   #7
   print("Fibonacci sequence upto",n,":")#8
   print(b2)                     #9
else:                            #10   
   print("Fibonacci sequence:")  #11
   while (count < n):            #12
       print(a1)                 #13
       nth = a1 + b2             #14   
       a1 = b2                   #15
       b2 = nth                  #16
       count += 1                #17
#18

# ALGORITHM of the Program to display the Fibonacci sequence

# 1. START PROGRAMME.
# 2. get the input n to the limit sequence. 
# 3. assigning a1 as 0,  assigning b1 as 1.
# 4. assigning the cout = 0.
# 5. if condition n<=0 is true go to the line 6 and 18.
# 6. print please enter a positive integer.  
# 7. elif condition (n==1) is work when if condition is false and go to line 8, 9 and 18.
# 8. print "Fibonacci sequence upto",n.
# 9. print b2.
# 10. else both the codition if and elif is not true go to line 11 and 18. 
# 11. print Fibonacci sequence.
# 12. creating a while loop to limit the recursion size and itreate
#     is condition is true go to line 13,14,15,16,17 and 18 until the condition true.
# 13. print a1
# 14. assigning nth=a1+b2
# 15. a1=b2 changing the value
# 16. b2=nth updating value
# 17. count+=1 itreating the loop by the count
# 18. STOP PROGRAMME

