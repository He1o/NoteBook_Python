import numpy as np

a = [
    [26,3,5],
    [3,56,8],
    [6,999,85],
    [676,99,85],
]
# print(np.argmax(a))
# print(np.argmax(a, axis = 0))  #[3 2 2]
# print(np.argmax(a, axis = 1))  #[0 1 1 0]
# print(np.argmax(a, axis = -1))  #[0 1 1 0]


#把矩阵想象成里外，axis越大相当于越里层，shape(4,3)  

print(np.inf < np.inf)