def hee(a, b):
    b = 5

c = 1
d = 2
hee(c,d)
print(d)  #2  不可改变


def hee_2(a, b):
    b[0] = 5

c = 1
d = [2, 3, 4]
hee_2(c,d)
print(d)  #[5, 3, 4]  地址引用 可改变