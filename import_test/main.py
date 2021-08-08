import package1
from package1 import module2
import sys
import os

# print("\n".join(sys.path))   
# 它是一个list.默然情况下python导入文件或者模块的话，
# 他会先在sys.path里找模块的路径。如果没有的话,程序就会报错。
# 第一项为脚本的位置
# 第二项为lib目录下(home目录\pythonXX\lib)
# 第三项为lib目录下的site-package目录下(home目录\pythonXX\lib\site-packages)

# d:\\Python_new\\Python_test\\import_test
# D:\\软件\Python\\python37.zip
# D:\\软件\Python\\DLLs
# D:\\软件\Python\\lib
# D:\\软件\\Python
# C:\\Users\\heao\\AppData\\Roaming\\Python\\Python37\\site-packages
# D:\\软件\\Python\\lib\\site-packages
# D:\\软件\\Python\\lib\\site-packages\\win32
# D:\\软件\\Python\\lib\\site-packages\\win32\lib
# D:\\软件\\Python\\lib\\site-packages\\Pythonwin


BASE_DIR = os.path.dirname(__file__)
# print(BASE_DIR)
sys.path.append(BASE_DIR + "/package1")
# d:/Python_new/Python_test/import_test

print("\n".join(sys.path))