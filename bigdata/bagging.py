from functools import reduce
import numpy as np
import math
import random

#根据采样数据生成使当前错误率最小的分类器
def classifier_fun(data):
    #每个数据都有一样的权重，即1/n
    weight=1/len(data)
    #记录最小的误差率和阈值
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
                Error1+=weight
            elif data[k][0]>j and data[k][1]!=-1:
                Error1+=weight
            else:
                Error1+=0
        for k in range(len(data)):
            if data[k][0]<=j and data[k][1]!=-1:
                Error2+=weight
            elif data[k][0]>j and data[k][1]!=1:
                Error2+=weight
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
    return minError,minIndex,gloabSign


#data为训练数据集，count为训练次数，默认为5次
def bagging_fun(data,count=5):
    simpleDatas=[]
    classifierList=[]
    for i in range(count):
        #假定每次抽取出6个样本进行训练
        sampleData=random.sample(data,6)
        print("数据集为：",sampleData)
        simpleDatas.append(sampleData)
        #选取使总体误差值最小的阈值作为分类器即x<=v时f(x)=1;x>v时f(x)=-1或者x<=v时f(x)=-1;x>v时f(x)=1作为分类器
        minError,minIndex,gloabSign=classifier_fun(sampleData)
        classifierList.append((minIndex,gloabSign))
        if gloabSign==1:
            print("弱分类器"+str(i+1),"G(x)=1 if x<=",minIndex,"else -1")
        else:
            print("弱分类器"+str(i+1),"G(x)=-1 if x<=",minIndex,"else 1")
        print("目前的分类误差率",minError)
        errorCount=0
        correctCount=0
        for j in sampleData:
            if(gloabSign==1):
                if (j[0]<=minIndex and j[1]==1) or (j[0]>minIndex and j[1]==-1):
                    correctCount+=1
                else:
                    errorCount+=1
            else:
                if (j[0]<=minIndex and j[1]==-1) or (j[0]>minIndex and j[1]==1):
                    correctCount+=1
                else:
                    errorCount+=1
        print("在当前抽样出来的数据上分错的个数",errorCount)
    print("最终的分类器为：")
    for i in range(len(classifierList)):
        if(classifierList[i][1]==1):
            print("第"+str(i+1)+"个分类器为","G(x)=1 if x<=",classifierList[i][0],"else -1")
        else:
            print("第"+str(i+1)+"个分类器为","G(x)=-1 if x<=",classifierList[i][0],"else 1")
    return classifierList


if __name__=="__main__":
    #给出数据集
    data=[(0,1),(1,1),(2,1),(3,-1),(4,-1),(5,-1),(6,1),(7,1),(8,1),(9,-1)]
    #count代表迭代次数，即抽取样本的次数
    count=7
    classifiers=bagging_fun(data,count)
    #将分类器用于所有数据
    #分类结果依据所有分类结果中，占比例最大的结果
    #correctNum代表分类正确的个数
    correctNum=0
    for i in data:
        num=0
        for j in classifiers:
            if j[1]==1:
                if (i[0]<=j[0] and i[1]==1) or (i[0]>j[0] and i[1]==-1):
                    num+=1
            else:
                if (i[0]<=j[0] and i[1]==-1) or (i[0]>j[0] and i[1]==1):
                    num+=1
        if num>count-num:
            correctNum+=1
    print("最终分类错误的点的个数为：",10-correctNum)

