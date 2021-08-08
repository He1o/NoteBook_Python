import numpy as np
import matplotlib.pyplot as plt
 
# 加载数据
def loadDataSet(fileName):
    data = np.mat([[2,3], [4,5], [4,5], [77,44], [66,55], [8, 76], [3,5]])
    return data
 
def distEclud(vecA, vecB):      #计算欧式距离
    return np.sqrt(sum(np.power(np.array(vecA)[0] - np.array(vecB)[0], 2)))  # la.norm(vecA-vecB)

def randCent(dataSet, k):         #  初始化k个随机簇心
    n = np.shape(dataSet)[1]       #特征个数
    centroids = np.mat(np.zeros((k, n)))  # 簇心矩阵k*n
    for j in range(n):  #特征逐个逐个地分配给这k个簇心。每个特征的取值需要设置在数据集的范围内
        minJ = min(dataSet[:, j])   #数据集中该特征的最小值
        rangeJ = float(max(dataSet[:, j]) - minJ)   #数据集中该特征的跨度
        centroids[:, j] = np.mat(minJ + rangeJ * np.random.rand(k, 1))    #为k个簇心分配第j个特征，范围需限定在数据集内。
    return centroids        #返回k个簇心

def KMeans(dataSet, k, distMeas=distEclud, createCent=randCent):
    m = np.shape(dataSet)[0]    #数据个数
    clusterAssment = np.mat(np.zeros((m, 2)))  # 记录每个数据点被分配到的簇，以及到簇心的距离
    centroids = createCent(dataSet, k)      #  初始化k个随机簇心
    clusterChanged = True       #  记录一轮中是否有数据点的归属出现变化，如果没有则算法结束
    while clusterChanged:
        clusterChanged = False
        for i in range(m):  # 枚举每个数据点，重新分配其簇归属
            minDist = np.inf; minIndex = -1    #记录最近簇心及其距离
            for j in range(k):      #枚举每个簇心
                distJI = distMeas(centroids[j, :], dataSet[i, :])   #计算数据点与簇心的距离
                if distJI < minDist:        #更新最近簇心
                    minDist = distJI;  minIndex = j
            if clusterAssment[i, 0] != minIndex: clusterChanged = True  #更新“变化”记录
            clusterAssment[i, :] = minIndex, minDist ** 2     #更新数据点的簇归属
        # print (centroids)
        for cent in range(k):  #枚举每个簇心，更新其位置
            ptsInClust = dataSet[np.nonzero(clusterAssment[:, 0].A == cent)[0]]  # 得到该簇所有的数据点
            centroids[cent, :] = np.mean(ptsInClust, axis=0)  # 将数据点的均值作为簇心的位置
    return centroids, clusterAssment    # 返回簇心及每个数据点的簇归属


def showCluster(dataSet,k,centroids,clusterAssment):
    m,n = dataSet.shape
    if n != 2:
        print("数据不是二维的")
        return 1
 
    mark = ['or', 'ob', 'og', 'ok', '^r', '+r', 'sr', 'dr', '<r', 'pr']
    if k > len(mark):
        print("k值太大了")
        return 1
 
    # 绘制所有的样本
    for i in range(m):
        markIndex = int(clusterAssment[i,0])
        plt.plot(dataSet[i,0],dataSet[i,1],mark[markIndex])
 
    mark = ['Dr', 'Db', 'Dg', 'Dk', '^b', '+b', 'sb', 'db', '<b', 'pb']
    # 绘制质心
    for i in range(k):
        plt.plot(centroids[i,0],centroids[i,1],mark[i])
 
    plt.show()
dataSet = loadDataSet("test.txt")
k = 3
centroids,clusterAssment = KMeans(dataSet,k)
 
showCluster(dataSet,k,centroids,clusterAssment)