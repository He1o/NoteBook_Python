'''
all(iterable)

如果 iterable 的所有元素均为真值（或可迭代对象为空）则返回 True 。 等价于:

def all(iterable):
    for element in iterable:
        if not element:
            return False
    return True
'''

a = [1,2,3,0]
print(all(a)) # False

l = [[2], [3], [4]]
a = (ll == 2 for ll in l)
print(a) # False
print(all(a)) # <generator object <genexpr> at 0x1053e1ac0>
print(all(l)) # True
