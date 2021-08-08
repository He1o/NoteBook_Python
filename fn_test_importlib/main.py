import sys
import os
import importlib

BASE_DIR = os.path.dirname(__file__)
BASE_DIR = os.path.dirname(BASE_DIR)
# print(BASE_DIR)
sys.path.append(BASE_DIR + "/import_test")
# d:/Python_new/Python_test/import_test

import package1

print(package1.module1)  #<module 'package1.module1' from 'd:/Python_new/Python_test/import_test\\package1\\module1.py'>
print(package1.module1.module1)  #<class 'package1.module1.module1'>
print(package1.module1.module1())  #<package1.module1.module1 object at 0x000002C7A59BC6A0>
a = importlib.import_module('package1.module1')  
print(a) ##<module 'package1.module1' from 'd:/Python_new/Python_test/import_test\\package1\\module1.py'>

b = getattr(a, 'module1')  #<class 'package1.module1.module1'>
# module1（class）是module1的一个属性 
print(b)