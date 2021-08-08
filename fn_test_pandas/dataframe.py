import numpy as np
import pandas as pd
import os
a = os.getcwd() #获取当前工作路径
print(a)


test_1 = pd.DataFrame(np.random.rand(4, 4),
        index=list('ABCD'), columns=list('1234'))  # 产生随机数,index行,columns列
test_2 = pd.DataFrame([[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7]],
                      index=list('1234'), columns=list('ABCD'))  # 自己输入
dic1 = {'name': ['小明', '小红', '狗蛋', '铁柱'],
        'age': [17, 20, 5, 40], 'sex': ['男', '女', '女', '男']}  # 使用字典进行输入
test_3 = pd.DataFrame(dic1, index=list('ABCD'))

# pd.set_option('display.unicode.ambiguous_as_wide', True)
# pd.set_option('display.unicode.east_asian_width', True)
# pd.set_option('display.width', 180) # 设置打印宽度(**重要**)
# pd.set_option('expand_frame_repr', False) #数据超过总宽度后，是否折叠显示

# print(test_1, '\n')
# print(test_2, '\n')
# print(test_3, '\n')


for _ in range(5):
    test_3.to_csv('data\\he.out',mode = 'a', sep = ' ')
        