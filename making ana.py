from collections import Counter as c
a,b=input(),input()
print(sum(((c(a)-c(b)).values()))+sum(((c(b)-c(a)).values())))
