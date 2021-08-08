import numpy as np

def sort_selection(list):
    for i in range(len(list) - 1):
        l_min = list[i]
        inx_min = i
        for j in range(i + 1, len(list)):
            if list[j] < l_min :
                l_min = list[j]
                inx_min = j
        temp = list[i]
        list[i] = l_min
        list[inx_min] = temp
    return list  #  并不需要l_min, 只需要下标索引j就可以了

a = [83, 73, 23, 55, 75, 234, 2, 6, 164, 92]
print(sort_selection(a))

