from . import module1  #相对导入，只导入该文件位置的module
from .package3 import module4
class module2():
    pass

module1.out()