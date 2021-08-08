# 回调函数

# 你到一个商店买东西，刚好你要的东西没有货，于是你在店员那里留下了你的电话，过了几天店里有货了，店员就打了你的电话，然后你接到电话后就到店里去取了货。在这个例子里，你的电话号码就叫回调函数，你把电话留给店员就叫登记回调函数，店里后来有货了叫做触发了回调关联的事件，店员给你打电话叫做调用回调函数，你到店里去取货叫做响应回调事件。

# code 只是对行为的一种描述，比如有个机器人可以开灯，关灯，扫地。如果跟机器人约定好，0 表示开灯，1 表示关灯，2 表示扫地。我发出指令串，0 1 2，就可以控制机器人开灯，关灯，扫地。再约定用二进制表示，两位一个指令，就有一个数字串，000111，这个时候 000111 这串数字就描述了机器人的一系列动作，这个就是从一方面理解是 code，它可以控制机器人的行为。但另一方面，它可以传递，可以记录，可以修改，也就是数据。只要大家都协商好，code 就可以编码成 data, 将 data 解释运行的时候，也变成了 code。code 和 data 可以不用区分，统一称为信息。既然 int max(int a, int b) 中 int，double 等表示普通 data 的东西可以传递进去，自然表示 code 的函数也可以传进去了。
# 有些语言确实是不区分的，它的 function(表示code)跟 int, double 的地位是一样的。这种语言就为函数是第一类值。
# 而有些语言是不能存储函数，不能动态创建函数，不能动态销毁函数。只能存储一个指向函数的指针，这种语言称为函数是第二类值。
# 另外有些语言不单可以传递函数，函数里面又用到一些外部信息(包括code, data)。那些语言可以将函数跟函数所用到的信息一起传递存储。这种将函数和它所用的信息作为一个整体，就为闭包。

from collections import defaultdict


# log_missing 即为回调函数也为挂钩函数
def log_missing():
    print('key addad')
    return 2
heao = defaultdict(log_missing)
heao['hh']
# print(heao)  #defaultdict(<function log_missing at 0x0000018F0A43C1E0>, {'hh': 2})
# print(heao['hh'])  #2
# 提供log_missing 这样的函数，可以使API构建更加容易，也更易测试，因为它能把附带的效果和确定行为分隔开 e5c07b

# 实现功能统计该字典一共遇到多少个缺失的键
# 方法1 闭包
def increment_with_report(current, increments):
    added_count = 0
    def missing():
        nonlocal added_count 
        added_count += 1
        return 0
    result = defaultdict(missing, current)
    for key, amount in increments.items():
        result[key] += amount

    return result, added_count
current = {'heao': 23}
increments = {'heao': 5, 'her': 50}
result, count = increment_with_report(current, increments)
# print(result)  # {'heao': 28, 'her': 50}

# 方法2 小型类
class countMissing(object):
    def __init__(self):
        self.added = 0

    def missing(self):
        self.added += 1
        return 0

counter = countMissing()
result = defaultdict(counter.missing, current)

for key, amount in increments.items():
    result[key] += amount
# print(result) # {'heao': 28, 'her': 50}

# Countmissing对象由谁来构建？missing方法由谁来调用？该类以后是否要添加新的公共方法
# 方法3 利用__call__的特殊方法
class BetterCountMissing(object):
    def __init__(self):
        self.added = 0

    def __call__(self):
        self.added += 1
        return 0

counter = BetterCountMissing()
# print(counter())  # 0
# print(callable(counter))  # True
result = defaultdict(counter, current)
for key, amount in increments.items():
    result[key] += amount
# print(result) # {'heao': 28, 'her': 50}

