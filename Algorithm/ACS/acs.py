import numpy as np
from collections import defaultdict
import matplotlib.pyplot as plt
import math

'''
根据levy飞行计算新的巢穴位置
'''
def GetNewNestViaLevy(Xt,Xbest,Lb,Ub,lamuda):
    beta = 1.5
    sigma_u = (math.gamma(1 + beta) * math.sin(math.pi * beta / 2) / (
                math.gamma((1 + beta) / 2) * beta * (2 ** ((beta - 1) / 2)))) ** (1 / beta)
    sigma_v = 1
    for i in range(Xt.shape[0]):
        s = Xt[i,:]
        u = np.random.normal(0, sigma_u, 1)
        v = np.random.normal(0, sigma_v, 1)
        Ls = u / ((abs(v)) ** (1 / beta))
        stepsize = lamuda*Ls*(s-Xbest)   #lamuda的设置关系到点的活力程度  方向是由最佳位置确定的  有点类似PSO算法  但是步长不一样
        s = s + stepsize * np.random.randn(1, len(s))  #产生满足正态分布的序列
        Xt[i, :] = s
        Xt[i,:] = simplebounds(s,Lb,Ub)
    return Xt
'''
按pa抛弃部分巢穴
'''
def empty_nests(nest,Lb,Ub,pa):
    n = nest.shape[0]
    nest1 = nest.copy()
    nest2 = nest.copy()
    rand_m =pa - np.random.rand(n,nest.shape[1])
    rand_m = np.heaviside(rand_m,0)
    np.random.shuffle(nest1)
    np.random.shuffle(nest2)
    # stepsize = np.random.rand(1,1) * (nest1 - nest)
    stepsize = np.random.rand(1,1) * (nest1 - nest2)
    new_nest = nest + stepsize * rand_m
    nest = simplebounds(new_nest,Lb,Ub)
    return nest
'''
获得当前最优解
'''
def get_best_nest(nest, newnest,Nbest,nest_best):
    fitall = 0
    for i in range (nest.shape[0]):
        temp1 = fitness(nest[i,:])
        temp2 = fitness(newnest[i,:])
        if temp1 > temp2:
            nest[i, :] = newnest[i,:]
            if temp2 < Nbest :
                Nbest = temp2
                nest_best = nest[i,:]
            fitall = fitall + temp2
        else:
            fitall = fitall + temp1
    meanfit = fitall/nest.shape[0]
    return  nest , Nbest , nest_best ,meanfit
 
'''
进行适应度计算
'''
def fitness(xv):
    design = defaultdict(list)
    for i in range(len(psgs)):
        design[xv[i]].append(i)
    dists = []
    for car, psg in design.items():
        if car == len(cars) - 1:
            dist = 1e6 * len(psg)
        else:
            dist = 0
            px = np.array(cars[car])
            for p in psg:
                py = np.array(psgs[p])
                dxy = np.sqrt(np.sum((px - py)**2)) * 1e5
                # if dxy > 2e3:
                #     dist += np.inf
                # else:
                dist += dxy
            if gc[car] < sum(gp[psg]):
                dist += np.inf
        
        dists.append(dist)
    return sum(dists) + len(design) * 1e5
 
'''
进行全部适应度计算
'''
def fit_function(X,Y):
    # rastrigin函数
    A = 10
    Z = 2 * A + X ** 2 - A * np.cos(2 * np.pi * X) + Y ** 2 - A * np.cos(2 * np.pi * Y)
    return Z
'''
约束迭代结果
'''
def simplebounds(s,Lb,Ub):
    for i in range(s.shape[0]):
        for j in range(s.shape[1]):
            if s[i][j] < Lb[j]:
                s[i][j] = Lb[j]
            if s[i][j] > Ub[j]:
                s[i][j] = Ub[j]
    s = np.ceil(s).astype(np.int64)
    return s
 


class Pso():
    def __init__(self, cars, psgs, gc, gp, end):
        self.c1 = 1.49445
        self.c2 = 1.49445
        self.maxgen = 200
        self.sizepop = 20

        self.gc = gc
        self.gp = gp
        self.cars = cars
        self.psgs = psgs
        self.end = end

        self.L = len(psgs)
        self.K = len(cars)
        self.Prange = [0, self.K - 1]
        self.Vrange = [-1, 1]

        self.trace = []


    def initpops(self):
        xv = []
        for _ in range(self.sizepop):
            design = defaultdict(int)
            tempxv = [self.K - 1] * self.L
            idxlist = np.random.choice(np.arange(self.L), size=self.L, replace=False)
            for i in idxlist:
                mindist = np.inf
                driver = self.K - 1
                for j in range(self.K):
                    tempdist = np.sqrt(np.sum((np.array(self.psgs[i]) - np.array(self.cars[j]))**2)) * 1e5
                    if  tempdist < mindist and (design[j] + self.gp[i]) <= self.gc[j]:
                        mindist = tempdist
                        driver = j
                design[driver] += self.gp[i]
                tempxv[i] = driver
            xv.append(tempxv)
        xv = np.array(xv)
        # xv = np.random.randint(0, self.K, (self.sizepop, self.L))
        return xv
        
        
        # vv = np.random.randint(*self.Vrange, (self.sizepop, self.L))
        # self.pops = xv
        # self.V = vv
        # self.fits = self.fitness(self.pops)
        # self.zbest = xv[np.argmin(self.fits)]
        # self.gbest = self.pops
        # self.zbestfitness = min(self.fits)
        # self.maxfitness = max(self.fits)
        # self.gbestfitness = self.fits
        # return self.fits
    
    def updata(self):
        v = self.V + self.c1 * np.random.rand(self.sizepop, self.L) * (self.gbest - self.pops) + \
                            self.c2 * np.random.rand(self.sizepop, self.L) * (self.zbest - self.pops)
        v = np.clip(v, *self.Vrange)
        pop = np.clip(self.pops + v, *self.Prange)

        self.pops = np.ceil(pop).astype(np.int64)
        self.V = v

    def fitness(self, xv):
        print(xv)
        design = defaultdict(list)
        for i in range(self.L):
            design[xv[i]].append(i)
        dists = []
        for car, psg in design.items():
            if car == self.K - 1:
                dist = 1e6 * len(psg)
            else:
                dist = 0
                px = np.array(self.cars[car])
                for p in psg:
                    py = np.array(self.psgs[p])
                    dxy = np.sqrt(np.sum((px - py)**2)) * 1e5
                    if dxy > 2e3:
                        dist += np.inf
                    else:
                        dist += dxy
                if self.gc[car] < sum(self.gp[psg]):
                    dist += np.inf
            
            dists.append(dist)
        return sum(dists) + len(design) * 1e5


    def main(self):
        
        lamuda = 1
        pa =0.25
        Lb=[0] * self.L#下界
        Ub=[self.K - 1] * self.L  #上界
        population_size = self.sizepop
        dim = self.L
        # nest= np.random.uniform(Lb[0], Ub[0],(population_size,dim))  # 初始化位置
        nest = self.initpops()
        nest_best = nest[0,:]
        Nbest =self.fitness(nest_best)
        nest ,Nbest, nest_best ,fitmean = get_best_nest(nest,nest,Nbest,nest_best)
        for i in range (self.maxgen):
            nest_c = nest.copy()
            newnest = GetNewNestViaLevy(nest_c, nest_best, Lb, Ub, lamuda) # 根据莱维飞行产生新的位置
    
            nest,Nbest, nest_best ,fitmean = get_best_nest(nest, newnest,Nbest, nest_best) # 判断新的位置优劣进行替换
    
            nest_e = nest.copy()
            newnest = empty_nests(nest_e,Lb,Ub,pa) #丢弃部分巢穴
    
            nest,Nbest, nest_best ,fitmean = get_best_nest(nest,newnest, Nbest, nest_best)  # 再次判断新的位置优劣进行替换
            self.trace.append(Nbest)
    
        print("最优解的适应度函数值",Nbest)
        return  nest_best
        
user_list = [
  {"size":"2","coordinate":["103.972802","30.587585"],"id":"50","is_grab":1,"bind_car":""},
  {"size":"1","coordinate":["103.973741","30.587955"],"id":"51","is_grab":1,"bind_car":""},
  {"size":"3","coordinate":["103.980314","30.587485"],"id":"52","is_grab":1,"bind_car":""},
  {"size":"1","coordinate":["103.975619","30.584122"],"id":"53","is_grab":1,"bind_car":""},
  {"size":"2","coordinate":["103.975613","30.587212"],"id":"54","is_grab":1,"bind_car":""},
  {"size":"3","coordinate":["103.978436","30.590303"],"id":"55","is_grab":1,"bind_car":""},
  {"size":"2","coordinate":["103.981253","30.592622"],"id":"56","is_grab":1,"bind_car":""},
  {"size":"1","coordinate":["104.075655","30.664052"],"id":"01","is_grab":0,"bind_car":""},
  {"size":"3","coordinate":["104.086121","30.663835"],"id":"02","is_grab":0,"bind_car":""},
  {"size":"2","coordinate":["104.095305","30.659031"],"id":"03","is_grab":0,"bind_car":""},
  
  {"size":"1","coordinate":["104.099425","30.648473"],"id":"04","is_grab":0,"bind_car":""},
  {"size":"4","coordinate":["104.086464","30.640954"],"id":"05","is_grab":0,"bind_car":""},
  {"size":"3","coordinate":["104.078654","30.653789"],"id":"06","is_grab":0,"bind_car":""},
  {"size":"1","coordinate":["104.072903","30.645745"],"id":"07","is_grab":0,"bind_car":""},
  {"size":"1","coordinate":["104.073332","30.669072"],"id":"08","is_grab":1,"bind_car":""},
  {"size":"2","coordinate":["104.085349","30.670327"],"id":"09","is_grab":1,"bind_car":""},
  {"size":"2","coordinate":["104.103631","30.668777"],"id":"10","is_grab":1,"bind_car":""},
  {"size":"1","coordinate":["104.108265","30.653051"],"id":"11","is_grab":1,"bind_car":""},
  {"size":"1","coordinate":["104.069384","30.637396"],"id":"12","is_grab":1,"bind_car":""},
  {"size":"5","coordinate":["104.089469","30.640202"],"id":"13","is_grab":0,"bind_car":""},
  
  {"size":"2","coordinate":["104.086658","30.652903"],"id":"14","is_grab":0,"bind_car":""},
  {"size":"1","coordinate":["104.075113","30.659585"],"id":"15","is_grab":0,"bind_car":""},
  {"size":"3","coordinate":["104.096228","30.655635"],"id":"16","is_grab":0,"bind_car":""},
  {"size":"1","coordinate":["104.082366","30.659917"],"id":"17","is_grab":0,"bind_car":""},
  {"size":"2","coordinate":["104.058634","30.663203"],"id":"18","is_grab":1,"bind_car":""},
  {"size":"1","coordinate":["104.061981","30.644522"],"id":"19","is_grab":1,"bind_car":""},
  {"size":"2","coordinate":["104.055716","30.641347"],"id":"20","is_grab":1,"bind_car":""},
  {"size":"1","coordinate":["104.049793","30.652349"],"id":"21","is_grab":1,"bind_car":""}]

driver_list = [
  {"driver_id":"1","coordinate":["104.096554","30.653434"],"sites":4},
  {"driver_id":"2","coordinate":["104.075736","30.650107"],"sites":6},
  {"driver_id":"3","coordinate":["104.080448","30.647407"],"sites":4},
  {"driver_id":"4","coordinate":["104.077281","30.658662"],"sites":4},
  {"driver_id":"5","coordinate":["104.096845","30.644411"],"sites":6},
  {"driver_id":"6","coordinate":["104.092902","30.656964"],"sites":4},
  {"driver_id":"7","coordinate":["104.085452","30.664464"],"sites":6},
  {"driver_id":"8","coordinate":["104.076766","30.640571"],"sites":6},
  {"driver_id":"9","coordinate":["104.070843","30.652312"],"sites":4},
  {"driver_id":"10","coordinate":["104.090069","30.64049"],"sites":4},
  
  {"driver_id":"11","coordinate":["104.086379","30.66711"],"sites":5},
  {"driver_id":"12","coordinate":["104.109295","30.66284"],"sites":6},
  {"driver_id":"13","coordinate":["104.063719","30.66805"],"sites":8},
  {"driver_id":"14","coordinate":["104.066294","30.63319"],"sites":6},
  {"driver_id":"15","coordinate":["104.057969","30.65239"],"sites":4},
  {"driver_id":"16","coordinate":["104.096764","30.63384"],"sites":6},
  {"driver_id":"17","coordinate":["104.083289","30.65028"],"sites":4},
  {"driver_id":"18","coordinate":["104.075306","30.64581"],"sites":3},
  {"driver_id":"19","coordinate":["104.095648","30.64083"],"sites":6},
  {"driver_id":"20","coordinate":["104.095648","30.64083"],"sites":6},
  
  {"driver_id":"71","coordinate":["103.954680","30.59416"],"sites":6},
  {"driver_id":"72","coordinate":["103.914680","30.59416"],"sites":6},
  {"driver_id":"73","coordinate":["103.924680","30.59416"],"sites":6},
  {"driver_id":"74","coordinate":["103.934680","30.59416"],"sites":6},
  {"driver_id":"75","coordinate":["103.944680","30.51416"],"sites":6},
  {"driver_id":"76","coordinate":["103.964680","30.55416"],"sites":6},
  {"driver_id":"77","coordinate":["103.977680","30.59516"],"sites":6},
  {"driver_id":"78","coordinate":["103.974680","30.59416"],"sites":6}]


cars = []
gc = []

for car in driver_list:
    cars.append([float(car["coordinate"][0]), float(car["coordinate"][1])])
    gc.append(car["sites"])

psgs = []
gp = []

for psg in user_list:
    psgs.append([float(psg["coordinate"][0]), float(psg["coordinate"][1])])
    gp.append(int(psg["size"]))

# cars = [(2, 3), (45, 87), (67, 85), (0, 0)]
# # cars = [(2, 3), (45, 87), (67, 85), (15, 56), (29, 45)]
# psgs = [(18, 54), (22, 60), (58, 69), (71, 71), (83, 46), (91, 38), (24, 42), (18, 40)]
# end = np.array([200, 50])
# # gc = np.array([4, 6, 4, 4, 6])
cars = cars + [[103.90, 30.50]]
gc = np.array(gc + [100])
gp = np.array(gp)
end = np.array([104.50, 30.60])




p = Pso(cars, psgs, gc, gp, end)
xv = p.main()
fits = p.trace


def drawmap(xv):
    # plt.plot(list(range(self.maxgen)), self.trace)

    design = defaultdict(list)
    for i in range(len(psgs)):
        design[xv[i]].append(i)
    print(len(design))
    for car, psg in design.items():
        px = [cars[car][0]]
        py = [cars[car][1]]
        for ps in psg:
            px.append(psgs[ps][0])
            px.append(cars[car][0])
            py.append(psgs[ps][1])
            py.append(cars[car][1])
        
        plt.plot(px, py)
    
    plt.scatter([p[0] for p in psgs], [p[1] for p in psgs], c = 'blue')
    plt.scatter([p[0] for p in cars], [p[1] for p in cars], c = 'red')
    for i, num in enumerate(gp):
        plt.text(psgs[i][0] + 0.0001, psgs[i][1] + 0.0001, num)
    for i, num in enumerate(gc):
        plt.text(cars[i][0] + 0.0001, cars[i][1] + 0.0001, num)
    plt.scatter(end[0], end[1])

    plt.figure(2)
    plt.plot(list(range(p.maxgen)), fits)
    plt.show()
    

drawmap(xv)