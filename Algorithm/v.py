import numpy as np
from matplotlib import tri 
from scipy.linalg import solve
from matplotlib.patches import Circle
import matplotlib.pyplot as plt


class voronoi():
    def __init__(self, point_start, point_end, points_enemy):
        self.p_start = [point_start]
        self.p_end = [point_end]
        self.p_enemy = points_enemy
        self.p_num = len(points_enemy) + 2
        self.points = np.array(self.p_start + self.p_enemy + self.p_end)
        self.x_tri = self.points[:,0]
        self.y_tri = self.points[:,1]


    #画圆
    def draw_circle(self, x, y, r, ax):
        ax = ax.gca()
        cir = Circle(xy=(x, y), radius=r, alpha=0.5)
        ax.add_patch(cir)
        ax.plot()

    #画三角形
    def plot_triangle(self, A, B, C):
        x = [A[0], B[0], C[0], A[0]]
        y = [A[1], B[1], C[1], A[1]]

        ax = plt.gca()
        ax.plot(x, y, linewidth=2)

    #获取外接圆圆心坐标、半径
    def get_outer_circle(self, A, B, C):
        xa, ya = A[0], A[1]
        xb, yb = B[0], B[1]
        xc, yc = C[0], C[1]
        # 两条边的中点
        x1, y1 = (xa + xb) / 2.0, (ya + yb) / 2.0
        x2, y2 = (xb + xc) / 2.0, (yb + yc) / 2.0
        # 两条线的斜率
        ka = (yb - ya) / (xb - xa) if xb != xa else None
        kb = (yc - yb) / (xc - xb) if xc != xb else None
        alpha = np.arctan(ka) if ka != None else np.pi / 2
        beta  = np.arctan(kb) if kb != None else np.pi / 2
        # 两条垂直平分线的斜率
        k1 = np.tan(alpha + np.pi / 2)
        k2 = np.tan(beta + np.pi / 2)
        # 圆心
        y, x = solve([[1.0, -k1], [1.0, -k2]], [y1 - k1 * x1, y2 - k2 * x2])
        # 半径
        r1 = np.sqrt((x - xa)**2 + (y - ya)**2)
        return(x, y, r1)

    def pathplaning(self):
        ax = plt.figure(figsize=(12,9))
        # 生成三角形
        self.triangles = tri.Triangulation(self.x_tri,self.y_tri) 
        T = self.triangles.triangles
        num_cir = T.shape[0]
        C = np.zeros((num_cir,3))
        self.sign = np.zeros((num_cir + 2, num_cir + 2), dtype=np.int) #标记点与点是否相连 0-1矩阵  1表示相连
        for i in range(num_cir):
            C[i] = self.get_outer_circle(self.points[T[i,0]], self.points[T[i,1]], self.points[T[i,2]]) #获取三角形外心
            # 起点与终点与所在三角形的外心相连
            if 0 in T[i,:]:
                self.sign[0, i + 1] = 1
                self.sign[i + 1, 0] = 1
                plt.plot([C[i][0], self.p_start[0][0]], [C[i][1], self.p_start[0][1]], 'r')
            if self.p_num - 1 in T[i,:]:
                self.sign[num_cir + 1, i + 1] = 1
                self.sign[i + 1, num_cir + 1] = 1
                plt.plot([C[i][0], self.p_end[0][0]], [C[i][1], self.p_end[0][1]], 'r')
            self.draw_circle(C[i][0], C[i][1], C[i][2], ax)
        #  所有路径点
        self.pathpoints = np.array(self.p_start + list(C[:, :2]) + self.p_end)


        #相邻三角形的外心相连接
        for i in range(num_cir):    
            for j in range(3):
                k = self.triangles.neighbors[i][j]  #
                if k != -1:
                    self.sign[i + 1, k + 1] = 1
                    self.sign[k + 1, i + 1] = 1
                    plt.plot([C[i][0], C[k][0]], [C[i][1], C[k][1]], 'r')

        plt.triplot(self.triangles)  
        plt.scatter(self.x_tri, self.y_tri, color="blue",marker="s")
        plt.axis((-50,54.7, -50,56.1))
        # for i in range(len(self.x_tri)):
        #     plt.text(self.x_tri[i], self.y_tri[i]+0.2, i,ha = 'center',va = 'bottom',fontsize=8)
        for i in range(self.pathpoints.shape[0]):
            plt.text(self.pathpoints[i,0], self.pathpoints[i,1]+0.2, i,ha = 'center',va = 'bottom',fontsize=8)
        plt.show()
        self.dijkstra(self.pathpoints, self.sign)
    
    def dijkstra(self, position, sign):
        cost = np.ones(sign.shape) * np.inf
        for i in range(sign.shape[0]):
            for j in range(sign.shape[1]):
                if sign[i][j] == 1:
                    cost[i][j] = np.sqrt(sum((position[i,:] - position[j,:])**2)) 

        dist=cost[0, :]
        s = np.zeros(sign.shape[0])
        s[0]=1
        dist[0]=0
        path=np.zeros(sign.shape[0])

        for _ in range(1, sign.shape[0]):
    
            mindist = np.inf
            for i in range(sign.shape[0]):
                if s[i] == 0:
                    if dist[i] < mindist:
                        mindist=dist[i]
                        u=i
            
            s[u]=1
            for w in range(sign.shape[0]):
                if s[i] == 0:
                    if dist[u] + cost[u,w] < dist[w]:
                        dist[w] = dist[u] + cost[u,w]
                        path[w]=u
        idx = sign.shape[0] - 1            
        shortest_path = [int(idx)] 
        for _ in range(sign.shape[0] - 1, -1, -1):
            shortest_path.append(int(path[idx]))
            idx = int(path[idx])
            if idx == 0 :
                break
        shortest_path.reverse()

        
        print(shortest_path) #最短路径标号
        route = self.pathpoints[shortest_path, :]
        print(route) #最短路径坐标



point_start = [0,0]
point_end = [50,50]
points = [[5,20], [16,27], [39, 19], [23, 45]]
v = voronoi(point_start, point_end, points)
v.pathplaning()