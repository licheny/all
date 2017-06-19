import numpy as np
from matplotlib.pyplot import *
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
# a=[1,2,3,4,5]
# print(a[::2])

# print(np.arange(0, 60, 10).reshape(-1,1))

# print(np.arange(0, 6))

# a=np.arange(0, 60, 10).reshape(-1,1)+np.arange(0, 6)
# print(a)

# print(a[::,::])
# a=np.array([[1,2,3],[4,5,6],[7,8,9]])
# a=np.array(([1,2,3],[4,5,6],[7,8,9]))
# a=np.array([(1,2,3),(4,5,6),(7,8,9)])
# b=np.diff(a)
# # print(b)
# # print(a[:-1,:-1])
# # print(a[0::-1,0::-1])
# # print(a)
# # a.flat[1:3]=100
# # print(a.flat[1:3]=100)
# # print(a)
# c=a[:,:-1]
# d=b/c
# print(np.std(d))
# print(np.var(d))
# print(b/a)
# print(np.ravel(np.where(a>5)))
# c=np.zeros(5)
# print(c)
# a=np.arange(0,6).reshape(2,3)
# b=np.arange(0,6).reshape(2,3)
# c=np.add.outer(a,b)
# print(c)
# print(a)
# b=([1,1,1])
# c=np.convolve(b,a)
# print(c[2:-2])
# a.flat=2
# print(a)

# def fun1(a,b,c,d,e):
#     a=1
#     b=2
#     c=[1,1]
#     d="hello1"
#     e.append(1)


# a=0
# b=0
# c=[0,0]
# d="hello"
# e=[0,0]
# fun1(a,b,c,d,e)
# print(a,b,c,d,e)

# a=1
# b=-1
# c=1
# aa=[1,1]
# bb=[1,1]
# print(a^b)
# print(a^c)
# print(np.bitwise_xor(a,b),np.bitwise_xor(a,c))
# print((a XOR b))
# print((a XOR c))
# print(id(a),id(b),id(c))
# print(id(aa),id(bb))

# a=np.array([1,2])
# a=np.diag(a)
# print(a)
# print(a-1)
# print(a)
# b=np.all((a-1)<=1)
# print(b)
# a=[1,2,3]
# print(a.min(),a.max())
# cash=np.zeros(10000)
# cash[0]=1000
# outcome=np.random.binomial(9,0.5,size=len(cash))

# for i in range(1,len(cash)):
#     if outcome[i]<5:
#         cash[i]=cash[i-1]-1
#     elif outcome[i]<10:
#         cash[i]=cash[i-1]+1

# print(outcome.min(),outcome.max())

# plot(np.arange(len(cash)),cash)
# show()
# for i in range(1,10):
#     print(i) 

# a=np.mat("1 2;3 4")
# print(a)
# b=np.mat("1 2;3 4")
# print(b)
# a=np.array([[1,2],[3,4]])
# print(a)
# b=np.array([[1,2],[3,4]])
# print(b)
# print(a*b)
# a=np.array([1,2,3,4]).astype(float)
# print(a)
# b=[1,2,3,4]
# plot(a,b)
# xlabel("x")
# ylabel("y(x)")
# show()
# fun=np.poly1d(a)
# print(fun)
# fun2=fun.deriv(m=1)
# print(fun2)
# x=np.arange(1,10)
# y=fun(x)
# y1=fun2(x)
# plot(x,y,"ro",x,y1,"g--")
# xlabel("x")
# ylabel("y")
# show()
# a=[1,2,3,4]
# b=[1,2,3,4]
# hist(a,b)
# show()

a=[1,2,3,4]
b=[2,3,4,5]
c=[4,3,2,1]
# fig=figure()
# ax=fig.add_subplot(311)
# ax.plot(a,b)
# ax=fig.add_subplot(312)
# ax.plot(a,b)
# ax=fig.add_subplot(313)
# ax.plot(a,b)
# show()

# fig=figure()
# ax=fig.add_subplot(111)
# ax.scatter(a,b,s=1000)
# plot(a,b)
# ax.plot(a,c)
# ax.grid(True)
# ax.set_title("hello")
# show()
# a=np.linspace(-1,1,100)
# b=np.linspace(-1,1,100)
# a,b=np.meshgrid(a,b)
# print(a,b)
a=[1,2,3]
b=[1,2,3]
a,b=np.meshgrid(a,b)
z=np.power(a,2)+np.power(b,2)
print(z)
fig=figure()
ax=fig.add_subplot(111,projection="3d")
ax.plot_surface(a,b,z,rstride=4,cstride=4)
show()