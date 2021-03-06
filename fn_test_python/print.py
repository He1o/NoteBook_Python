# print(*objects, sep=' ', end='\n', file=sys.stdout)

#sep设置间隔符
print('he','as','bb', sep = '+')  #he+as+bb
print('he','as','bb') #he as bb
print('he''as''bb') #heasbb


#   %c	 格式化字符及其ASCII码
#   %s	 格式化字符串
#   %d	 格式化整数
#   %u	 格式化无符号整型
#   %o	 格式化无符号八进制数
#   %x	 格式化无符号十六进制数
#   %X	 格式化无符号十六进制数（大写）
#   %f	 格式化浮点数字，可指定小数点后的精度
#   %e	 用科学计数法格式化浮点数
#   %E	 作用同%e，用科学计数法格式化浮点数
#   %g	 %f和%e的简写
#   %G	 %f 和 %E 的简写
#   %p	 用十六进制数格式化变量的地址
# %标记转换说明符的开始
a = 'heao'
b = 22
print('%s is %d years old' %(a,b))  #heao is 22 years old


# 最小字段宽度：转换后的字符串至少应该具有该值指定的宽度。如果是*（星号），则宽度会从值元组中读出。
# 点(.)后跟精度值：如果需要输出实数，精度值表示出现在小数点后的位数。如果需要输出字符串，
# 那么该数字就表示最大字段宽度。如果是*，那么精度将从元组中读出。
a = 3.25744897
print('%10.3f' %a)  #     3.257

'''
*	定义宽度或者小数点精度,从后面元组中进行读取
-	用做左对齐
+	在正数前面显示加号( + )
<sp>	在正数前面显示空格
#	在八进制数前面显示零('0')，在十六进制前面显示'0x'或者'0X'(取决于用的是'x'还是'X')
0	显示的数字前面填充'0'而不是默认的空格
%	'%%'输出一个单一的'%'
(var)	映射变量(字典参数)
m.n.	m 是显示的最小总宽度,n 是小数点后的位数(如果可用的话)
'''
print('%-10.3f' %a)  #3.257    '%-10.3f'是格式控制符，(8,a)是转换说明符
print('%+10.3f' %a)  #    +3.257
print('%010.3f' %a)  #000003.257
print('%0*.3f' %(8,a))  #0003.257
print('%0*.*f' %(8,4,a))  #003.2574

for i in range(10):
    print(i, end = '')
for i in range(10):
    print(i, end = ' ')   #01234567890 1 2 3 4 5 6 7 8 9

# f = open(r"F:\text.txt","w")    # 打开文件，以便写入
# print('test',file = f)  # 输出到文件
# f.close()   # 关闭文件