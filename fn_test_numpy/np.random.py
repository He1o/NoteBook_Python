import numpy as np
import random

# a = 5  == np.range(5) = [0, 1, 2, 3, 4, 5]
bobo = np.random.choice(5, size = 5, replace = False)  #[1 4 0 2 3]
bobo = np.random.choice(5, size = 5, replace = True)  #[1 2 0 1 3]
bobo = np.random.choice(5, size = 3, p=[0.1, 0, 0.3, 0.6, 0])  #[3 3 3]
a = [[2,3], [4,5], [9,2], [0,2,4]]
bobo = np.random.choice(a, size = 3, p=[0.1, 0, 0.3, 0.6]) #[list([0, 2, 4]) list([9, 2]) list([2, 3])]

bobo = random.sample(a, 1)  #[9,2]
bobo = random.random()  #0.5866477110482269  no arguments

bobo = np.random.normal(loc=0.0, scale=1.0, size=(2,3))  # mu, sigma (-3sig,3sig)=99%
# print(bobo)
bobo = np.random.exponential(scale = 1, size = 10)  #Exponential Distribution rate=lamda


bobo = np.random.uniform(low=0, high=3, size=(3,2))



bobo = np.random.rand(3,2).astype(np.float32)  # 3rows,2columns, scale[0,1) d1,d2,d3
# print(bobo)
bobo = np.random.rand(3).astype(np.float32)  # [0.58645475 0.416789 0.17292345]

bobo = np.random.randn(3).astype(np.float32)  # standard normal distribution

bobo = np.random.randint(low=0, high=3, size=100, dtype=np.int32)  # int



seed = 1  #@param{type: 'integer'}
rand = np.random.RandomState(seed=seed)
rand = np.random.RandomState(seed=seed)




bobo = np.random.randint(low=0, high=359, size=1, dtype=np.int32)  # int

print(bobo)

# SEED = 1
# np.random.seed(SEED)

print(np.random.randint(2))

 