import numpy as np

def bobo(a,b):
    return sum(a)*b

c = np.vectorize(bobo, excluded=['a'])  
#excluded == not vectorize 
#put every element of a list or array into the function

print(c(a = [2,3,4],b = [9,4,6]))  #[81 36 54]
