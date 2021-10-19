from time import ctime, time # 导入time模块中的ctime方法
from os import system # 导入os模块中的system方法


def get_time():
    """ 获取当前时间 """
    return ctime() # 获取当前时间并返回到函数调用处

def create_git_order(time):
    """ 生成git指令并执行 """
    order_arr = ["git add *","git commit -m " + '"' + time + '"',"git push origin master"] # 创建指令集合
    for order in order_arr:
        system(order) # 执行每一项指令

def put_file(time):
    """ 在桌面放置文件 """
    file = open(r"C:\Users\HKplus\Desktop\git_push_time.txt","w") # 此处的路径根据自己实际需求配置
    file.write(time + "完成最后一次提交")

if __name__ == "__main__":
    date = get_time() # 获取时间
    create_git_order(date) # 提交到git
    put_file(date) # 在桌面创建文件