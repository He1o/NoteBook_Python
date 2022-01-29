import numpy as np
from collections import defaultdict
import itertools
import json
import matplotlib.pyplot as plt
class Order(object):
    def __init__(self, id_, num, lng, lat):
        self.id_ = id_
        self.num = num
        self.lng = lng
        self.lat = lat
        self.pos = [lng, lat]

class Car(object):
    def __init__(self, id_, sites, lng, lat):
        self.id_ = id_
        self.sites = sites
        self.lng = lng
        self.lat = lat
        self.pos = [lng, lat]
        self.other_pos = []


class Pso():
    def __init__(self, data, type_):
        self.initdata(data)
        
        self.c1 = 1.49445
        self.c2 = 1.49445
        self.maxgen = 50
        self.sizepop = 200
        self.Vrange = [-2, 2]
        if type_ == 'receive':
            self.Prange = [0, self.len_cars - 1]
            self.popshape = self.len_cars
            self.fitness = self.fitness_receive
        if type_ == 'send':
            self.Prange = [0, self.len_psgs - 1]
            self.popshape = self.len_psgs
            self.fitness = self.fitness_send
        
        self.trace = []

        self.zbestfitness = np.inf
        self.bestans = None
    
    
    def initdata(self, data):
        self.grab = defaultdict(list)

        driver_list = data['driver_list']
        user_list = data['user_list']

        self.cars = []
        for car in driver_list:
            self.cars.append(
                Car(car["driver_id"], car["sites"], float(car["coordinate"][0]), float(car["coordinate"][1])))

        self.psgs = []
        for psg in user_list:
            if psg['bind_car']:
                for caridx, car in enumerate(self.cars):
                    if car.id_ == psg['bind_car']:
                        car.other_pos.append([float(psg["coordinate"][0]), float(psg["coordinate"][1])])
                        car.sites -= int(psg["size"])
                        self.grab[caridx].append(Order(psg["id"], int(psg["size"]), float(psg["coordinate"][0]), float(psg["coordinate"][1])))
            else:
                self.psgs.append(Order(psg["id"], int(psg["size"]), float(psg["coordinate"][0]), float(psg["coordinate"][1])))


        self.cars.append(Car('none', 0, 0, 0))


        self.len_cars = len(self.cars)
        self.len_psgs = len(self.psgs)


    def initpops(self):
        self.pops = []     
        for i in range(self.sizepop):
            self.pops.append(np.random.choice(np.arange(self.popshape), size=self.popshape, replace=False))

        self.pops = np.array(self.pops)


        self.V = np.random.randint(*self.Vrange, (self.sizepop, self.popshape))
        self.fits = self.fitness(self.pops)
        self.zbest = self.pops[np.argmin(self.fits)]
        self.gbest = self.pops
        self.zbestfitness = min(self.fits)
        self.gbestfitness = self.fits
        return self.fits
    
    def updata(self):
        v = self.V + self.c1 * np.random.rand(self.sizepop, self.popshape) * (self.gbest - self.pops) + \
                            self.c2 * np.random.rand(self.sizepop, self.popshape) * (self.zbest - self.pops)
        v = np.clip(v, *self.Vrange)
        self.pops = np.clip(self.pops + v, *self.Prange)

        # self.pops = np.ceil(pop).astype(np.int64)
        
        self.V = v

    
    def fitness_receive(self, pops):
        fits = []
        for pop_idx in range(self.sizepop):
            choosed = [1] * self.len_psgs
            tempxv = np.array([self.len_cars - 1] * self.len_psgs)
            carlist = np.argsort(self.pops[pop_idx])
            dists = []
            notfull = []
            for i in carlist:
                px = np.array(self.cars[i].pos)
                unchoo = np.where(choosed)[0]
                dists_CtoP = []
                for j in unchoo:
                    temp_dists = [np.sqrt(np.sum((px - np.array(self.psgs[j].pos))**2)) * 1e5]
                    for op in self.cars[i].other_pos:
                        temp_dists.append(np.sqrt(np.sum((np.array(op) - np.array(self.psgs[j].pos))**2)) * 1e5)
                    dists_CtoP.append(min(temp_dists))
                unchoo = unchoo[np.argsort(dists_CtoP)]
            
                sizecar = self.cars[i].sites
                cardist = 0
                for idx, j in enumerate(unchoo):
                    if self.psgs[j].num <= sizecar:
                        if  sorted(dists_CtoP)[idx] < 5e3:
                            cardist += sorted(dists_CtoP)[idx]
                            sizecar -= self.psgs[j].num
                            choosed[j] = 0
                            tempxv[j] = i
                if cardist:
                    dists.append(cardist)
                    notfull.append(sizecar)
            fit = sum(dists) + len(np.where(tempxv == (self.len_cars - 1))[0]) * 1e5 + sum(notfull) * 1e4
            if  fit <= self.zbestfitness:
                self.bestans = tempxv
            fits.append(fit)
        return np.array(fits)

    def fitness_send(self, pops):
        fits = []
        for pop_idx in range(self.sizepop):
            cars = list(np.argsort([x.sites for x in self.cars]))

            choosed = [1] * self.len_psgs
            tempxv = np.array([self.len_cars - 1] * self.len_psgs)
            psglist = np.argsort(self.pops[pop_idx])
            dists = []
            notfull = []

            for i in self.grab.keys():
                unchoo = np.where(choosed)[0]
                dists_CtoP = []
                for j in range(self.len_psgs):
                    temp_dists = []
                    for op in self.cars[i].other_pos:
                        temp_dists.append(np.sqrt(np.sum((np.array(op) - np.array(self.psgs[j].pos))**2)) * 1e5)
                    dists_CtoP.append(min(temp_dists))
                unchoo = unchoo[np.argsort(dists_CtoP)]                
                
                sizecar = self.cars[i].sites
                cardist = 0
                for idx, j in enumerate(unchoo):
                    if self.psgs[j].num <= sizecar:
                        if  sorted(dists_CtoP)[idx] < 5e3:
                            cardist += sorted(dists_CtoP)[idx]
                            sizecar -= self.psgs[j].num
                            choosed[j] = 0
                            tempxv[j] = i
                dists.append(cardist)                
                cars.remove(i)
                notfull.append(sizecar)
            
            for i in psglist:
                if choosed[i]:
                    px = np.array(self.psgs[i].pos)
                    sizecar = self.cars[cars[-1]].sites - self.psgs[i].num
                    if sizecar >= 0:
                        choosed[i] = 0
                        tempxv[i] = cars.pop()
                        
                        unchoo = np.where(choosed)[0]

                        if len(unchoo):
                            unchoo = sorted(unchoo, key = lambda x: np.sqrt(np.sum((px - np.array(self.psgs[x].pos))**2)))
                        else:
                            break
                        
                        cardist = 0
                        for j in unchoo:
                            if self.psgs[j].num <= sizecar:
                                dis = (np.sqrt(np.sum((px - np.array(self.psgs[j].pos))**2)) * 1e5)
                                if  dis < 5e3:
                                    cardist += dis
                                    sizecar -= self.psgs[j].num
                                    choosed[j] = 0
                                    tempxv[j] = tempxv[i]
                        if cardist:
                            dists.append(cardist)
                            notfull.append(sizecar)
            fit = sum(dists) + len(np.where(tempxv == (self.len_cars - 1))[0]) * 1e5 + sum(notfull) * 1e4
            if  fit < self.zbestfitness:
                self.bestans = tempxv
            fits.append(fit)
        return np.array(fits)


    def iteration(self):
        self.initpops()
        for i in range(self.maxgen):
            print(i, self.maxgen)
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
        return self.decode()

    def decode(self):
        self.bestans = list(self.bestans)
        for car_idx, orders in self.grab.items():
            for order in orders:
                self.bestans.append(car_idx)
                self.psgs.append(order)
        
        result = []
        design = defaultdict(list)
        for i in range(len(self.psgs)):
            design[self.bestans[i]].append(i)
        for car, psg in design.items():
            temp = []
            for p in psg:
                temp.append({
                    'order': {
                        'id': self.psgs[p].id_, 'lnglat': self.psgs[p].pos,
                        'passenger_num': self.psgs[p].num,
                        'is_grab':0
                    }
                })        
            result.append({
                        'car': {'id': self.cars[car].id_, 'sites': self.cars[car].sites,
                                'lnglat': self.cars[car].pos},
                        'orders': temp
                    })
        return result
        
