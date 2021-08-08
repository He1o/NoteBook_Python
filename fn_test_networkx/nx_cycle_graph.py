import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
ax = plt.figure(1).gca()

num_nodes = 5
G = nx.cycle_graph(num_nodes)

pos_array = np.random.uniform(low=-10, high=10, size=(num_nodes, 2))
pos = dict(enumerate(pos_array))
# pos = nx.spring_layout(G,scale = 10)
# pos_array = list(pos.values())
nx.draw_networkx(G, pos, ax=ax)


for i,j in G.edges():
    dis = np.sqrt(np.sum((pos_array[i]-pos_array[j])**2))
    G.add_edge(i,j, dis = dis)
# ax.yaxis.set_visible(False)
# ax.xaxis.set_visible(False)
plt.show()



'''
计算直线表达式
:param vertex1: 前一个顶点
:param vertex2: 后一个顶点
:return (type, param): 返回直线的类别及其描述参数
'''
def kb(vertex1, vertex2):
    x1 = vertex1[0]
    y1 = vertex1[1]
    x2 = vertex2[0]
    y2 = vertex2[1]
    
    if x1==x2:
        return (0, x1)      # 0-垂直直线
    if y1==y2:              
        return (1, y1)      # 1-水平直线
    else:
        k = (y1-y2)/(x1-x2)
        b = y1 - k*x1
        return (2, k, b)    # 2-倾斜直线

'''
判断是否为凸多边形
:param vertexes: 构成多边形的所有顶点坐标列表，如[[0，0], [50, 0], [0, 50]]
:return convex: 布尔类型，为True说明该多边形为凸多边形，否则为凹多边形
'''
def isConvex(vertexes):
    # 默认为凸多边形
    convex = 1   
    
    # 多边形至少包含三个顶点
    l = len(vertexes)
    if l<3:
        raise ValueError("多边形至少包含三个顶点！")
    
    # 对每两个点组成的直线做判断
    for i in range(l):
        pre = i
        nex = (i+1)%l
        
        # 得到直线
        line = kb(vertexes[pre], vertexes[nex])
        
        # 计算所有点和直线的距离（可能为正也可能为负）
        if line[0]==0:
            offset = [vertex[0]-vertexes[pre][0] for vertex in vertexes]
        elif line[0]==1:
            offset = [vertex[1]-vertexes[pre][1] for vertex in vertexes]
        else:
            k, b = line[1], line[2]
            offset = [round(k*vertex[0]+b-vertex[1],10) for vertex in vertexes]
        
        # 计算两两距离的乘积，如果出现负数则存在两个点位于直线两侧，因此为凹多边形
        for o in offset:
            for s in offset:
                if o*s<0:
                    convex = 0
                    break
            if convex==0:
                break
                    
        if convex==0:
            break
            
	# # 打印判断结果
    # if convex==1:
    #     print("该多边形为凸多边形！")
    # else:
    #     print("该多边形为凹多边形！")
    
    return convex


class point(): #定义类
    def __init__(self,x,y):
        self.x=x
        self.y=y   

def cross(p1,p2,p3):#跨立实验
    x1=p2.x-p1.x
    y1=p2.y-p1.y
    x2=p3.x-p1.x
    y2=p3.y-p1.y
    return x1*y2-x2*y1     

def IsIntersec(p1,p2,p3,p4): #判断两线段是否相交

    #快速排斥，以l1、l2为对角线的矩形必相交，否则两线段不相交
    if(max(p1.x,p2.x)>=min(p3.x,p4.x)    #矩形1最右端大于矩形2最左端
    and max(p3.x,p4.x)>=min(p1.x,p2.x)   #矩形2最右端大于矩形最左端
    and max(p1.y,p2.y)>=min(p3.y,p4.y)   #矩形1最高端大于矩形最低端
    and max(p3.y,p4.y)>=min(p1.y,p2.y)): #矩形2最高端大于矩形最低端

    #若通过快速排斥则进行跨立实验
        if(cross(p1,p2,p3)*cross(p1,p2,p4)<=0
           and cross(p3,p4,p1)*cross(p3,p4,p2)<=0):
            D=2
        else:
            D=0
    else:
        D=0
    return D

def to_one_hot(indices, max_value, axis=-1):
  one_hot = np.eye(max_value)[indices]
  if axis not in (-1, one_hot.ndim):
    one_hot = np.moveaxis(one_hot, -1, axis)
  return one_hot

def judge_polygon(pos_array):
    '''
    [1,0,0]  凹
    [0,1,0]  凸
    [0,0,1]  相交
    '''
    for inx_1 in range(len(pos_array)):
        inx_1_2 = (inx_1+1)%len(pos_array)
        for inx_2 in range(len(pos_array)):
            inx_2_2 = (inx_2+1)%len(pos_array)
            if inx_1 == inx_2 or inx_2_2 == inx_1 or inx_1_2 == inx_2 :
                continue
            
            p1 = point(*pos_array[inx_1])
            p2 = point(*pos_array[inx_1_2])
            p3 = point(*pos_array[inx_2])
            p4 = point(*pos_array[inx_2_2])
            if_inter = IsIntersec(p1,p2,p3,p4)
            if if_inter == 2:
                return to_one_hot(if_inter, 3)
    if_inter = isConvex(pos_array)
    return to_one_hot(if_inter, 3)


print(judge_polygon(pos_array))


