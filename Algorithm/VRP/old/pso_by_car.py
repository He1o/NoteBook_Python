import numpy as np
from collections import defaultdict
import matplotlib.pyplot as plt
import json
import itertools
class Pso():
    def __init__(self, cars, psgs, size_cars, size_psgs):
        self.c1 = 1.49445
        self.c2 = 1.49445
        self.maxgen = 50
        self.sizepop = 200

        self.size_cars = size_cars
        self.size_psgs = size_psgs
        self.cars = cars
        self.psgs = psgs

        self.len_psgs = len(psgs)
        self.len_cars = len(cars)
        self.Prange = [0, self.len_cars - 1]
        self.Vrange = [-2, 2]

        self.trace = []

        self.zbestfitness = np.inf

    def initpops(self):
        self.pops = []     
        for i in range(self.sizepop):
            self.pops.append(np.random.choice(np.arange(self.len_cars), size=self.len_cars, replace=False))

        self.pops = np.array(self.pops)


        self.V = np.random.randint(*self.Vrange, (self.sizepop, self.len_cars))
        self.fits = self.fitness(self.pops)
        self.zbest = self.pops[np.argmin(self.fits)]
        self.gbest = self.pops
        self.zbestfitness = min(self.fits)
        self.gbestfitness = self.fits
        self.bestans = None
        return self.fits
    
    def updata(self):
        v = self.V + self.c1 * np.random.rand(self.sizepop, self.len_cars) * (self.gbest - self.pops) + \
                            self.c2 * np.random.rand(self.sizepop, self.len_cars) * (self.zbest - self.pops)
        v = np.clip(v, *self.Vrange)
        self.pops = np.clip(self.pops + v, *self.Prange)

        # self.pops = np.ceil(pop).astype(np.int64)
        
        self.V = v

    
    def fitness(self, pops):
        fits = []
        for pop_idx in range(self.sizepop):
            choosed = [1] * self.len_psgs
            tempxv = np.array([self.len_cars - 1] * self.len_psgs)
            carlist = np.argsort(self.pops[pop_idx])
            dists = []
            for i in carlist:
                px = np.array(self.cars[i])
                unchoo = np.where(choosed)[0]
                if len(unchoo):
                    unchoo = sorted(unchoo, key = lambda x: np.sqrt(np.sum((px - np.array(self.psgs[x]))**2)))
                else:
                    break
                
                sizecar = self.size_cars[i]
                cardist = 0
                for j in unchoo:
                    if self.size_psgs[j] <= sizecar:
                        dis = (np.sqrt(np.sum((px - np.array(self.psgs[j]))**2)) * 1e5)
                        if  dis < 5e3:
                            cardist += dis
                            sizecar -= self.size_psgs[j]
                            choosed[j] = 0
                            tempxv[j] = i
                dists.append(cardist)
            fit = sum(dists) + len(np.unique(tempxv)) * 1e4 + len(np.where(tempxv == (self.len_cars - 1))[0]) * 1e5
            if  fit < self.zbestfitness:
                self.bestans = tempxv
            fits.append(fit)
        return np.array(fits)


    def main(self):
        self.initpops()
        for i in range(self.maxgen):
            print(i)
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
print(p.bestans)
def drawmap(zbest):

    design = defaultdict(list)
    for i in range(len(psgs)):
        design[zbest[i]].append(i)
    print(len(design))
    for car, psg in design.items():
        mindis = np.inf
        bestseq = None
        for seq in itertools.permutations(psg):
            dist = 0
            px = np.array(cars[car])
            for pidx in seq:
                py = np.array(psgs[pidx])
                dist += np.sqrt(np.sum((px - py)**2)) * 1e5
                px = py
            if dist < mindis:
                bestseq = seq
                mindis = dist

        xlis = [cars[car][0]]
        ylis = [cars[car][1]]
        for ps in bestseq:
            xlis.append(psgs[ps][0])
            ylis.append(psgs[ps][1])

        plt.plot(xlis, ylis)
    
    plt.scatter([p[0] for p in psgs], [p[1] for p in psgs], c = 'blue')
    plt.scatter([p[0] for p in cars], [p[1] for p in cars], c = 'red')
    for i, num in enumerate(size_psgs):
        plt.text(psgs[i][0] + 0.0001, psgs[i][1] + 0.0001, num)
    for i, num in enumerate(size_cars):
        plt.text(cars[i][0] + 0.0001, cars[i][1] + 0.0001, num)



    plt.figure(2)

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



    plt.figure(3)
    plt.plot(list(range(p.maxgen)), fits)
    plt.show()
    

drawmap(p.bestans)