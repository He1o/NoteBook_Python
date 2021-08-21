# range

def sqrt(num):
    left = 0
    right = num
    while True:
        mid = (left + right) / 2

        if abs(mid * mid * mid - num) < 1e-6:
            break
        if mid * mid * mid > num:
            right = mid - 0.000001
        else:
            left = left + 0.000001


    return mid

print(sqrt(6))


flag[0] = 1
