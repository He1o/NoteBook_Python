# import numpy as np
# from collections import defaultdict
# import matplotlib.pyplot as plt
# import json



# [{'car': {'id': 1, 'sites': 4, 'lnglat': [104.096554, 30.653434]}, 'orders': [{'order': {'id': 4, 'lnglat': [104.099425, 30.648473], 'passenger_num': 1, 'is_grab': 0}}, {'order': {'id': 16, 'lnglat': [104.096228, 30.655635], 'passenger_num': 3, 'is_grab': 0}}]}, 
# {'car': {'id': 2, 'sites': 6, 'lnglat': [104.075736, 30.650107]}, 'orders': [{'order': {'id': 17, 'lnglat': [104.082366, 30.659917], 'passenger_num': 1, 'is_grab': 0}}, {'order': {'id': 6, 'lnglat': [104.078654, 30.653789], 'passenger_num': 3, 'is_grab': 0}}]}, 
# {'car': {'id': 3, 'sites': 4, 'lnglat': [104.080448, 30.647407]}, 'orders': [{'order': {'id': 7, 'lnglat': [104.072903, 30.645745], 'passenger_num': 1, 'is_grab': 0}}]}, 
# {'car': {'id': 4, 'sites': 4, 'lnglat': [104.077281, 30.658662]}, 'orders': [{'order': {'id': 15, 'lnglat': [104.075113, 30.659585], 'passenger_num': 1, 'is_grab': 0}}, {'order': {'id': 1, 'lnglat': [104.075655, 30.664052], 'passenger_num': 1, 'is_grab': 0}}]}, 
# {'car': {'id': 6, 'sites': 4, 'lnglat': [104.092902, 30.656964]}, 'orders': [{'order': {'id': 3, 'lnglat': [104.095305, 30.659031], 'passenger_num': 2, 'is_grab': 0}}, {'order': {'id': 11, 'lnglat': [104.108265, 30.653051], 'passenger_num': 1, 'is_grab': 1}}]}, 
# {'car': {'id': 7, 'sites': 6, 'lnglat': [104.085452, 30.664464]}, 'orders': [{'order': {'id': 2, 'lnglat': [104.086121, 30.663835], 'passenger_num': 3, 'is_grab': 0}}]}, 
# {'car': {'id': 9, 'sites': 4, 'lnglat': [104.070843, 30.652312]}, 'orders': [{'order': {'id': 18, 'lnglat': [104.058634, 30.663203], 'passenger_num': 2, 'is_grab': 1}}]}, 
# {'car': {'id': 10, 'sites': 4, 'lnglat': [104.090069, 30.64049]}, 'orders': [{'order': {'id': 5, 'lnglat': [104.086464, 30.640954], 'passenger_num': 4, 'is_grab': 0}}]}, 
# {'car': {'id': 11, 'sites': 5, 'lnglat': [104.086379, 30.66711]}, 'orders': [{'order': {'id': 9, 'lnglat': [104.085349, 30.670327], 'passenger_num': 2, 'is_grab': 1}}]}, 
# {'car': {'id': 12, 'sites': 6, 'lnglat': [104.109295, 30.66284]}, 'orders': [{'order': {'id': 10, 'lnglat': [104.103631, 30.668777], 'passenger_num': 2, 'is_grab': 1}}]}, 
# {'car': {'id': 13, 'sites': 8, 'lnglat': [104.063719, 30.66805]}, 'orders': [{'order': {'id': 8, 'lnglat': [104.073332, 30.669072], 'passenger_num': 1, 'is_grab': 1}}]}, 
# {'car': {'id': 14, 'sites': 6, 'lnglat': [104.066294, 30.63319]}, 'orders': [{'order': {'id': 12, 'lnglat': [104.069384, 30.637396], 'passenger_num': 1, 'is_grab': 1}}]}, 
# {'car': {'id': 15, 'sites': 4, 'lnglat': [104.057969, 30.65239]}, 'orders': [{'order': {'id': 20, 'lnglat': [104.055716, 30.641347], 'passenger_num': 2, 'is_grab': 1}}, {'order': {'id': 19, 'lnglat': [104.061981, 30.644522], 'passenger_num': 1, 'is_grab': 1}}, {'order': {'id': 21, 'lnglat': [104.049793, 30.652349], 'passenger_num': 1, 'is_grab': 1}}]}, 
# {'car': {'id': 16, 'sites': 6, 'lnglat': [104.096764, 30.63384]}, 'orders': [{'order': {'id': 13, 'lnglat': [104.089469, 30.640202], 'passenger_num': 5, 'is_grab': 0}}]}, 
# {'car': {'id': 17, 'sites': 4, 'lnglat': [104.083289, 30.65028]}, 'orders': [{'order': {'id': 14, 'lnglat': [104.086658, 30.652903], 'passenger_num': 2, 'is_grab': 0}}]}]

# design = {
#     1: [4, 16],
#     2: [17, 6],
#     3: [7],
#     4: [15, 1],
#     6: [3, 11],
#     7: [2],
#     9: [18],
#     10: [5],
#     11: [9],
#     12: [10],
#     13: [8],
#     14: [12],
#     15: [20, 19, 21],
#     16: [13],
#     17: [14]
# }


# with open('data.json') as f:
#     data = json.load(f)

# driver_list = data['driver_list']
# user_list = data['user_list']

# cars = []
# gc = []

# for car in driver_list:
#     cars.append([float(car["coordinate"][0]), float(car["coordinate"][1])])
#     gc.append(car["sites"])

# psgs = []
# gp = []

# for psg in user_list:
#     psgs.append([float(psg["coordinate"][0]), float(psg["coordinate"][1])])
#     gp.append(int(psg["size"]))

# cars = cars + [[103.90, 30.50]]
# gc = np.array(gc + [100])
# gp = np.array(gp)
# end = np.array([104.50, 30.60])

# # tempxv = [self.len_cars - 1] * self.len_psgs
# # idxlist = np.random.choice(np.arange(self.len_cars), size=self.len_cars, replace=False)
# # for i in idxlist:
# #     mindist = np.inf
# #     for j in range(self.len_psgs):
# #         if tempxv[j] == self.len_cars - 1:
# #             tempdist = np.sqrt(np.sum((np.array(self.psgs[i]) - np.array(self.cars[j]))**2)) * 1e5
# #             if  tempdist < mindist and (design[j] + self.size_psgs[i]) <= self.size_cars[j]:
# #                 mindist = tempdist
# #                 driver = j
# # print(len(cars))

# # def drawmap():
# #     zbest = [20, 20, 23, 20, 20, 23, 26, 12, 3, 11, 11, 1, 8, 8, 12, 2, 11, 11, 0, 15, 1, 12, 0, 12, 12, 12, 2, 12]



# #     # plt.plot(list(range(self.maxgen)), self.trace)
# #     design = defaultdict(list)
# #     for i in range(len(psgs)):
# #         design[zbest[i]].append(i)


# #     for car, psg in design.items():
        
# #         px = [cars[car][0]]
# #         py = [cars[car][1]]
# #         for ps in psg:
# #             px.append(psgs[ps][0])
# #             px.append(cars[car][0])
# #             py.append(psgs[ps][1])
# #             py.append(cars[car][1])
        
# #         plt.plot(px, py)
    
# #     plt.scatter([p[0] for p in psgs], [p[1] for p in psgs], c = 'blue')
# #     plt.scatter([p[0] for p in cars], [p[1] for p in cars], c = 'red')
# #     for i, num in enumerate(gp):
# #         plt.text(psgs[i][0] + 0.0001, psgs[i][1] + 0.0001, num)
# #     for i, num in enumerate(gc):
# #         plt.text(cars[i][0] + 0.0001, cars[i][1] + 0.0001, num)
# #     plt.scatter(end[0], end[1])

# #     plt.show()
    

# # drawmap()

# # px = np.array([0, 0])
# # choosed = [1,1,1,1,1]
# # unchoo = np.where(choosed)[0]
# # for x in unchoo:
# #     # print(psgs[x])
# #     print(np.sqrt(np.sum((px - np.array(psgs[x]))**2)))
# # a = sorted(unchoo, key = lambda x: np.sqrt(np.sum((px - np.array(psgs[x]))**2)))
# # print(a)

# # px = np.array([103.9137, 30.5937])
# # print(np.sqrt(np.sum((px - np.array([104.0503, 30.6521]))**2))*1e5)

# # import itertools
# # print(list(itertools.permutations([2,3,4,6])))

# # a = np.where([0,1,0,1])[0]
# # b = np.delete(a, np.random.randint(len([])))

# # print(b)
# # print(a)

# a = [1,2,3,4]
# b = a[:]
# b[0] = 3
# print(a)


# def ss():
#     for i in range(10):
#         yield i
# s = ss()
# print(next(s))

import numpy as np
# print(next(s))
a = np.array([2,3,4,5,6])


print(a[[3,4,1]])

