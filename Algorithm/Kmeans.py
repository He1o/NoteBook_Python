import numpy as np
import matplotlib.pyplot as plt
 
# 加载数据
def loadDataSet(fileName):
    data = np.array([[78,88], [4,5], [77,44], [66,55], [8, 76], [3,5]])
    return data
 
# 欧氏距离计算
def distEclud(x,y):
    return np.sqrt(np.sum((x-y)**2))  # 计算欧氏距离
# 为给定数据集构建一个包含K个随机质心的集合
def randCent(dataSet,k):
    m,n = dataSet.shape
    centroids = np.zeros((k,n))
    # for i in range(k):
    #     index = int(np.random.uniform(0,m)) #
    #     centroids[i,:] = dataSet[index,:]
    for j in range(n):  #特征逐个逐个地分配给这k个簇心。每个特征的取值需要设置在数据集的范围内
        minJ = min(dataSet[:, j])   #数据集中该特征的最小值
        rangeJ = float(max(dataSet[:, j]) - minJ)   #数据集中该特征的跨度
        centroids[:, j] = (minJ + rangeJ * np.random.rand(k, 1)).reshape(1,3)[0]   #为k个簇心分配第j个特征，范围需限定在数据集内。
        # centroids[0, j] = minJ
        # centroids[1, j] = minJ + rangeJ/2
        # centroids[2, j] = minJ + rangeJ
    return centroids
 
# k均值聚类
def KMeans(dataSet,k):
    best_mean = np.inf
    for _ in range(10):
        m = np.shape(dataSet)[0]  #行的数目
        # 第一列存样本属于哪一簇
        # 第二列存样本的到簇的中心点的误差
        clusterAssment = np.mat(np.zeros((m,2)))
        clusterChange = True
    
        # 第1步 初始化centroids
        centroids = randCent(dataSet,k)

        while clusterChange:
            clusterChange = False
    
            # 遍历所有的样本（行数）
            for i in range(m):
                minDist = np.inf
                minIndex = -1
    
                # 遍历所有的质心
                #第2步 找出最近的质心
                for j in range(k):
                    # 计算该样本到质心的欧式距离
                    distance = distEclud(centroids[j,:],dataSet[i,:])
                    if distance < minDist:
                        minDist = distance
                        minIndex = j
                # 第 3 步：更新每一行样本所属的簇
                if clusterAssment[i,0] != minIndex:
                    clusterChange = True
                    clusterAssment[i,:] = minIndex,minDist
            #第 4 步：更新质心
            for j in range(k):
                # pointsInCluster = dataSet[np.nonzero(clusterAssment[:,0].A == j)[0]]  # 获取簇类所有的点
                dis = np.inf
                for idx in np.nonzero(clusterAssment[:,0].A == j)[0]:
                    if clusterAssment[idx, 1] < dis:
                        dis = clusterAssment[idx, 1]
                        min_idx = idx
                # centroids[j,:] = np.mean(pointsInCluster,axis=0)   # 对矩阵的行求均值
                if dis != np.inf:
                    centroids[j,:] = dataSet[min_idx] # 对矩阵的行求均值
                else:
                    centroids[j,:] = dataSet[int(np.random.uniform(0,m)),:]
            print(centroids)
            print(clusterAssment)
            if np.sum(clusterAssment[:, 1]) < best_mean:
                best_cluster = clusterAssment
                best_centrod = centroids
                best_mean = np.sum(clusterAssment[:, 1])
        
        
    return best_centrod, best_cluster
 
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