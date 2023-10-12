def rev(str1):
    str2=''
    i=len(str1)-1
    for i in range(len(str1)):
        str2+=str1[i]
        i+=1
        return str2
word=input("\n ENTER A STRING:")
print("\n THE MIRROR IMAGE OF THE GIVEN STRING IS :",rev(word))
