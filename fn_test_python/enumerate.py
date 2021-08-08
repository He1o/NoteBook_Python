a = ['bobo','i','miss','you']

for i, word in enumerate(a):
    print(i,word)

for i, word in enumerate(a, 1):  #指定初始计数值，从1开始
    print(i,word)


a = ['bobo','i','miss','you']
b = ['please', 'don\'t', 'leave', 'me']

for i, word in enumerate(zip(a,b)):
    print(i,word)