'''M11=int(input('enter the value of m11'))
M12=int(input('enter the value of m12'))
M21=int(input('enter the value of m13'))
M22=int(input('enter the value of m14'))
'''
import numpy as n
arr=n.array([[1,2,3],[3,4,6],[-7,3,-9]])
def cofactor(a):
    def cofactor1(a):
        x=arr[1][1]*arr[2][2]
        y=-(arr[2][1]*arr[1][2])
        return x+y
    def cofactor2(a):
        x=arr[0][0]*arr[2][2]
        y=-(arr[2][0]*arr[0][2])
        return x+y
    def cofactor3(a):
        x=arr[0][0]*arr[1][1]
        y=-(arr[1][0]*arr[0][1])
        return x+y
    return cofactor1(a)+cofactor2(a)+cofactor3(a)
print(cofactor(arr))
'''
2 3 4
5 6 7
8 9 2
#cofact of m11
m11 m12
m21 m22
#cofact of m22
m00 m02
m20 m22
#cofact of m33
m00 m01
m10 m11
'''
#to print a array total elements
'''
 for i in range(len(g)):
	for j in range(len(g[i])):
		print(g[i][j])
'''
