import time
s=time.time()
arr=[81,94,11,96,12,35,17,95,28,58]
n = len(arr)
for i in range(n):
    for j in range(0, n-i-1):
        if arr[j] > arr[j+1] :
            arr[j], arr[j+1] = arr[j+1], arr[j]
e=time.time()
print(e-s)
