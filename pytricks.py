a=['aal','turing','aal','aarthi','hari']
b=['dfa','fafff','sf','fsaf','ffeee']
c=[1,3,4,5,3]
z=list(zip(a,c,b))
print(min(z,key=lambda y:y[0]))
print(max(a,key=a.count))
x,y,z=input().split()



