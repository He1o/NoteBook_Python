import numpy as np
from collections import defaultdict
import matplotlib.pyplot as plt
class Pso():
    def __init__(self, cars, psgs, gc, gp, end):
        self.c1 = 1.49445
        self.c2 = 1.49445
        self.maxgen = 500
        self.sizepop = 200

        self.gc = gc
        self.gp = gp
        self.cars = cars
        self.psgs = psgs
        self.end = end

        self.L = len(psgs)
        self.K = len(cars)
        self.Prange = [0, self.K - 1]
        # self.Vrange = [[-(self.K - 1), (self.K - 1)], [-(self.L - 1), (self.L - 1)]]
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
        
        
        
        vv = np.random.randint(*self.Vrange, (self.sizepop, self.L))
        self.pops = xv
        self.V = vv
        self.fits = self.fitness(self.pops)
        self.zbest = xv[np.argmin(self.fits)]
        self.gbest = self.pops
        self.zbestfitness = min(self.fits)
        self.maxfitness = max(self.fits)
        self.gbestfitness = self.fits
        return self.fits
    
    def updata(self):
        v = self.V + self.c1 * np.random.rand(self.sizepop, self.L) * (self.gbest - self.pops) + \
                            self.c2 * np.random.rand(self.sizepop, self.L) * (self.zbest - self.pops)
        v = np.clip(v, *self.Vrange)
        pop = np.clip(self.pops + v, *self.Prange)

        self.pops = np.ceil(pop).astype(np.int64)
        self.V = v

    def fitness(self, pops):
        fits = []
        for i in range(self.sizepop):
            xv = pops[i]
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
                        if dxy > 5e3:
                            dist += np.inf
                        else:
                            dist += dxy
                    if self.gc[car] < sum(self.gp[psg]):
                        dist += np.inf
                
                dists.append(dist)
            fits.append(sum(dists) + len(design) * 1e5)
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
            # self.cross()
            # self.select()
        # self.drawmap()
        



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


a = []
b = []
for i in range(1):
    p = Pso(cars, psgs, gc, gp, end)
    p.main()
    fits = p.trace
    xv = p.zbest

    a.append(p.zbestfitness)
    b.append(p.zbest)

print(b[np.argmin(a)])
print(a)
def drawmap(zbest):
    # plt.plot(list(range(self.maxgen)), self.trace)

    xv= zbest
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
    

drawmap(b[np.argmin(a)])