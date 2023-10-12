l=input().split()
#n=l[0]
#mne=l[1]
#print(n,mne)
neOfArr=input().split()
eOfA=set(input().split())
eOfB=set(input().split())
l=0
happiness=0
for i in neOfArr:
    if(i in eOfA):
        happiness+=1
for i in neOfArr:
    if(i in eOfB):
        happiness-=1
print(happiness)

        



