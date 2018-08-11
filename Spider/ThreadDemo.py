# 多线程Demo

# 导入模块
import threading

class A(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        print("A 初始化")

    def run(self):
        for i in range(100):
            print("我是线程A")

class B(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        print("B 初始化")

    def run(self):
        for i in range(100):
            print("我是线程B")

a = A()
b = B()
a.start()
b.start()
