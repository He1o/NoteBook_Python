from contextlib import contextmanager
import time

''' example1 '''
class MyResource:
    #with语句中的代码块执行前, 会执行__enter__, 返回的值将赋值给with句中as后的变量. 
    def __enter__(self):
        print('connect to resource')
        return self
    #with语句中的代码块执行结束或出错, 会执行_exit__
    def __exit__(self, exc_type, exc_value, tb):
        print('close resource conection')

    def query(self):
        print('query data')

with MyResource() as r:
    r.query()

''' example2 '''
class MyResource2:
    def query(self):
        print('query data')

@contextmanager
def make_myresource():
    print('start to connect')
    yield MyResource2()  #as return , return the next option behind it
    print('end connect')
    pass

with make_myresource() as f:
    f.query()

''' example3 '''
@contextmanager
def timer(name):
    start = time.time()
    yield
    end = time.time()
    print('{} COST:{}'.format(name, end - start))

with timer('Timer Monte Carlo Iter'):
    print("*"*20)
