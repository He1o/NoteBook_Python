# yield 的用法有以下四种常见的情况：一个是生成器，二是用于定义上下文管理器，三是协程，四是配合 from 形成 yield from 用于消费子生成器并传递消息。这四种用法，其实都源于 yield 所具有的暂停的特性，也就说程序在运行到 yield 所在的位置 result = yield expr 时，先执行 yield expr 将产生的值返回给调用生成器的 caller，然后暂停，等待 caller 再次激活并恢复程序的执行。而根据恢复程序使用的方法不同，yield expr 表达式的结果值 result 也会跟着变化。如果使用 __next()__ 来调用，则 yield 表达式的值 result 是 None；如果使用 send()来调用，则 yield 表达式的值 result 是通过 send 函数传送的值。

# 可迭代对象
# 迭代器（iterator） 生成器（generator）
# 序列 字符串str 列表list 元组tuple 集合set
# 字典
def index_words(text):
    result = []
    if text:
        result.append(0)
    for index, letter in enumerate(text):
        if letter == ' ':
            result.append(index + 1)
    return result

def index_words_iter(text):
    if text:
        yield 0
    for index, letter in enumerate(text):
        if letter == ' ':
            yield index + 1

address = 'four sfdk skfj wer wet...'
result = index_words(address)
print(result[:3])

rusult = list(index_words_iter(address))