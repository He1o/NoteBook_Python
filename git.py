from time import ctime, time # 导入time模块中的ctime方法
from os import system # 导入os模块中的system方法




def git_push(repository):
    currtime = ctime()
    order_arr = ['cd {}'.format(repository)]
    order_arr.append("git add -A")
    order_arr.append("git commit -m " + '"' + currtime + '"'), 
    order_arr.append("git push")
    for order in order_arr:
        system(order) 


    with open('/Users/renren/git_push/git_record.txt', 'a') as f:
        f.write('time: {} {}'.format(currtime, repository))


def main():
    repositories = [
        '/Users/renren/NoteBook/NoteBook_Python',
        '/Users/renren/NoteBook/NoteBook_MySQL',
        '/Users/renren/NoteBook/NoteBook_LeetCode',
        '/Users/renren/NoteBook/NoteBook_HTML',
        '/Users/renren/NoteBook/Cyrus_NoteBook',
    ]
    for rep in repositories:
        git_push(rep)

if __name__ == "__main__":
    main() #