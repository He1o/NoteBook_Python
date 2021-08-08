fun = lambda x,y,z,e:(x -y -z -e) * 100

a = fun(*(2,3,5,7))
b = []
b += fun(*(2,3,5,7))
print(b)