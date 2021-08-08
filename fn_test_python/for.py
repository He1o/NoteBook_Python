for a  in []:
    if a >0:
        print(1)

l = [ 2, 3, 4]
for a in l:  #a是int不可变对象
    a = 2
print(l)  #[2, 3, 4]

l = [ [2], [3], [4]]
for a in l:  #a是list 可变对象
    a[0] = 0
print(l)   #[[0], [0], [0]]

var = [3]
var[0] = 1 if var[0] == 0 else 1
print(var)

l = [ [2], [3], [4]]
a = (ll == 2 for ll in l)
print(all(a))