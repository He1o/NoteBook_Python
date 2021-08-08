import numpy as np
import matplotlib.pyplot as plt
import time
from contextlib import contextmanager

@contextmanager
def timer(name):
    start = time.time()
    yield
    end = time.time()
    print('{} COST:{:.10f}'.format(name, end - start))

class KMeans():
    def __init__(self, pointsEnemy, num_centro = 3):
        self.pointsEnemy = np.array(pointsEnemy)
        self.num_enemy, self.num_feature = self.pointsEnemy.shape
        self.num_centro = num_centro

    def distEclud(self, x, y):
        return np.sqrt(np.sum((x-y)**2))  

    def randCent(self):
        centroids = np.zeros((self.num_centro, self.num_feature))
        for i in range(self.num_centro):
            index = int(np.random.uniform(0, self.num_enemy)) #
            centroids[i, :] = self.pointsEnemy[index, :] 
        return centroids

    def KMeans(self):
        best_mean = np.inf
        for _ in range(20):
            clusterChange = True
            clusterAssment = np.zeros((self.num_enemy, 2))
            centroids = self.randCent()
            
            while clusterChange:
                clusterChange = False
                for i in range(self.num_enemy):
                    minDist = np.inf
                    minIndex = -1
                    for j in range(self.num_centro):
                        distance = self.distEclud(centroids[j,:],self.pointsEnemy[i,:])
                        if distance < minDist:
                            minDist = distance
                            minIndex = j
                    if clusterAssment[i,0] != minIndex:
                        clusterChange = True
                    clusterAssment[i,:] = minIndex,minDist
                for j in range(self.num_centro):
                    ptsInClust = self.pointsEnemy[np.nonzero(clusterAssment[:, 0] == j)[0]]  
                    if len(ptsInClust):
                        centroids[j, :] = np.mean(ptsInClust, axis=0)  
                if np.sum(clusterAssment[:, 1]) < best_mean:
                    best_cluster = clusterAssment
                    best_centrod = np.unique(centroids)
                    best_mean = np.sum(clusterAssment[:, 1])
        return best_centrod, best_cluster

    def showCluster(self, centroids, clusterAssment):
        plt.ion()
        plt.clf()
        m,n = self.pointsEnemy.shape
        if n != 2:
            print("数据不是二维的")
            return 1
    
        mark = ['or', 'ob', 'og', 'ok', '^r', '+r', 'sr', 'dr', '<r', 'pr']
        if self.num_centro > len(mark):
            print("k值太大了")
            return 1
    
        # 绘制所有的样本
        for i in range(m):
            markIndex = int(clusterAssment[i,0])
            plt.plot(self.pointsEnemy[i,0],self.pointsEnemy[i,1],mark[markIndex])
    
        mark = ['Dr', 'Db', 'Dg', 'Dk', '^b', '+b', 'sb', 'db', '<b', 'pb']
        # 绘制质心
        for i in range(self.num_centro):
            plt.plot(centroids[i,0],centroids[i,1],mark[i])
        plt.pause(0.01)


with timer('Astar'):
    pointsEnemy = np.array([[78,88], [4,5], [77,44], [66,55], [8, 76], [3,5]])
    K = KMeans(pointsEnemy)
    centroids, clusterAssment = K.KMeans()
for _ in range(10):
    K.showCluster(centroids, clusterAssment)
print(centroids,clusterAssment)