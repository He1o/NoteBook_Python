def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError as e:
        raise ValueError('Invalid inputes') from e
        # return None
        # 尽量用异常来表示特殊情况 而不要返回None
# During handling of the above exception, another exception occurred:  不用from
# The above exception was the direct cause of the following exception:  用from

x, y = 2, 0
divide(x,y)