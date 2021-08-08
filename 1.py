# 原来有一个非常长的有序数组。尾部一段元素被截取放到了头部。例如 [19, 20, 100, 888, -1, 3, 8, 10, 11, 15, 18] 。写代码找出新数组的最小值。

def findmin(nums):
    i, j = 0, len(nums) - 1
    while i <= j:
        mid = (i + j) // 2
        if nums[i] <= nums[mid - 1] and nums[mid] <= nums[j]:
            return nums[mid]
        
        if nums[i] <= nums[mid]:
            i = mid + 1
        else:
            j = mid - 1
    return nums[i - 1]
nums = [19, 20, 100, 888, 11, 15, 18]
print(findmin(nums))