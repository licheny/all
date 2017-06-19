from functools import reduce
import numpy as np
import math
#给出数据集
data=[(0,1),(1,1),(2,1),(3,0),(4,0),(5,0),(6,1),(7,1),(8,1),(9,0)]
#初始化权重
negativeCount=0
positiveCount=0
for i in data:
    if i[1]==1:
        positiveCount+=1
    else:
        negativeCount+=1
w=[]
for i in data:
    if(i[1]==1):
        w.append(1/(2*positiveCount))
    else:
        w.append(1/(2*negativeCount))
#进入T次迭代过程，在这里默认5次
ft=[]
fun=[]
for i in range(5):
    print("round：",i)
    #1.初始化权重
    wsum=reduce(lambda x,y:x+y,w)
    for j in range(len(w)):
        w[j]=w[j]/wsum
    print("w",w)
    #2.训练一个分类器
    minError=0
    minIndex=0
    Error=0
    t=[0.5,1.5,2.5,3.5,4.5,6.5,7.5,8.5,9.5]
    # np.arange(0,10,0.5)
    for j in t:
        #弱分类器由x<v或x>v产生
        for k in range(len(data)):
            if data[k][0]<j and data[k][1]!=0:
                Error+=w[k]
            elif data[k][0]>j and data[k][1]!=1:
                Error+=w[k]
            else:
                Error+=0
    #3.选取使总体误差值最小的阈值作为分类器即x<v时f(x)=0;x>v时f(x)=1作为分类器
        if j==0.5:
            minError=Error
            minIndex=0.5
        elif Error<minError:
            minError=Error
            minIndex=j
        else:
            pass
        # print("Error",Error)
        Error=0
    print("v",minIndex)
    print("minError",minError)
    #4.更新权值
    fun.append(minIndex)
    ft.append(math.log(1/(minError/(1-minError))))
    errorCount=0
    correctCount=0
    for j in range(len(data)):
        if (data[j][0]<minIndex and data[j][1]==0) or (data[j][0]>minIndex and data[j][1]==1):
            correctCount+=1
            w[j]=w[j]*(minError/(1-minError))
        else:
            errorCount+=1
            w[j]=w[j]
    print("Error count",errorCount)

correctFinal=0
sum2=0
for i in ft:
    sum2+=i
for i in data:
    sum1=0
    for j in range(5):
        if i[0]>fun[j]:
            sum1+=ft[j]
    if (sum1>=sum2 and i[1]==1) or (sum1<sum2 and i[1]==0):
        correctFinal+=1
print("correctFinal",correctFinal)

    


        
        


