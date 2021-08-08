import numpy as np

def pos_array_to_pos_mat(pos_array):
  x = round((pos_array[0] - (-10)) / 20 * 100) 
  y = round((pos_array[1] - (-10)) / 20 * 100) 
  mat = np.zeros((100,100))
  mat[x,y] = 1
  return mat

mat = pos_array_to_pos_mat([2.4,5.6])
mat = mat[:,np.newaxis]
mat = mat.reshape(100,100,1)
print(mat[69,78,0])