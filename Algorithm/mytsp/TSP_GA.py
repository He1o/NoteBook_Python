# -*- encoding: utf-8 -*-

import numpy as np
import pandas as pd
from DW import *
from collections import defaultdict
import matplotlib.pyplot as plt

class TSP(object):
    citys = np.array([])
    citys_name = np.array([])
    pop_size = 50
    c_rate = 0.7
    m_rate = 0.05
    pop = np.array([])
    fitness = np.array([])
    city_size = -1
    ga_num = 200
    best_dist = 1
    best_gen = []
    dw = Draw()

    def __init__(self, c_rate, m_rate, pop_size, ga_num, cars, psgs, gc, gp, end):
        self.c_rate = c_rate
        self.m_rate = m_rate
        self.pop_size = pop_size
        self.ga_num = ga_num

        self.gc = gc
        self.gp = gp
        self.cars = cars
        self.psgs = psgs
        self.end = end

        self.L = len(psgs)
        self.K = len(cars)

        self.trace = []



    def init(self):
        xv = []
        for _ in range(self.pop_size):
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



        tsp = self
        # tsp.load_Citys()
        tsp.pop = xv
        tsp.fitness = tsp.get_fitness(tsp.pop)
        # tsp.dw.bound_x = [np.min(tsp.citys[:, 0]), np.max(tsp.citys[:, 0])]
        # tsp.dw.bound_y = [np.min(tsp.citys[:, 1]), np.max(tsp.citys[:, 1])]
        # tsp.dw.set_xybound(tsp.dw.bound_x, tsp.dw.bound_y)

    # --------------------------------------

    def get_fitness(self, pop):
        fits = []
        for i in range(self.pop_size):
            xv = pop[i]
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
                        dist += np.sqrt(np.sum((px - py)**2)) * 1e5
                        # px = py
                    # dist += np.sqrt(np.sum((px - self.end)**2))
                    if self.gc[car] < sum(self.gp[psg]):
                        dist += np.inf
                
                dists.append(dist)
            fits.append(1 / (sum(dists) + len(design) * 5e3))
        return np.array(fits)

    def gen_distance(self, xv):
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
                    dist += np.sqrt(np.sum((px - py)**2)) * 1e5
                    # px = py
                # dist += np.sqrt(np.sum((px - self.end)**2))
                if self.gc[car] < sum(self.gp[psg]):
                    dist += np.inf
            
            dists.append(dist)
        return sum(dists) + len(design) * 5e3
    # -------------------------------------
    def select_pop(self, pop):
        best_f_index = np.argmax(self.fitness)
        av = np.median(self.fitness, axis=0)
        for i in range(self.pop_size):
            if i != best_f_index and self.fitness[i] < av:
                pi = self.cross(pop[best_f_index], pop[i])
                pi = self.mutate(pi)
                # d1 = self.distance(pi)
                # d2 = self.distance(pop[i])
                # if d1 < d2:
                pop[i, :] = pi[:]

        return pop

    def cross(self, parent1, parent2):
        """交叉"""
        if np.random.rand() > self.c_rate:
            return parent1
        index1 = np.random.randint(0, self.L)
        index2 = np.random.randint(index1, self.L)
        if np.random.rand() > 0.5:
            tempGene = parent2[index1:index2]  # 交叉的基因片段
            newGene = parent1
            # p1len = 0
            # for g in parent1:
            #     if p1len == index1:
            #         newGene.extend(tempGene)  # 插入基因片段
            #     if g not in tempGene:
            #         newGene.append(g)
            #     p1len += 1
            
            # newGene = np.array(newGene)
            newGene[index1:index2] = tempGene
        else:
            newGene = parent1
            tmp = newGene[index1]
            newGene[index1] = newGene[index2]
            newGene[index2] = tmp

        return newGene

    def mutate(self, gene):
        """突变"""
        if np.random.rand() > self.m_rate:
            return gene
        index1 = np.random.randint(0, self.L)
        # index2 = np.random.randint(index1, self.city_size - 1)
        newGene = gene
        newGene[index1] = np.random.randint(self.K)
        # if newGene.shape[0] != self.city_size:
        #     print('m error')
        #     return self.creat_pop(1)
        return newGene



    def evolution(self):
        tsp = self
        for i in range(self.ga_num):
            best_f_index = np.argmax(tsp.fitness)
            worst_f_index = np.argmin(tsp.fitness)
            local_best_gen = tsp.pop[best_f_index]
            local_best_dist = tsp.gen_distance(local_best_gen)
            if i == 0:
                tsp.best_gen = local_best_gen
                tsp.best_dist = tsp.gen_distance(local_best_gen)

            if local_best_dist < tsp.best_dist:
                tsp.best_dist = local_best_dist
                tsp.best_gen = local_best_gen
                # tsp.dw.ax.cla()
                # tsp.re_draw()
                # tsp.dw.plt.pause(0.001)
            else:
                tsp.pop[worst_f_index] = self.best_gen
            print('gen:%d evo,best dist :%s' % (i, self.best_dist))

            tsp.pop = tsp.select_pop(tsp.pop)
            tsp.fitness = tsp.get_fitness(tsp.pop)
            for j in range(self.pop_size):
                r = np.random.randint(0, self.pop_size - 1)
                if j != r:
                    tsp.pop[j] = tsp.cross(tsp.pop[j], tsp.pop[r])
                    tsp.pop[j] = tsp.mutate(tsp.pop[j])
            #self.best_gen = self.EO(self.best_gen)
            tsp.best_dist = tsp.gen_distance(self.best_gen)



def main():
    
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

    tsp = TSP(0.5, 0.1, 100, 500, cars, psgs, gc, gp, end)
    tsp.init()
    tsp.evolution()


if __name__ == '__main__':
    main()
