def binarySearch(target, sortedLyst, left, right ):
    mid = (left + right) // 2
    if sortedLyst[mid] == target:
        return mid
    elif sortedLyst[mid] < target:
        left =  mid
        ans = binarySearch(target, sortedLyst, left, right)
    else:
        right = mid
        ans = binarySearch(target, sortedLyst, left, right)
    return ans
    
a = [1,5,9,13,34,67,89,134,156,178]
print(binarySearch(1, a, 0 ,len(a)))


# 存在bug，不需要递归，可以用while left < right