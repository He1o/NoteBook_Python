import os
import sys
import json
import code
# print(os.path.abspath('.'))
# print(sys.path)
# with open('/'.join([sys.path[0],'data/d.json']), 'w') as file_obj:
#     json.dump([2,3,4], file_obj, indent = 4)


# with open('path_test/data/d.json', 'w') as file_obj:
#     json.dump([6,3,4], file_obj, indent = 4)

code.c



'''
一个很重要的问题！！！！！！！
相对路径不是相对于你写代码的那个文件
而是相对于终端目录的
如果在Python-NoteBook路径下运行这个main.py文件
那么在这个工作区中无论哪个文件写相对路径的时候相对的都是/Python-NoteBook
而不是相对于main所在的目录/Python-NoteBook/path_test/main.py
因此如果要运行某个文件，一定要进入到正确的文件夹中
例如在终端中，如果在根目录下运行就不会成功
python Python-NoteBook/path_test/main.py
必须
cd Python-NoteBook
python path_test/main.py

'''