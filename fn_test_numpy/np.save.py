import numpy as np
'''
numpy.save(file, arr, allow_pickle=True, fix_imports=True)
file:文件名/文件路径
arr:要存储的数组
allow_pickle:布尔值,允许使用Python pickles保存对象数组(可选参数,默认即可)
fix_imports:为了方便Pyhton2中读取Python3保存的数据(可选参数,默认即可)
'''
a = [[1,2,3,4]]
# np.save('D:\\Python_new\\Python_test\\data\\he.npy',a)

'''
numpy.savez(file, *args, **kwds)
file:文件名/文件路径
*args:要存储的数组,可以写多个,如果没有给数组指定Key,Numpy将默认从'arr_0','arr_1'的方式命名
kwds:(可选参数,默认即可)
'''
#生成数据 
# x=np.arange(10) 
# x 
# array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) 
# y=np.sin(x) 
# y 
# array([ 0.  , 0.84147098, 0.90929743, 0.14112001, -0.7568025 , 
#   -0.95892427, -0.2794155 , 0.6569866 , 0.98935825, 0.41211849]) 
   
# #数据保存 
# np.save('save_xy',x,y) 

# #读取保存的数据 
# npzfile=np.load('save_xy.npz') 
# npzfile #是一个对象,无法读取 
# <numpy.lib.npyio.NpzFile object at 0x7f63ce4c8860> 
  
# #按照组数默认的key进行访问 
# npzfile['arr_0'] 
# array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) 
# npzfile['arr_1'] 
# array([ 0.  , 0.84147098, 0.90929743, 0.14112001, -0.7568025 , 
#   -0.95892427, -0.2794155 , 0.6569866 , 0.98935825, 0.41211849])


'''
numpy.savetxt(fname, X, fmt='%.18e', delimiter=' ', newline='\n', header='', footer='', comments='# ', encoding=None)
fname:文件名/文件路径,如果文件后缀是.gz,文件将被自动保存为.gzip格式,np.loadtxt可以识别该格式
X:要存储的1D或2D数组
fmt:控制数据存储的格式
delimiter:数据列之间的分隔符
newline:数据行之间的分隔符
header:文件头步写入的字符串
footer:文件底部写入的字符串
comments:文件头部或者尾部字符串的开头字符,默认是'#'
encoding:使用默认参数

numpy.loadtxt(fname, dtype=<class 'float'>, comments='#', delimiter=None, converters=None, skiprows=0, usecols=None, unpack=False, ndmin=0, encoding='bytes')
fname:文件名/文件路径,如果文件后缀是.gz或.bz2,文件将被解压,然后再载入
dtype:要读取的数据类型
comments:文件头部或者尾部字符串的开头字符,用于识别头部,尾部字符串
delimiter:划分读取上来值的字符串
converters:数据行之间的分隔符
'''
# np.savetxt('D:\\Python_new\\Python_test\\data\\he.out',a)
# np.savetxt('D:\\Python_new\\Python_test\\data\\he.out',a, header='abcd', fmt='%d')
# a = np.loadtxt('D:\\Python_new\\Python_test\\data\\he.out', dtype=int,comments  ='#')

# 在文件中读取二进制数据，或向其中写入二进制数据时，总应该以'rb'或'wb'等二进制模式开启文件


# r   以只读方式打开文件。文件的指针将会放在文件的开头。这是默认模式。
# rb  以二进制格式打开一个文件用于只读。文件指针将会放在文件的开头。这是默认模式。
# r+  打开一个文件用于读写。文件指针将会放在文件的开头。
# rb+ 以二进制格式打开一个文件用于读写。文件指针将会放在文件的开头。
# w   打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
# wb  以二进制格式打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
# w+  打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
# wb+ 以二进制格式打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
# a   打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
# ab  以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
# a+  打开一个文件用于读写。如果该文件已存在，文件指针将会放在文件的结尾。文件打开时会是追加模式。如果该文件不存在，创建新文件用于读写。
# ab+ 以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。如果该文件不存在，创建新文件用于读写。

with open('D:\\Python_new\\Python_test\\data\\he.out','ab') as f: 
    for i in range(5):                              
     newresult = [[6,3,4,5,4,5]]
     np.savetxt(f, newresult, delimiter=" ", header='abcd', fmt='%d') 