import numpy as np
import matplotlib.pyplot as plt
 
def loadDataSet(fileName):
    data = np.array([[78,88], [4,5], [77,44], [66,55], [8, 76], [3,5]])
    return data

def distEclud(x, y):
    return np.sqrt(np.sum((x-y)**2))  

def randCent(dataSet,k):
    m,n = dataSet.shape
    centroids = np.zeros((k,n))
    for i in range(k):
        index = int(np.random.uniform(0,m)) #
        centroids[i,:] = dataSet[index,:] 
    return centroids

def KMeans(dataSet,k):
    best_mean = np.inf
    for _ in range(20):
        clusterChange = True
        m = np.shape(dataSet)[0]
        clusterAssment = np.zeros((m,2))
        centroids = randCent(dataSet,k)
        
        while clusterChange:
            clusterChange = False
            for i in range(m):
                minDist = np.inf
                minIndex = -1
                for j in range(k):
                    distance = distEclud(centroids[j,:],dataSet[i,:])
                    if distance < minDist:
                        minDist = distance
                        minIndex = j
                if clusterAssment[i,0] != minIndex:
                    clusterChange = True
                clusterAssment[i,:] = minIndex,minDist
            for j in range(k):
                ptsInClust = dataSet[np.nonzero(clusterAssment[:, 0] == j)[0]]  
                centroids[j, :] = np.mean(ptsInClust, axis=0)  
            
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
