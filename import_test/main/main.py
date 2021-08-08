import sys
import os
BASE_DIR = os.path.dirname(__file__)  #返回所在目录
BASE_DIR = os.path.dirname(BASE_DIR)  #返回上一级目录
print(BASE_DIR)
sys.path.append(BASE_DIR)

import package1
from package1 import module1

