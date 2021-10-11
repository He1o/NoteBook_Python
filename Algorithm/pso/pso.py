import numpy as np
from collections import defaultdict
import matplotlib.pyplot as plt
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
        self.Prange = [[0, self.K - 1], [0, self.L - 1]]
        self.Vrange = [[-(self.K - 1), (self.K - 1)], [-(self.L - 1), (self.L - 1)]]
        # self.Vrange = [[-2, 2], [-2, 2]]

        self.trace = []


    def initpops(self):
        xv = np.random.randint(0, self.K, (self.sizepop, self.L))
        xr = np.random.uniform(0, self.L, (self.sizepop, self.L))
        vv = np.random.randint(*self.Vrange[0], (self.sizepop, self.L))
        vr = np.random.uniform(*self.Vrange[1], (self.sizepop, self.L))
        self.pops = [xv, xr]
        self.V = [vv, vr]
        self.fits = self.fitness(self.pops)
        self.zbest = [xv[np.argmin(self.fits)], xr[np.argmin(self.fits)]]
        self.gbest = self.pops
        self.zbestfitness = min(self.fits)
        self.gbestfitness = self.fits
        return self.fits
    
    def updata(self):
        pops = []
        V = []
        for idx, pop in enumerate(self.pops):
            v = self.V[idx] + self.c1 * np.random.rand(self.sizepop, self.L) * (self.gbest[idx] - pop) + \
                              self.c2 * np.random.rand(self.sizepop, self.L) * (self.zbest[idx] - pop)
            v = np.clip(v, *self.Vrange[idx])
            pop = np.clip(pop + v, *self.Prange[idx])
            V.append(v)
            pops.append(pop)
        pops[0] = np.ceil(pops[0]).astype(np.int64)
        self.pops = pops
        self.V = V


    def fitness(self, pops):
        fits = []
        for i in range(self.sizepop):
            xv, xr = pops[0][i], pops[1][i]
            design = defaultdict(list)
            for i in range(self.L):
                design[xv[i]].append(i)
            dists = []
            for car, psg in design.items():
                dist = 0
                px = np.array(self.cars[car])
                for idx, tup in enumerate(sorted(zip(psg, xr[psg]), key=lambda x: x[1])):
                    py = np.array(self.psgs[tup[0]])
                    dist += np.sqrt(np.sum((px - py)**2))
                    px = py
                    xr[psg[idx]] = idx
                dist += np.sqrt(np.sum((px - self.end)**2))
                if self.gc[car] < sum(self.gp[psg]):
                    dist += np.inf
                
                dists.append(dist)
            fits.append(sum(dists) + len(design) * 10)
        return fits

            
    def drawmap(self):
        # plt.plot(list(range(self.maxgen)), self.trace)

        xv, xr = self.zbest
        design = defaultdict(list)
        for i in range(self.L):
            design[xv[i]].append(i)
        for car, psg in design.items():
            px = [self.cars[car][0]]
            py = [self.cars[car][1]]
            for tup in sorted(zip(psg, xr[psg]), key=lambda x: x[1]):
                px.append(self.psgs[tup[0]][0])
                py.append(self.psgs[tup[0]][1])
            
            plt.plot(px, py)
        
        [p[0] for p in self.psgs]
        plt.scatter([p[0] for p in self.psgs], [p[1] for p in self.psgs], c = 'blue')
        plt.scatter([p[0] for p in self.cars], [p[1] for p in self.cars], c = 'red')
        plt.show()

    def main(self):
        self.initpops()
        for i in range(self.maxgen):
            self.updata()
            self.fits = self.fitness(self.pops)
            for j in range(self.sizepop):
                if self.fits[j] < self.gbestfitness[j]:
                    self.gbestfitness[j] = self.fits[j]
                    self.gbest[0][j] = self.pops[0][j]
                    self.gbest[1][j] = self.pops[1][j]
                if self.fits[j] < self.zbestfitness:
                    self.zbestfitness = self.fits[j]
                    self.zbest = [self.pops[0][j], self.pops[1][j]]
            
            self.trace.append(self.zbestfitness)
        # self.drawmap()
        
        


cars = [(2, 3), (45, 87), (67, 85), (15, 56), (29, 45)]
psgs = [(18, 54), (22, 60), (58, 69), (71, 71), (83, 46), (91, 38), (24, 42), (18, 40)]
end = np.array([200, 50])
gc = np.array([4, 6, 4, 4, 6])
gp = np.array([2, 3, 1, 1, 2, 2, 3, 1])

a = []
b = []
for i in range(1):
    p = Pso(cars, psgs, gc, gp, end)
    p.main()
    a.append(p.zbestfitness)
    b.append(p.zbest)
    fits = p.trace
print(b[np.argmin(a)])
print(a)

def drawmap(zbest):
    # plt.plot(list(range(self.maxgen)), self.trace)

    xv, xr = zbest
    design = defaultdict(list)
    for i in range(len(psgs)):
        design[xv[i]].append(i)
    for car, psg in design.items():
        px = [cars[car][0]]
        py = [cars[car][1]]
        for tup in sorted(zip(psg, xr[psg]), key=lambda x: x[1]):
            px.append(psgs[tup[0]][0])
            py.append(psgs[tup[0]][1])
        
        plt.plot(px, py)
    
    [p[0] for p in psgs]
    plt.scatter([p[0] for p in psgs], [p[1] for p in psgs], c = 'blue')
    plt.scatter([p[0] for p in cars], [p[1] for p in cars], c = 'red')
    
    
    plt.figure(2)
    plt.plot(list(range(p.maxgen)), fits)
    plt.show()

drawmap(b[np.argmin(a)])