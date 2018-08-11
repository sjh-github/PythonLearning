# 读取变量
# name = input("请输入你的名字：")
# print("Hello", name)

# 多行换行输出
# print('''line1
# line2
# line3''')

# n = 123
# f = 456.789
# s1 = "Hello, world"
# s2 = "Hello, \'Adam\'"
# s3 = r"Hello, 'Bart'"
# s4 = r'''Hello,
# Lisa!'''
# print(n)
# print(f)
# print(s1)
# print(s2)
# print(s3)
# print(s4)

# 字符编码为bytes以及bytes解码为字符
# print("ABC".encode("ascii"))
# print("中文".encode("utf-8"))
# print(b"ABC".decode("ascii"))
# print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))

# 格式化输出(%)或format
# print("Hello %s, your account is $%d" % ("SJH",1000))
# s1 = 72
# s2 = 85
# r = (s2 - s1)/s1 * 100
# print("成绩提升了%.1f%%" % r)
# print("{0}成绩提升了{1:.1f}%".format('小明',r))

# list有序集合
# roommates = ["石佳豪", "黄结", "企鹅", "许苏韬", "茂茂"]
# print("I have", len(roommates), "个室友：", roommates)
# print("first:", roommates[0])
# print("lase:", roommates[-1])
# roommates.append("someone")
# print("I have", len(roommates), "个室友：", roommates)
# roommates.insert(0, "one")
# print("I have", len(roommates), "个室友：", roommates)
# classmates = ["Student1", "Student2", ["S31", "S32"], "Student4"]
# print(classmates[2][1])

# tuple元组（初始化后不可修改）
# 只有一个元素时，需要添加逗号
# t = (1,)
# print(t)
# L = [
#      ['Apple', 'Google', 'Microsoft'],
#      ['Java', 'Python', 'Ruby', 'PHP'],
#      ['Adam', 'Bart', 'Lisa']
#     ]
# print(L[0][0])
# print(L[1][1])
# print(L[2][2])

# if
# height = 1.75
# weight = 80.5
# bmi = weight / (height ** 2)
# print("bmi =", bmi)
# if bmi < 18.5:
#     print("过轻")
# elif 18.5 <= bmi < 25:
#     print("正常")
# elif 25 <= bmi < 28:
#     print("过重")
# elif 28 <= bmi < 32:
#     print("肥胖")
# else:
#     print("严重肥胖")

# 循环
# sum = 0
# for x in range(101):
#     sum = sum + x
# print("sum =", sum)

# sum = 0
# n = 0
# while n < 101:
#     sum = sum + n
#     n = n + 1
# print("sum =", sum)

# L = ['Bart', 'Lisa', 'Adam']
# for name in L:
#     print(name)

# dict 不变对象作为key
# d = {'SJH': 100, 'XST': 90, 'HJ': 95}
# print(d['SJH'])
# print('SJJ' in d)
# print(d.get('SJJ', '不存在'))
# d.pop('XST')
# print(d)

# set 传入list作为构造函数形参
# s = set([1, 1, 2, 3])
# print(s)
# s.add(5)
# s.remove(3)
# print(s)
# s2 = set([1, 2])
# print(s & s2)
# print(s | s2)

# t1 = (1, 2, 3)
# t2 = (1, [2, 3])
# d1 = {t1: 100}
# # d2 = {t2: 90} t2中包含list因而不能作为dict的key
# s1 = (t1)
# s2 = (t2)
# print(d1, s1, s2)

# 函数 hex()整数转为十六进制字符串
# n1 = 255
# n2 = 2000
# print(hex(n1))
# print(hex(n2))


# def my_abs(x):
#     if not isinstance(x, (int, float)):
#         raise TypeError("参数类型有误")
#     if x >= 0:
#         return x
#     else:
#         return -x


# print(my_abs(-1))


# import math


# def move(x, y, step, angle=0):
#     nx = x + step * math.cos(angle)
#     ny = y - step * math.sin(angle)
#     return nx, ny


# x, y = move(100, 100, 60, math.pi / 6)
# print(x, y)


# 默认参数
# def power(x, n=2):
#     s = 1
#     while n > 0:
#         n = n - 1
#         s = s * x
#     return s


# print(power(5))
# print(power(5, 3))


# 尽量使用None不变参数传参
# def add_end(L=None):
#     if L is None:
#         L = []
#     L.append('END')
#     return L


# print(add_end)


# 可变(个数)参数
# def cal(*numbers):
#     sum = 0
#     for n in numbers:
#         sum = sum + n * n
#     return sum


# print(cal(1, 2))
# print(cal(1, 2, 3))
# nums = (1, 2, 3)
# nums2 = [1, 2, 3]
# print(cal(*nums))
# print(cal(*nums2))


# 关键字参数（组装成dict）
# def person(name, age, **kw):
#     print('name:', name, 'age:', age, 'other:', kw)


# person('SJH', 21)
# person('Bob', 35, city='北京', job='程序员')
# extra = {'city': '杭州', 'job': 'HR'}
# person('Tom', 41, **extra)


# 命名关键字参数（*后限制关键字参数的名字）
# def person(name, age, *, city, job):
#     print(name, age, city, job)


# person('Bob', 20, city='杭州', job='HR')


# def product(*nums):
#     sum = 1
#     for n in nums:
#         sum = sum * n
#     return sum


# print(product(2))
# print(product(2, 3))
# print(product(2, 3, 4))


# 递归函数
# def fact(n):
#     if n == 1:
#         return 1
#     return n * fact(n - 1)


# print(fact(5))


# 汉诺塔
# def move(n, a, b, c):
#     if n == 1:
#         print(a, '-->', c)
#     else:
#         move(n - 1, a, c, b)
#         move(1, a, b, c)
#         move(n - 1, b, a, c)


# move(3, 'A', 'B', 'C')


# 切片
# L = list(range(100))
# print(L)
# print(L[2:5])
# print(L[:10])
# print(L[-10:])
# print(L[0:10:2])
# print(L[::5])

# print('ABCDEFG'[::2])
# print((0, 1, 2, 3, 4, 5)[:3])


# def trim(s):
#     while(s[:1] == ' '):
#         s = s[1:]
#     while(s[-1:] == ' '):
#         s = s[:-1]
#     return s


# print(trim('   SJH  '))


# 迭代
# d = {'a': 1, 'b': 2, 'c': 3}
# for key in d:
#     print(key)

# for value in d.values():
#     print(value)

# for k, v in d.items():
#     print(k, v)

# for ch in 'ABC':
#     print(ch)

# from collections import Iterable
# print(isinstance('abc', Iterable))
# print(isinstance(123, Iterable))

# for i, value in enumerate(['A', 'B', 'C']):
#     print(i, value)

# for x, y in [(1, 1), (2, 4), (3, 6)]:
#     print(x, y)


# def findMinAndMax(L):
#     if L is None or L == []:
#         return None, None
#     min = L[0]
#     max = L[0]
#     for num in L:
#         if num > max:
#             max = num
#         elif num < min:
#             min = num
#     return min, max


# print(findMinAndMax([]))


# 列表生成式
# print([x * x for x in range(1, 11)])
# print([x * x for x in range(1, 11) if x % 2 == 0])
# print([m + n for m in 'ABC' for n in 'XYZ'])
# print([s.lower() for s in ['Hello', 'World']])

# import os
# print([d for d in os.listdir('.')])

# L1 = ['Hello', 'World', 18, 'Apple', None]
# print([l.lower() for l in L1 if isinstance(l, str)])


# 生成器generator:yield以及列表生成式[]换为()
# g = (x * x for x in range(10))
# print(g)
# for n in g:
#     print(n)


# def fib(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         yield(b)
#         a, b = b, a+b
#         n = n + 1
#     return 'done'


# print(fib(10))
# for n in fib(6):
#     print(n)

# def triangles():
#     ls = [1]
#     i = 1
#     while i < 10:
#         i = i + 1
#         print(ls)
#         ls = [1] + [ls[i] + ls[i+1] for i in range(len(ls) - 1)] + [1]


# triangles()


# 高阶函数：一个函数接受领一个函数作为参数
# def add(x, y, f):
#     return f(x) + f(y)


# print(add(10, -2, abs))


# map返回惰性Iterator，接收函数作为第一个形参
# def f(x):
#     return x * x


# r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
# print(list(r))

# print(list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])))


# reduce:reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
# 把结果继续和序列的下一个元素做累积计算
# from functools import reduce


# def add(x, y):
#     return x * 10 + y


# print(reduce(add, [1, 3, 5, 7, 9]))

# from functools import reduce
# DIGGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}


# def str2int(s):
#     def fn(x, y):
#         return x * 10 + y

#     def char2num(s):
#         return DIGGITS[s]
#     return reduce(fn, map(char2num, s))


# print(str2int('12345'))


# def normalize(name):
#     if name is None:
#         return None
#     return name[0].upper() + name[1:].lower()
#

# L1 = ['adam', 'LISA', 'barT']
# L2 = list(map(normalize, L1))
# print(L2)


# from functools import reduce


# def prod(L):
#     return reduce(lambda x, y: x * y, L)


# print(prod([3, 5, 7, 9]))


# from functools import reduce


# def str2float(s):
#     higtInt = s.split('.')[0]
#     lowInt = s.split('.')[1][::-1]
#     return reduce(lambda x, y: x * 10 + y, list(map(int, higtInt))) + reduce(lambda x, y: x / 10 + y, list(map(int, lowInt))) / 10


# print(str2float('123.456'))


# filter过滤，返回Iterator惰性序列
# print(list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5])))
# print(list(filter(lambda s: s and s.strip(), ['A', '', None, ' '])))


# 打印素数
# def _init():
#     n = 1
#     while True:
#         n = n + 2
#         yield n


# def _not_divisiable(n):
#     return lambda x: x % n > 0


# def primes():
#     yield 2
#     it = _init()
#     while True:
#         n = next(it)
#         yield n
#         it = filter(_not_divisiable(n), it)


# for n in primes():
#     if n < 1000:
#         print(n)
#     else:
#         break


# 回数判断
# def is_palindrome(n):
#     return str(n) == str(n)[::-1]


# print(list(filter(is_palindrome, range(1, 1000))))


# sorted排序
# print(sorted([36, 5, -12, 9, -21]))
# print(sorted([36, 5, -12, 9, -21], key=abs))
# print(sorted([36, 5, -12, 9, -21], key=abs, reverse=True))


# def by_name(t):
#     return t[0].lower()


# def by_score(t):
#     return t[1]


# L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
# print(list(sorted(L, key=by_name)))
# print(list(sorted(L, key=by_score)))


# 返回函数,闭包


# 匿名函数
# L = list(filter(lambda n: (n % 2 == 1), range(1, 20)))
# print(L)


# 装饰器
# import functools


# def log(*text):
#     def decorator(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kw):
#             print("BEGIN...")
#             print('%s %s():' % (text, func.__name__))
#             print("END!!!")
#             return func(*args, **kw)
#         return wrapper
#     return decorator


# @log()
# def now():
#     print('2018-05-10')


# f = now
# f()
# print(now.__name__)


# 偏函数：使用functools.partial可以创建一个新的函数，这个新函数可以固定住原函数的部分参数，从而在调用时更简单。
# print(int('123456'))


# import functools
# int2 = functools.partial(int, base=2)
# print(int2('100000'))


# 类和实例(函数第一个参数永远是self)
# class Student(object):
#     def __init__(self, name, score):
#         self.__name = name
#         self.__score = score

    # def print_score(self):
    #     print("%s: %s" % (self.__name, self.__score))

# bart = Student('SJH', 100)
# bart.print_score()
# print(bart.__name)


# 继承和多态
# class Animal(object):
#     def run(self):
#         print('Animal is running...')

 # class Dog(Animal):
 #     def run(self):
 #         print('Dog is running...')
 #
 #     def eat(self):
 #         print('Dog is eating...')

# class Cat(Animal):
#     def run(self):
#         print('Cat is running...')


# def printAnimal(animal):
#     animal.run()
#
# class Timer(object):
#     def run(self):
#         print('Start...')
#
# dog = Dog();
# cat = Cat();
# dog.run();
# cat.run();
# printAnimal(Animal())
# printAnimal(Dog())
# printAnimal(Cat())
# printAnimal(Timer())

#实例计数
# class Student(object):
#     count = 0
#
#     def __init__(self, name):
#         self.name = name
#         Student.count = Student.count + 1
#
# a = Student('a')
# b = Student('b')
# print(Student.count)

# __slots__ 用于限制动态添加类的属性的范围
# class Student(object):
#     __slots__ = ('name', 'age')
#
# s = Student()
# s.name = 'SJH'
# s.age = 21
# print(s.name)


# @property 用于把类的方法变成属性调用的装饰器
# class Student(object):
#     @property
#     def score(self):
#         return self._score
#
#     @score.setter
#     def score(self, value):
#         if not isinstance(value, int):
#             raise ValueError('score必须为整数')
#         if value < 0 or value > 100:
#             raise ValueError('score 必须为 1~100')
#         self._score = value
#
# s = Student()
# s.score = 60
# print(s.score)
# s.score = 101

# 定制类
# class Student(object):
#     def __init__(self, name):
#         self.name = name
#
#     def __str__(self):
#         return 'Student object (name: %s)' % self.name
#
#     def __getattr__(self, attr):
#         if attr == 'score':
#             return 100
#
#     def __call__(self):
#         print('My name is %s.' % self.name)
#
#     __repr__ = __str__
#
# s = Student('SJH')
# print(s)
# print(s.name)
# print(s.score) #调用__getattr__
# s() #调用__call__


# 枚举
# from enum import Enum, unique
#
# Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
#
# for name, member in Month.__members__.items():
#     print(name, '->', member, ',', member.value)
#
#
# @unique
# class Weekday(Enum):
#     Sun = 0
#     Mon = 1
#     Tue = 2
#     Wed = 3
#     Thu = 4
#     Fri = 5
#     Sat = 6
#
# print(Weekday.Mon)
# print(Weekday['Tue'])
# for name, member in Weekday.__members__.items():
#     print(name, '->', member)


# 错误处理
# try:
#     print('try...')
#     r = 10 / 0
#     print('result:', r)
# except ZeroDivisionError as e:
#     print('except:', e)
# finally:
#     print('finally...')
# print('END')


# 调试(断言，日志)
# import logging
# logging.basicConfig(level = logging.INFO)
#
# def foo(s):
#     n = int(s)
#     logging.info('n = %d' % n)
#     assert n != 0, 'n is zero'
#     return 10 / n
#
# foo('0')


# 单元测试


# 文件读写
# with open('E://text.txt', 'r') as f:
#     for line in f.readlines():
#         print(line.strip())

# with open('E://图片//照片photo.png', 'rb') as f:
#     print(f.read())

# with open('E://text.txt', 'a') as f:
#     f.write('Hello, World, My name is 石佳豪')


# StringIO和BytesIO
# from io import StringIO
# f = StringIO()
# print(f.write('HELLO'))
# print(f.write('WORLD'))
# print(f.getvalue())
#
# f = StringIO('Hello\nHI!\nGoodBye')
# while True:
#     s = f.readline()
#     if s == '':
#         break
#     print(s.strip())

# from io import BytesIO
# f = BytesIO()
# f.write('中文'.encode('utf-8'))
# print(f.getvalue())

# 操作文件和目录
# import os
# print(os.path.abspath('.'))
# print(os.path.join('E://', 'test.txt'))
# os.mkdir('E://sjh')
# os.rmdir('E://sjh')
# print(os.path.split('E://text.txt'))
# print(os.path.splitext('E://text.txt'))
# os.rename('E://text.txt', 'E://test.txt')
# os.remove('E://test.txt')

# 序列化
# import pickle
# d = dict(name='SJH', age=20, score=100)
# print(pickle.dumps(d))
# with open('E://pickle.txt', 'wb') as f:
#     pickle.dump(d, f)

# with open('E://pickle.txt', 'rb') as f:
#     db = f.read()
# d = pickle.loads(db)
# print(d)

# with open('E://pickle.txt', 'rb') as f:
#     d = pickle.load(f)
#     print(d)


# JSON
# import json
# d = dict(name='Bob', age=20, score=98)
# print(d)
# dj = json.dumps(d)
# print(dj)
# d = json.loads(dj)
# print(d)


# class Student(object):
#     def __init__(self, name, age, score):
#         self.name = name
#         self.age = age
#         self.score = score
#
# def studentdict(std):
#     return {
#         'name' : std.name,
#         'age' : std.age,
#         'score' : std.score
#     }
#
# s = Student('Bob', 20, 88)
# sj1 = json.dumps(s, default=studentdict)
# sj2 = json.dumps(s, default=lambda obj: obj.__dict__)
# print(sj1)
# print(sj2)
#
# def dictstudent(d):
#     return Student(d['name'], d['age'], d['score'])
#
# print(dictstudent(json.loads(sj2)))


# 多进程
# from multiprocessing import Process
# import os
#
# # 子进程要执行的代码
# def run_proc(name):
#     print('Run child process %s (%s)...' % (name, os.getpid()))
#
# if __name__=='__main__':
#     print('Parent process %s.' % os.getpid())
#     p = Process(target=run_proc, args=('test',))
#     print('Child process will start.')
#     p.start()
#     p.join()
#     print('Child process end.')

# 进程池
# from multiprocessing import Pool
# import os, time, random
#
#
# def long_time_task(name):
#     print('Run task %s (%s)...' % (name, os.getpid()))
#     start = time.time()
#     time.sleep(random.random() * 3)
#     end = time.time()
#     print('Task %s runs %0.2f seconds.' % (name, (end - start)))
#
#
# if __name__ == '__main__':
#     print('Parent process %s.' % os.getpid())
#     p = Pool(4)
#     for i in range(5):
#         p.apply_async(long_time_task, args=(i,))
#     print('Waiting for all subProcesses done...')
#     p.close()
#     p.join()
#     print('All subProcesses done.')


# 进程间通信(Queue)
# from multiprocessing import Process, Queue
# import os, time, random
#
#
# def write(q):
#     print('Process to write: %s' % os.getpid())
#     for value in ['A', 'B', 'C']:
#         print('Put %s to queue...' % value)
#         q.put(value)
#         time.sleep(random.random())
#
#
# def read(q):
#     print('Process to read %s' % os.getpid())
#     while True:
#         value = q.get(True)
#         print('Get %s from queue...' % value)
#
#
# if __name__ == '__main__':
#     q = Queue()
#     pw = Process(target=write, args=(q,))
#     pr = Process(target=read, args=(q,))
#     pw.start()
#     pr.start()
#     pw.join()
#     pr.terminate()


# 多线程
# import time
# import threading
#
#
# def loop():
#     print('thread %s is running...' % threading.current_thread().name)
#     n = 0
#     while n < 5:
#         n = n + 1
#         print('thread %s >>> %s' % (threading.current_thread().name, n))
#         time.sleep(1)
#     print('thread %s end.' % threading.current_thread().name)
#
#
# print('thread %s is running...' % threading.current_thread().name)
# t = threading.Thread(target=loop, name='LoopThread')
# t.start()
# t.join()
# print('thread %s ended.' % threading.current_thread().name)


# ThreadLocal
# import threading
# local_school = threading.local()
#
#
# def process_student():
#     std = local_school.student
#     print('Hello, %s (in %s)' % (std, threading.current_thread().name))
#
#
# def process_thread(name):
#     local_school.student = name
#     process_student()
#
#
# t1 = threading.Thread(target=process_thread, args=('Alice',), name='Thread-A')
# t2 = threading.Thread(target=process_thread, args=('Bob',), name='Thread-B')
# t1.start()
# t2.start()
# t1.join()
# t2.join()


# 正则表达式
# import re
# print(re.match(r'\d{3}\-\d{3,8}$', '010-12345'))
# print(re.split(r'\s+', 'a b  c'))
# print(re.split(r'[\s\,]+', 'a, ,b,  c'))
# m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
# print(m.group(0))
# print(m.group(1))
# print(m.group(2))
#
# re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')
# print(re_telephone.match('010-12345').groups())


# datetime
# from datetime import datetime, timedelta
# now = datetime.now()
# print(now)
# dt = datetime(2015, 4, 19, 12, 20)
# print(dt)
# print(dt.timestamp())
# t = 1429417200.0
# print(datetime.fromtimestamp(t))
# print(datetime.utcfromtimestamp(t))
# cday = datetime.strptime('2018-05-23 21:46:59', '%Y-%m-%d %H:%M:%S')
# print(cday)
# print(now.strftime('%a, %b %d %H:%M'))
# print(now)
# print(now + timedelta(hours=10))
# print(now - timedelta(days=1))


# collections
# from collections import namedtuple
# Point = namedtuple('Point', ['x', 'y'])
# p = Point(1, 2)
# print(p.x,  p.y)

# deque
# from collections import deque
# q = deque(['a', 'b', 'c'])
# q.append('x')
# q.appendleft('y')
# print(q)

# defaultdict
# from collections import defaultdict
# dd = defaultdict(lambda : 'N/A')
# dd['key1'] = 'abc'
# print(dd['key1'])
# print(dd['key2'])

# OrderedDict
# from collections import OrderedDict
# d = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
# print(d)

# Counter
# from collections import Counter
# c = Counter()
# for ch in 'programming':
#     c[ch] = c[ch] + 1
# print(c)

# base64
# import base64
# print(base64.b64encode(b'binary\x00string'))
# print(base64.b64decode(b'YmluYXJ5AHN0cmluZw=='))
# print(base64.b64encode(b'i\xb7\x1d\xfb\xef\xff'))
# print(base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff'))


# struct
# import struct
# print(struct.pack('>I', 10240099))
# print(struct.unpack('>IH', b'\xf0\xf0\xf0\xf0\x80\x80'))


# hashlib
# import hashlib
# md5 = hashlib.md5()
# md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
# print(md5.hexdigest())


# hmac
# import hmac
# message = b'Hello world'
# key = b'secret'
# h = hmac.new(key, message, digestmod='MD5')
# print(h.hexdigest())


# itertools
# import itertools

# natuals = itertools.count(1)
# for n in natuals:
#     print(n)

# cs = itertools.cycle('abc')
# for n in cs:
#     print(n)

# ns = itertools.repeat('A', 3)
# for n in ns:
#     print(n)

# natuals = itertools.count(1)
# ns = itertools.takewhile(lambda x: x <= 10, natuals)
# print(list(ns))

# for c in itertools.chain('ABC', 'XYZ'):
#     print(c)

# for key, group in itertools.groupby('AAaBBCCCAAA', lambda c: c.upper()):
#     print(key, list(group))


# urllib
# from urllib import request

# GET请求
# with request.urlopen('http://115.159.71.92/hongruan/web/loginPage') as f:
#     data = f.read()
#     print('status:', f.status, f.reason)
#     for k, v in f.getheaders():
#         print('%s: %s' % (k, v))
#     print('Data:', data.decode('utf-8'))

# 模拟iphone6访问豆瓣
# req = request.Request('http://www.douban.com/')
# req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
# with request.urlopen(req) as f:
#     print('Status:', f.status, f.reason)
#     for k, v in f.getheaders():
#         print('%s: %s' % (k, v))
#     print('Data:', f.read().decode('utf-8'))

#POST请求
# from urllib import request, parse
# print('Login to sina.cn...')
# email = input('Email: ')
# passwd = input('Password: ')
# login_data = parse.urlencode([
#     ('username', email),
#     ('password', passwd),
#     ('entry', 'mweibo'),
#     ('client_id', ''),
#     ('savestate', '1'),
#     ('ec', ''),
#     ('pagerefer', 'http://115.159.71.92/hongruan/web/loginPage')
# ])
#
# req = request.Request('https://passport.weibo.cn/sso/login')
# req.add_header('Origin', 'https://passport.weibo.cn')
# req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
# req.add_header('Referer', 'https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F')
#
# with request.urlopen(req, data=login_data.encode('utf-8')) as f:
#     print('Status:', f.status, f.reason)
#     for k, v in f.getheaders():
#         print('%s: %s' % (k, v))
#     print('Data:', f.read().decode('utf-8'))


# pillow
# 缩放图片
# from PIL import Image
# im = Image.open('E:\图片\照片photo.png')
# w,h = im.size
# print('size: %sx%s' % (w,h))
# im.thumbnail((w//2, h//2))
# im.save('E:\图片\照片.png', 'png')

# 模糊图片
# from PIL import Image, ImageFilter
# im = Image.open('E:\图片\照片photo.png')
# im2 = im.filter(ImageFilter.BLUR)
# im2.save('E:\图片\照片.png', 'png')


# requests
# import requests
# r = requests.get('http://115.159.71.92/hongruan/web/loginPage')
# print(r.status_code)
# print(r.text)

# r = requests.get('https://www.douban.com/search', params={'q': 'python', 'cat': '1001'})
# print(r.url)