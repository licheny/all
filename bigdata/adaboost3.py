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
signFun=[]
#进入T次迭代过程，在这里默认4次
for i in range(3):
    print("迭代次数：",i)
    #训练一个分类器
    minError=0
    minIndex=0 
    # gloabSign=1
    for j in np.arange(0,10,0.5):
        Error=0
        Error1=0
        Error2=0
        #弱分类器由x<v或x>v产生
        for k in range(len(data)):
            if data[k][0]<=j and data[k][1]!=1:
                Error1+=w[k]
            elif data[k][0]>j and data[k][1]!=-1:
                Error1+=w[k]
            else:
                Error1+=0
        for k in range(len(data)):
            if data[k][0]<=j and data[k][1]!=-1:
                Error2+=w[k]
            elif data[k][0]>j and data[k][1]!=1:
                Error2+=w[k]
            else:
                Error2+=0
        if Error1<Error2:
            Error=Error1
            sign=1
        else:
            Error=Error2
            sign=2
    #选取使总体误差值最小的阈值作为分类器即x<=v时f(x)=1;x>v时f(x)=-1或者x<=v时f(x)=-1;x>v时f(x)=1作为分类器
        if j==0:
            minError=Error
            minIndex=0
            gloabSign=sign   
        elif Error<minError:
            minError=Error
            minIndex=j
            gloabSign=sign
        else:
            pass
        # print("Error",Error)
    if gloabSign==1:
        print("弱分类器","G(x)=1 if x<=",minIndex,"else -1")
    else:
        print("弱分类器","G(x)=-1 if x<=",minIndex,"else 1")
    print("目前的分类误差率",minError)
    signFun.append(gloabSign)
    #计算当前分类器的系数
    aerfa=0.5*math.log((1-minError)/minError)
    fun.append(minIndex)
    ft.append(aerfa)
    #统计错误点个数
    errorCount=0
    correctCount=0
    for i in data:
        if(gloabSign==1):
            if (i[0]<=minIndex and i[1]==1) or (i[0]>minIndex and i[1]==-1):
                correctCount+=1
            else:
                errorCount+=1
        else:
            if (i[0]<=minIndex and i[1]==-1) or (i[0]>minIndex and i[1]==1):
                correctCount+=1
            else:
                errorCount+=1
    print("分错的个数",errorCount)
    #更新权值
    z=0
    #它使下一次的每一个权值成为一个概率分布
    if(gloabSign==1):
        for j in range(len(data)):
            gx=1 if data[j][0]<=minIndex else -1
            z+=w[j]*math.exp(-aerfa*data[j][1]*gx)
    else:
        for j in range(len(data)):
            gx=-1 if data[j][0]<=minIndex else 1
            z+=w[j]*math.exp(-aerfa*data[j][1]*gx)
    if(gloabSign==1):
        for j in range(len(data)):
            gx=1 if data[j][0]<=minIndex else -1
            w[j]=w[j]/z*math.exp(-aerfa*data[j][1]*gx)
    else:
        for j in range(len(data)):
            gx=-1 if data[j][0]<=minIndex else 1
            w[j]=w[j]/z*math.exp(-aerfa*data[j][1]*gx)
    print("各数据项的权值",w)
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
        if(signFun[j]==1):
            res+=ft[j]*(1 if i[0]<=fun[j] else -1)
        else:
            res+=ft[j]*(-1 if i[0]<=fun[j] else 1)
    print(i,"G(x)=",res)
    if (res>0 and i[1]==1) or (res<0 and i[1]==-1):
        num+=1
print("最终错误个数:",10-num)



    


        
        


