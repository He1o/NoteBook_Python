def sort_bubble_(list):  # 写的不对，本质还是选择排序，并进行了不必要的交换
    for i in range(len(list) - 1):
        for j in range(i + 1, len(list)):
            if list[i] > list[j]:
                temp = list[j]
                list[j] = list[i]
                list[i] = temp
    return list

def sort_bubble(list):  # 
    for j in range(1, len(list)):
        for i in range(len(list) - j):
        
            if list[i] > list[i + 1]:
                temp = list[i + 1]
                list[i + 1] = list[i]
                list[i] = temp
    return list

a = [83, 73, 23, 55, 75, 234, 2, 6, 164, 92]
print(sort_bubble(a))
