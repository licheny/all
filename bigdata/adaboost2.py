from functools import reduce
import numpy as np
import math
#给出数据集
data=[(0,1),(1,1),(2,1),(3,-1),(4,-1),(5,-1),(6,1),(7,1),(8,1),(9,-1)]
#初始化权重
w=[]
for i in range(len(data)):
    w.append(1/len(data))
ft=[]
fun=[]
#进入T次迭代过程，在这里默认4次
for i in range(4):
    print("迭代次数：",i)
    #训练一个分类器
    minError=0
    minIndex=0
    Error=0
    for j in np.arange(0,10,0.5):
        #弱分类器由x<v或x>v产生
        for k in range(len(data)):
            if data[k][0]<=j and data[k][1]!=1:
                Error+=w[k]
            elif data[k][0]>j and data[k][1]!=-1:
                Error+=w[k]
            else:
                Error+=0
    #选取使总体误差值最小的阈值作为分类器即x<=v时f(x)=1;x>v时f(x)=-1作为分类器
        if j==0:
            minError=Error
            minIndex=0
        elif Error<minError:
            minError=Error
            minIndex=j
        else:
            pass
        # print("Error",Error)
        Error=0
    print("弱分类器","G(x)=1 if x<=",minIndex,"else -1")
    print("目前的分类误差率",minError)
    #计算当前分类器的系数
    aerfa=0.5*math.log((1-minError)/minError)
    fun.append(minIndex)
    ft.append(aerfa)
    #统计错误点个数
    errorCount=0
    correctCount=0
    for i in data:
        if (i[0]<=minIndex and i[1]==1) or (i[0]>minIndex and i[1]==-1):
            correctCount+=1
        else:
            errorCount+=1
    print("分错的个数",errorCount)
    #更新权值
    z=0
    #它使下一次的每一个权值成为一个概率分布
    for j in range(len(data)):
        gx=1 if data[j][0]<=minIndex else -1
        z+=w[j]*math.exp(-aerfa*data[j][1]*gx)
    for j in range(len(data)):
        gx=1 if data[j][0]<=minIndex else -1
        w[j]=w[j]/z*math.exp(-aerfa*data[j][1]*gx)

print("最终的分类器为：")
sFun="G(x)=sign["
for i in range(len(ft)):
    sFun=sFun+str("%.6f"%ft[i])+"G"+str(i+1)+"(x)"+ ("+" if i != len(ft)-1 else (""))
sFun+="]"
print(sFun)

num=0
for i in data:
    res=0
    for j in range(len(ft)):
        res+=ft[j]*(1 if i[0]<=fun[j] else -1)
    print(i,res)
    if (res>0 and i[1]==1) or (res<0 and i[1]==-1):
        num+=1
print(num)



    


        
        


