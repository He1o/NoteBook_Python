import os
import sys
import json
# print(os.path.abspath('.'))
# print(sys.path)
# with open('/'.join([sys.path[0],'data/d.json']), 'w') as file_obj:
#     json.dump([2,3,4], file_obj, indent = 4)


with open('path_test/data/d.json', 'w') as file_obj:
    json.dump([9,3,4], file_obj, indent = 4)