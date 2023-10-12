def minion_game(s): 
    n = len(s);  
    #For holding all the formed substrings  
    arr = [];  
    #This loop maintains the starting character  
    for i in range(0,n):  
        #This loop will add a character to start character one by one till the end is reached  
        for j in range(i,n):
            arr.append(s[i:(j+1)]);  
    #Prints all the subset    
    v=list('aeiou'.upper())
    stuart=0
    kevin=0
    for j in arr:
        if(j[0] in v):
            kevin+=1
        if(j[0] not in v):
            stuart+=1
    if(stuart>kevin):
        print('Stuart {}'.format(stuart))
    elif(stuart<kevin):
        print('Kevin {}'.format(kevin))
    else:
        print('Draw')
if __name__ == '__main__':
    s = input()
    minion_game(s)
