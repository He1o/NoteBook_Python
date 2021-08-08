import package1.package3 

package1.package3.module3.out()
# AttributeError: module 'package1.package3' has no attribute 'module3'
# package3 包的init文件必须要导入模块module3 
# 否则 只能用main2的方法