import numpy as np
from collections import defaultdict
import itertools
class Pso_receive():
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


    def iteration(self):
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
        return self.bestans
        # self.rule()

        # self.drawmap()
        


class Pso_send():
    def __init__(self, cars, psgs, size_cars, size_psgs):
        self.c1 = 1.49445
        self.c2 = 1.49445
        self.maxgen = 50
        self.sizepop = 200

        self.size_cars = sorted(size_cars)
        self.size_psgs = size_psgs
        self.cars = cars
        self.psgs = psgs

        self.len_psgs = len(psgs)
        self.len_cars = len(cars)
        self.Prange = [0, self.len_psgs - 1]
        self.Vrange = [-2, 2]

        self.trace = []

        self.zbestfitness = np.inf

    def initpops(self):
        self.pops = []     
        for i in range(self.sizepop):
            self.pops.append(np.random.choice(np.arange(self.len_psgs), size=self.len_psgs, replace=False))

        self.pops = np.array(self.pops)


        self.V = np.random.randint(*self.Vrange, (self.sizepop, self.len_psgs))
        self.fits = self.fitness(self.pops)
        self.zbest = self.pops[np.argmin(self.fits)]
        self.gbest = self.pops
        self.zbestfitness = min(self.fits)
        self.gbestfitness = self.fits
        self.bestans = None
        return self.fits
    
    def updata(self):
        v = self.V + self.c1 * np.random.rand(self.sizepop, self.len_psgs) * (self.gbest - self.pops) + \
                            self.c2 * np.random.rand(self.sizepop, self.len_psgs) * (self.zbest - self.pops)
        v = np.clip(v, *self.Vrange)
        self.pops = np.clip(self.pops + v, *self.Prange)

        # self.pops = np.ceil(pop).astype(np.int64)
        
        self.V = v

    
    def fitness(self, pops):
        fits = []
        for pop_idx in range(self.sizepop):
            cars = self.size_cars[:]
            choosed = [1] * self.len_psgs
            tempxv = np.array([self.len_cars - 1] * self.len_psgs)
            psglist = np.argsort(self.pops[pop_idx])
            dists = []
            for i in psglist:
                if choosed[i]:
                    px = np.array(self.psgs[i])
                    sizecar = cars[-1] - self.size_psgs[i]
                    if sizecar >= 0:
                        choosed[i] = 0
                        tempxv[i] = i
                        cars.pop()
                        unchoo = np.where(choosed)[0]

                        if len(unchoo):
                            unchoo = sorted(unchoo, key = lambda x: np.sqrt(np.sum((px - np.array(self.psgs[x]))**2)))
                        else:
                            break
                        
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


    def iteration(self):
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
        return self.bestans
        # self.drawmap()