# import time

# t1=time.clock()
# time.sleep(5)
# t2=time.clock()
# print(t1)
# print(t2)
# print(t2-t1)
import time
import math
import numpy as np
import struct
# x = [i * 0.001 for i in range(1000000)]
# start = time.clock()
# for i, t in enumerate(x):
#     x[i] = math.sin(t)
# print ("math.sin:", time.clock() - start)

# x = [i * 0.001 for i in range(1000000)]
# x = np.array(x)
# start = time.clock()
# np.sin(x,x)
# print ("numpy.sin:", time.clock() - start)

# a = np.matrix([[1,2,3],[5,5,6],[7,9,9]])
# print(a*a**-1)

# a=np.fromfile("1demo_2016051112_03_05_400_0_0_XX_5.mix", dtype=np.float32)
# print(a)

a=open("1demo_2016051112_03_05_400_0_0_XX_5.mix","rb")
# print(float(a.read(1)))
while True:
    temp=a.read(1)
    if len(temp)!=0:
        b=struct.unpack("B",temp)
        if(b[0]!=0):
            print(b)
    else:
        break
a.close()