import numpy as np
from collections import defaultdict
import matplotlib.pyplot as plt
import json

class Pso():
    def __init__(self, cars, psgs, size_cars, size_psgs):
        self.c1 = 1.49445
        self.c2 = 1.49445
        self.maxgen = 500
        self.sizepop = 100

        self.size_cars = size_cars
        self.size_psgs = size_psgs
        self.cars = cars
        self.psgs = psgs

        self.len_psgs = len(psgs)
        self.len_cars = len(cars)
        self.Prange = [0, self.len_cars - 1]
        self.Vrange = [-2, 2]

        self.trace = []


    def initpops(self):
        self.pops = []
        for _ in range(self.sizepop // 2):
            design = defaultdict(int)
            tempxv = [self.len_cars - 1] * self.len_psgs
            idxlist = np.random.choice(np.arange(self.len_psgs), size=self.len_psgs, replace=False)
            for i in idxlist:
                mindist = np.inf
                driver = self.len_cars - 1
                for j in range(self.len_cars):
                    tempdist = np.sqrt(np.sum((np.array(self.psgs[i]) - np.array(self.cars[j]))**2)) * 1e5
                    if  tempdist < mindist and (design[j] + self.size_psgs[i]) <= self.size_cars[j]:
                        mindist = tempdist
                        driver = j
                design[driver] += self.size_psgs[i]
                tempxv[i] = driver
            self.pops.append(tempxv)        

        for _ in range(self.sizepop // 2, self.sizepop):
            choosed = [1] * self.len_psgs
            tempxv = [self.len_cars - 1] * self.len_psgs
            carlist = np.random.choice(np.arange(self.len_cars - 1), size=self.len_cars - 1, replace=False)
            for i in carlist:
                px = np.array(self.cars[i])
                unchoo = np.where(choosed)[0]
                if len(unchoo):
                    unchoo = sorted(unchoo, key = lambda x: np.sqrt(np.sum((px - np.array(self.psgs[x]))**2)))
                sizecar = self.size_cars[i]
                load = []
                for j in unchoo:
                    if self.size_psgs[j] <= sizecar and ((np.sqrt(np.sum((px - np.array(self.psgs[j]))**2)) * 1e5) < 5e3):
                        sizecar -= self.size_psgs[j]
                        load.append(j)
                        choosed[j] = 0
                        tempxv[j] = i
                
            self.pops.append(tempxv)
        self.pops = np.array(self.pops)


        self.V = np.random.randint(*self.Vrange, (self.sizepop, self.len_psgs))
        self.fits = self.fitness(self.pops)
        self.zbest = self.pops[np.argmin(self.fits)]
        self.gbest = self.pops
        self.zbestfitness = min(self.fits)
        self.maxfitness = max(self.fits)
        self.gbestfitness = self.fits
        return self.fits
    
    def updata(self):
        v = self.V + self.c1 * np.random.rand(self.sizepop, self.len_psgs) * (self.gbest - self.pops) + \
                            self.c2 * np.random.rand(self.sizepop, self.len_psgs) * (self.zbest - self.pops)
        v = np.clip(v, *self.Vrange)
        pop = np.clip(self.pops + v, *self.Prange)

        self.pops = np.ceil(pop).astype(np.int64)
        self.V = v

    def rule(self):
        self.zbest = [27, 27, 26, 27, 26, 23, 27, 3, 6, 6, 0, 8, 2, 2, 3, 11, 11, 11, 13, 18, 15, 3, 0, 3, 13, 13, 15, 13]

        flag = True
        while flag:
            design = defaultdict(list)
            for i in range(self.len_psgs):
                design[self.zbest[i]].append(i)
            sorlist = sorted(design.items(), key = lambda x: len(x[1]))

            for order in sorlist:
                exchg = None
                cdx, psgs = order
                py1 = np.array(self.cars[cdx])
                for pdx in psgs:
                    px = np.array(self.psgs[pdx])
                    for cdx2 in design.keys():
                        py2 = np.array(self.cars[cdx2])
                        if np.sqrt(np.sum((px - py2)**2)) * 1e5 < np.sqrt(np.sum((px - py1)**2)) * 1e5 \
                            and sum(self.size_psgs[design[cdx2]]) + self.size_psgs[pdx] <= self.size_cars[cdx2]:
                            py1 = py2
                            exchg = [pdx, cdx2]
                    if exchg:
                        break
                if exchg:
                    self.zbest[exchg[0]] = exchg[1]
                    break
            else:
                flag = False


        print(self.zbest)

    
    def fitness(self, pops):
        fits = []
        for i in range(self.sizepop):
            pop = pops[i]
            design = defaultdict(list)
            for j in range(self.len_psgs):
                design[pop[j]].append(j)
            
            dists = []
            for car, psg in design.items():
                if car == self.len_cars - 1:
                    dist = 1e6 * len(psg)
                else:
                    dist = 0
                    px = np.array(self.cars[car])
                    for p in psg:
                        py = np.array(self.psgs[p])
                        dist += np.sqrt(np.sum((px - py)**2)) * 1e5
                    if self.size_cars[car] < sum(self.size_psgs[psg]):
                        dist += np.inf
                    # elif self.size_cars[car] == sum(self.size_psgs[psg]):
                    #     dist -= 1e4
                    # else:
                    #     dist += 1e4
                
                dists.append(dist)
            # fits.append(sum(dists))
            fits.append(sum(dists) + len(design) * 1e4)
        return np.array(fits)


    def main(self):
        self.initpops()
        for i in range(self.maxgen):
            self.updata()
            self.fits = self.fitness(self.pops)
            for j in range(self.sizepop):
                if self.fits[j] < self.gbestfitness[j]:
                    self.gbestfitness[j] = self.fits[j]
                    self.gbest[j] = self.pops[j]
                if self.fits[j] < self.zbestfitness:
                    self.zbestfitness = self.fits[j]
                    self.zbest = self.pops[j]
            
            self.trace.append(self.zbestfitness)
        # self.rule()

        # self.drawmap()
        

with open('data.json') as f:
    data = json.load(f)
driver_list = data['driver_list']
user_list = data['user_list']


cars = []
size_cars = []
for car in driver_list:
    cars.append([float(car["coordinate"][0]), float(car["coordinate"][1])])
    size_cars.append(car["sites"])

psgs = []
size_psgs = []
for psg in user_list:
    psgs.append([float(psg["coordinate"][0]), float(psg["coordinate"][1])])
    size_psgs.append(int(psg["size"]))

cars = cars + [[103.90, 30.50]]
size_cars = np.array(size_cars + [100])
size_psgs = np.array(size_psgs)


a = []
b = []
for i in range(1):
    p = Pso(cars, psgs, size_cars, size_psgs)
    p.main()
    fits = p.trace
    a.append(p.zbestfitness)
    b.append(p.zbest)
    xv = b[np.argmin(a)]


print(b[np.argmin(a)])
print(a)
def drawmap(zbest):

    design = defaultdict(list)
    for i in range(len(psgs)):
        design[zbest[i]].append(i)
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
    for i, num in enumerate(size_psgs):
        plt.text(psgs[i][0] + 0.0001, psgs[i][1] + 0.0001, num)
    for i, num in enumerate(size_cars):
        plt.text(cars[i][0] + 0.0001, cars[i][1] + 0.0001, num)

    plt.figure(2)
    plt.plot(list(range(p.maxgen)), fits)
    plt.show()
    

drawmap(b[np.argmin(a)])