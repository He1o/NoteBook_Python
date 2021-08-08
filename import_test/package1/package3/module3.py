from .. import module1
# 相对导入只能从上一级目录使用
# 即主函数运行的所在文件位置无法使用相对导入
# 即此文件的上级目录不能和主函数同级
# from package1 import module1

def out():
    module1.out()