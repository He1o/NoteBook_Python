import numpy as np

a = np.arange(5) # a.shape=(5,)
b = a[np.newaxis, :] # b.shape=(1,5)
c = a[:,np.newaxis] # c.shape=(5,1)
d = a[:,np.newaxis,np.newaxis] # d.shape=(5,1,1)
e = a[np.newaxis, np.newaxis, :] # e.shape=(1,1,5)
print('a = ',a)
print('b = ',b)
print('c = ',c)
print('d = ',d)
print('e = ',e)


a = np.arange(6).reshape(2, 3)  # a.shape=(2,3)
b = a[:, np.newaxis]  # b.shape=(2,1,3)
c = a[:, np.newaxis, :]  # c.shape=(2,1,3)
d = a[..., np.newaxis]  # d.shape=(2,3,1)
e = a[np.newaxis, ...]  # e.shape=(1,2,3)
print('a = ', a)
print('b = ', b)
print('c = ', c)
print('d = ', d)
print('e = ', e)
