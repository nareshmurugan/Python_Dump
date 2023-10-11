import matplotlib.pyplot as plt
import mpl_toolkits
from mpl_toolkits.mplot3d import Axes3D
fig=plt.figure()
ax=fig.add_subplot(111,projection='3d')
x=[1,2,3]
y=[5,6,2]
z=[3,2,3]
ax.scatter(x,y,z,c='r',marker='o')
ax.set_xlabel('X Label')
ax.set_xlabel('Y Label')
ax.set_xlabel('Z Label')
plt.show()
