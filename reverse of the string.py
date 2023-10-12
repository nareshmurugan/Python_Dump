word=input("ENTER A STRING")
def rev(str1):
    str2=""
    i=len(str1)-1
    while(i>=0):
        str2=str2+str1[i]
        i-=1
    return str2
print("THE REVERSE OF THE STRING IS ",rev(word))
