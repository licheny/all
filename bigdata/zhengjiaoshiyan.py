import itertools
from collections import namedtuple

points=[]
# print(isinstance(p, aaa))
# 生成在三维坐标系中的27个点
for i in range(0,3):
    for j in range(0,3):
        for k in range(0,3):
            points.append((i,j,k))

#在27个点中任意选出9个点，生成列表
points=list(itertools.combinations(points,9))
print(points[0:5])
print(len(points))


# point=[(1,2,3),(4,5,6),(7,8,9)]
# point=list(itertools.combinations(point,2))
# print(point)
