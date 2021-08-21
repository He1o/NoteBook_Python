'''
any(iterable)

如果 iterable 的任一元素为真值则返回 True。 如果可迭代对象为空，返回 False。 等价于:

def any(iterable):
    for element in iterable:
        if element:
            return True
    return False
'''

lis1 = [0, 2, 0, 0]
print(any(lis1)) # True