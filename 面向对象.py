# 1.初识面向对象编程
"""
1. 面向对象编程的基本概念
2. 类、对象、属性、方法
先定义类,在类中定义方法,在方法中实现具体的功能
实例化类并创建一个对象,通过对象调用方法,实现具体的功能
"""
# 1.1 对象和self
"""
在每个类中都可以定义特殊的__init__方法,该方法在对象被实例化时自动调用,可以用来初始化对象属性
self参数是类的实例,它代表当前对象的引用,可以用来访问对象内部的属性和方法
# 数据封装到对象,以后再去获取,规范约束数据
对象本质上是内存中的一块数据,是类的实例,可以通过self来访问类的属性和方法
"""

"""
总结:
仅做数据封装
数据封装+方法调用对数据进行操作
创建同一类的数据并且可以拥有相同的功能
"""
# class Police:
#     """警察"""
#     def __init__(self, name, role):
#         self.name = name
#         self.role = role
#         if role == '队员':
#             self.hit_points = 200
#         else:
#             self.hit_points = 500

#     def show_status(self):
#         message = f"警察{self.name}的生命值为：{self.hit_points}"
#         print(message)

#     def bomb(self,terrorist_list):
#         for terrorist in terrorist_list:
#             terrorist.blood -=200
#             terrorist.show_status()



# class Terrorist:
#     """恐怖分子"""
#     def __init__(self, name, blood = 300):
#         self.name = name
#         self.blood = blood

#     def show_status(self):
#         message = f"恐怖分子{self.name}的生命值为：{self.blood}"
#         print(message)

#     def shoot(self, police_object):
#         police_object.hit_points -= 20
#         police_object.show_status()

#     def strafe(self, police_object_list):
#         for police_object in police_object_list:
#             police_object.hit_points -= 10
#             police_object.show_status()

# def run():

#     p1 = Police('小红', '队员')
#     p2 = Police('小明', '队员')
#     p3 = Police('小张', '队长')
#     t1 = Terrorist('小刚')
#     t2 = Terrorist('小李')
    

#     t1.shoot(p1)
#     t2.shoot(p2)

#     p1.bomb([t1,t2])

#     t1.strafe([p1,p2,p3])
#     t2.strafe([p1,p2,p3])

#     p2.bomb([t1,t2])
#     p3.bomb([t1,t2])

# if __name__ == '__main__':
#     run()

# 2.封装、继承、多态
"""
封装:将数据和操作数据的方法封装到一个类中,外部代码只能通过类提供的接口访问数据和方法,隐藏内部实现
继承:子类可以继承父类的属性和方法,可以扩展父类的功能,提高代码复用性
多态:父类引用指向子类对象,可以调用子类的方法,实现代码的可扩展性
"""
"""
继承:mro和c3算法
mro:方法解析顺序,指的是在查找方法时,按照从左到右的顺序查找方法,直到找到第一个为止
c3算法:是一种优化的mro算法,可以避免重复搜索,提高查找效率
执行对象的方法时,会自动寻找对象所属类的继承链,如果对象所属类中没有找到对应的方法,则会继续向上查找父类的方法
如果找到了,则调用该方法,否则会报错
如果有多继承的情况,则会按照从左到右的顺序查找方法,找到第一个就停止查找

多态,Python对数据类型没有限制,天生支持多态
鸭子类型:动态类型的一种风格,只要看起来像鸭子,叫起来像鸭子,那么它就是鸭子,不管它本身是什么类型
"""
# obj.mro() # 查看对象所属类的继承链
# obj.__mro__ # 查看对象所属类的继承链
# 从左到右,深度优先,大小钻石,留住顶端

# 3.成员、成员修饰符、对象嵌套、特殊成员
"""
变量:类变量(属于类,可以被所有对象共享,不用实例化即可访问,用类名.变量名访问)、实例变量(属于对象,只能被该对象访问,用self.变量名访问)
方法:绑定方法(类中定义的函数,有self参数)、类方法(用@classmethod修饰的方法,有cls参数)、静态方法(用@staticmethod修饰的方法,没有self或cls参数)
属性:类属性(用@property修饰的绑定方法,可以像访问实例变量一样访问,用cls.变量名访问)、实例属性
"""
#类变量和实例变量的读顺序:先找实例变量,找不到再找类变量
#类变量和实例变量的写顺序:如果当前对象的变量名存在，则修改变量，否则创建变量
#用@property修饰的方法x,可以有@x.setter和@x.deleter和@x.getter修饰符,分别用来设置和删除和获取属性值
# 也可以用x = property(fget=fget, fset=fset, fdel=fdel, doc="注释内容")来简化代码
#实例变量名和方法名不能重名,否则在@property修饰的方法中可能会报错
"""
成员修饰符:公有成员(public member)、私有成员(private member)、保护成员(protected member)
公有成员:外部代码可以直接访问,包括类外的代码和子类
私有成员:用两个下划线开头,外部代码不能直接访问,只能通过类的方法访问
私有成员不能被子类继承,只能通过父类的方法访问
"""

# 对象嵌套
"""
面向对象编程时,对象之间存在各种各样的关系,可以用对象嵌套的方式来表示这种关系
"""
# 4.特殊成员
"""
特殊成员:特殊成员是指一些在Python中有特殊用途的成员,包括__init__、__str__、__call__、__len__等
"""
# __init__方法:初始化方法,在对象被实例化时自动调用,用来初始化对象属性
# __new__方法:构造方法,用来创建对象,返回对象实例,但不调用__init__方法,平时会省略不写
# __str__方法:打印对象时调用,返回对象的字符串表示
# __call__方法:对象可调用,可以像函数一样调用,可以重载()运算符obj()
# __dict__方法:返回对象的属性字典,可以通过字典的形式访问对象的属性
# __getitem__方法、__setitem__方法、__delitem__方法:实现对对象中元素的访问和修改,分别用于获取、设置和删除元素
# __enter__方法、__exit__方法:实现上下文管理器,with语句调用该方法
# __add__方法、__sub__方法、__mul__方法、__truediv__方法:实现数值运算,如+、-、*、/运算符
# __iter__方法:返回对象的迭代器,如for x in obj:...
"""
迭代器类型的定义:
类中定义了__iter__方法和__next__方法,并且__iter__方法返回自己,__next__方法返回下一个元素,如果没有数据了,则抛出StopIteration异常
for循环会调用__iter__方法,然后调用__next__方法,直到抛出StopIteration异常,循环结束
"""

# 生成器:
"""
生成器函数:用yield关键字定义的函数,返回一个生成器对象
生成器内部实现了__iter__和__next__方法,可以用for循环来迭代,也可以用next()函数来获取下一个元素
生成器可以用于迭代器,也可以用于列表推导式,可以节省内存
"""

# 可迭代对象:
"""
可迭代对象:实现了__iter__方法,返回一个迭代器对象,可以用for循环来迭代
"""

# 5.异常处理
"""
遇到不可预知的错误或者不想做一些判断时,可以选择用异常处理来处理
try...except...finally...语句可以捕获异常,并处理异常,finally语句用来做一些清理工作
return 语句不影响finally语句的执行
异常细分:
1. 语法错误:SyntaxError
2. 逻辑错误:ValueError、TypeError、IndexError、KeyError
3. 运行时错误:IOError、AttributeError、NameError、ImportError、MemoryError、RecursionError、SystemError、KeyboardInterrupt

AttributeError:试图访问一个对象没有的属性
NameError:试图访问一个还未赋值的变量
TypeError:对类型不正确的操作
IndexError:下标越界
KeyError:试图访问字典中不存在的键
IOError:输入输出错误
ValueError:传入无效的参数
ImportError:导入模块失败
MemoryError:内存溢出
RecursionError:递归太深
SystemError:系统错误
KeyboardInterrupt:用户中断程序

4. 其他错误:自定义异常,可以继承Exception类,定义自己的异常类型,可以用raise语句抛出异常
"""

# 6.反射
# getattr(obj, name, default)获取对象属性的值，如果属性不存在，则返回default值
# setattr(obj, name, value)设置对象属性的值
# delattr(obj, name)删除对象属性
# hasattr(obj, name)判断对象是否有某个属性,返回True或False

# 6.1 一切皆对象,每个对象的内部都有自己维护的成员,对象、类、模块、函数、方法、属性、异常等都可以看做对象
# 6.2 import_module +反射:通过import导入模块;或者通过import_module("模块名")导入模块,不能导入类
