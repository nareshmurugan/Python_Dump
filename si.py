fname=input("Enter file name:")
with open(fname,'r')as f:
    for line in f:
        words=line.split()
        for i in words:
            for letter in i:
                if(letter.isdigit()):
                    print(letter)
for char in fname(file_char," "):
    if char==" ":
        count+=1
print("No of blank spaces:",count)
