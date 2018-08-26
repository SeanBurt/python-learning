#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 列表 list 一种有序的集合，可以随时添加和删除其中的元素。
classmates = ['Michael', 'Bob', 'Tracy']
# 列表 tuple(元组)，一旦初始化就不能修改。
classmates = ('Michael', 'Bob', 'Tracy')

# 条件语句
if True:
    print('true')
else:
    print('false')

# 函数
# 如果没有return语句，函数执行完毕后也会返回结果，只是结果为None。return None可以简写为return。
def my_abs(x):
    if not isinstance(x. (int, float)):
        raise TabError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x
print(my_abs(-9))

# 空函数
# 实际上pass可以用来作为占位符，比如现在还没想好怎么写函数的代码，就可以先放一个pass，让代码能运行起来。
def nop():
    pass

# 函数参数校验
# 调用函数时，如果参数个数不对，Python解释器会自动检查出来，并抛出TypeError.
my_abs(1, 2)
# 如果参数类型不对，Python解释器就无法帮我们检查。试试my_abs和内置函数abs的差别.
my_abs('A')
abs('A')

# 返回多个参数
import math
def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny
x, y = move(100, 100, 60, math.pi / 6)
print(x, y)
# 其实这只是一种假象，Python函数返回的仍然是单一值，返回值是一个tuple。
r = move(100, 100, 60, math.pi / 6)
print(r)

# 默认参数
def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

# python函数在定义的时候，默认参数L的值就被计算出来了，即[]，因为默认参数L也是一个变量，它指向对象[]，每次调用该函数，如果改变了L的内容，则下次调用时，默认参数的内容就变了，不再是函数定义时的[]了。
def add_end(L=[]):
    L.append('END')
    return L
# 定义默认参数要牢记一点：默认参数必须指向不变对象！
# 为什么要设计str、None这样的不变对象呢？因为不变对象一旦创建，对象内部的数据就不能修改，这样就减少了由于修改数据导致的错误。此外，由于对象不变，多任务环境下同时读取对象不需要加锁，同时读一点问题都没有。我们在编写程序时，如果可以设计一个不变对象，那就尽量设计成不变对象。
def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L

# 可变参数 *
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

# 关键字参数 **
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)
person('Michael', 30)
person('Adam', 45, gender='M', job='Engineer')

# 命名关键字参数 * , key
# 只接收city和job作为关键字参数
def person(name, age, *, city, job):
    print(name, age, city, job)

# 递归函数
def fact(n):
    if n==1:
        return 1
    return n * fact(n - 1)
# 使用递归函数需要注意防止栈溢出。在计算机中，函数调用是通过栈（stack）这种数据结构实现的，每当进入一个函数调用，栈就会加一层栈帧，每当函数返回，栈就会减一层栈帧。由于栈的大小不是无限的，所以，递归调用的次数过多，会导致栈溢出。
fact(1000)

# 解决递归调用栈溢出的方法是通过尾递归优化
# 尾递归是指，在函数返回的时候，调用自身本身，并且，return语句不能包含表达式。这样，编译器或者解释器就可以把尾递归做优化，使递归本身无论调用多少次，都只占用一个栈帧，不会出现栈溢出的情况。
def fact(n):
    return fact_iter(n, 1)
def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)

# 切片 list tuple string
# python支持索引0取第一个元素，索引-1取倒数第一个元素
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
L[0:3]
L[:3]
L[-2:]
L[-2:-1]

# 迭代
# 判断一个对象是可迭代对象, 通过collections模块的Iterable类型判断
from collections import Iterable
isinstance('abc', Iterable)
isinstance([1,2,3], Iterable)
d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print(key)
# 对list实现类似Java那样的下标循环, Python内置的enumerate函数可以把一个list变成索引-元素对
for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)

# 列表生成式
[x * x for x in range(1, 11)]

# 生成器
# 把一个列表生成式的[]改成()，就创建了一个generator
(x * x for x in range(10))

# 迭代器
myiter = iter([1, 2, 3])
print(next(myiter))
for item in myiter:
    print(item)

# 函数式编程 Functional Programming
# 特点：允许把函数本身作为参数传入另一个函数，还允许返回一个函数。
# 变量可以指向函数
f = abs
f(-10)
# 函数名也是变量
abs = 10
abs(-10)
# 既然变量可以指向函数，函数的参数能接收变量，那么一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数。
def add(x, y, f):
    return f(x) + f(y)

# 内置高阶函数 map/reduce
# map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。
# reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算。
# 案例
from functools import reduce
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
def char2num(s):
    return DIGITS[s]
def str2int(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))
# filter()也接收一个函数和一个序列。和map()不同的是，filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。
def is_odd(n):
    return n % 2 == 1
list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15]))
# sorted()函数也是一个高阶函数，它还可以接收一个key函数来实现自定义的排序，例如按绝对值大小排序。

# 高阶函数除了可以接受函数作为参数外，还可以把函数作为结果值返回。
# 闭包
def count():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
    return fs
f1, f2, f3 = count()
f1()
f2()
f3()

# 匿名函数
# 关键字lambda表示匿名函数，冒号前面的x表示函数参数。
list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
# 匿名函数有个限制，就是只能有一个表达式，不用写return，返回值就是该表达式的结果。

# 装饰器
# 代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）。

# 偏函数
# functools.partial的作用就是，把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，调用这个新函数会更简单。
import functools
int2 = functools.partial(int, base=2)
int2('1000000')

# 模块
# 模块名要遵循Python变量命名规范，不要使用中文、特殊字符；
# 模块名不要和系统模块名冲突，最好先查看系统是否已存在该模块，检查方法是在Python交互环境执行import abc，若成功则说明系统存在此模块。
# 包

# 使用模块
import sys
# 在一个模块中，我们可能会定义很多函数和变量，但有的函数和变量我们希望给别人使用，有的函数和变量我们希望仅仅在模块内部使用。
# 类似_xxx和__xxx这样的函数或变量就是非公开的（private），不应该被直接引用，比如_abc，__abc等。

# 安装第三方模块
# 一般来说，第三方库都会在Python官方的pypi.python.org网站注册，要安装一个第三方库，必须先知道该库的名称，可以在官网或者pypi上搜索，比如Pillow的名称叫Pillow。
# Mac或Linux上有可能并存Python 3.x和Python 2.x，因此对应的pip命令是pip3。
# 在使用Python时，我们经常需要用到很多第三方库，例如，上面提到的Pillow，以及MySQL驱动程序，Web框架Flask，科学计算Numpy等。用pip一个一个安装费时费力，还需要考虑兼容性。我们推荐直接使用Anaconda，这是一个基于Python的数据处理和科学计算平台，它已经内置了许多非常有用的第三方库，我们装上Anaconda，就相当于把数十个第三方模块自动安装好了，非常简单易用。

# 模块搜索路径
# 默认情况下，Python解释器会搜索当前目录、所有已安装的内置模块和第三方模块，搜索路径存放在sys模块的path变量中。
# 一是直接修改sys.path，添加要搜索的目录；
# 第二种方法是设置环境变量PYTHONPATH，该环境变量的内容会被自动添加到模块搜索路径中。

# 面向对象编程 封装、继承、多态
# 类和实例
# class后面紧接着是类名，即Student，类名通常是大写开头的单词，紧接着是(object)，表示该类是从哪个类继承下来的，继承的概念我们后面再讲，通常，如果没有合适的继承类，就使用object类，这是所有类最终都会继承的类。
class Student(object):
    pass
# 定义好了Student类，就可以根据Student类创建出Student的实例，创建实例是通过类名+()实现的
bart = Student()
# 由于类可以起到模板的作用，因此，可以在创建实例的时候，把一些我们认为必须绑定的属性强制填写进去。通过定义一个特殊的__init__方法，在创建实例的时候，就把name，score等属性绑上去：
# 注意到__init__方法的第一个参数永远是self，表示创建的实例本身，因此，在__init__方法内部，就可以把各种属性绑定到self，因为self就指向创建的实例本身。
class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def print_score(self):
        print('%s: %s' % (self.name, self.score))

# 访问限制
# 如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线__，在Python中，实例的变量名如果以__开头，就变成了一个私有变量（private），只有内部可以访问，外部不能访问
class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score
    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))

# 继承和多态
# 在OOP程序设计中，当我们定义一个class的时候，可以从某个现有的class继承，新的class称为子类（Subclass），而被继承的class称为基类、父类或超类（Base class、Super class）。
class Animal(object):
    def run(self):
        print('Animal is running...')
class Dog(Animal):
    pass
class Cat(Animal):
    pass
dog = Dog()
dog.run()
cat = Cat()
cat.run()
# 当子类和父类都存在相同的run()方法时，我们说，子类的run()覆盖了父类的run()，在代码运行的时候，总是会调用子类的run()。这样，我们就获得了继承的另一个好处：多态。
class Dog(Animal):
    def run(self):
        print('Dog is running...')
class Cat(Animal):
    def run(self):
        print('Cat is running...')
# 多态的好处就是，当我们需要传入Dog、Cat、Tortoise……时，我们只需要接收Animal类型就可以了，因为Dog、Cat、Tortoise……都是Animal类型，然后，按照Animal类型进行操作即可。由于Animal类型有run()方法，因此，传入的任意类型，只要是Animal类或者子类，就会自动调用实际类型的run()方法，这就是多态的意思：
def run_twice(animal):
    animal.run()
    animal.run()
run_twice(Dog())
run_twice(Cat())
# 静态语言 vs 动态语言
# 对于静态语言（例如Java）来说，如果需要传入Animal类型，则传入的对象必须是Animal类型或者它的子类，否则，将无法调用run()方法。
# 对于Python这样的动态语言来说，则不一定需要传入Animal类型。我们只需要保证传入的对象有一个run()方法就可以了：
class Timer(object):
    def run(self):
        print('Start...')
# 这就是动态语言的“鸭子类型”，它并不要求严格的继承体系，一个对象只要“看起来像鸭子，走起路来像鸭子”，那它就可以被看做是鸭子。


