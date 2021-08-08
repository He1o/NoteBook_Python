import numpy as np

a = np.mat([[1, 2, 2],
            [2, 3, 4]])
b = a.A # .A将matrix转换为array  
# print(a * a.T)  #[[ 9 16] [16 29]]
# print(b * b)  #[[ 1  4  4] [ 4  9 16]]
# print(type(a), type(b))

# print(a == 2)  #[[False  True  True] [ True False False]]
# print(b == 2)  #[[False  True  True] [ True False False]]

# print(np.nonzero(a == 2))  #(array([0, 0, 1], dtype=int64), array([1, 2, 0], dtype=int64))
# print(np.nonzero(b == 2))  #(array([0, 0, 1], dtype=int64), array([1, 2, 0], dtype=int64))




a = np.array(
    [
        [1,2],
        [2,3],
        [1,2],
        [2,4]
    ]
)
print(sum(a[:,0] == 1))