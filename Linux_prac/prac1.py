#! usr/bin/python3
# def test1(r):
#     '''这是一'''
#     p = 3.14
#     s = p * r ** 2
#     return s
# res = test1(1)
# res2 = test1(2)
# print(f"半径为1的{res},2的{res2}")
# def test2(l):
#     return l**2
# print(test2(10))
# def func7(name,sex=1,lesson='Linux'):
#     return (name,sex,lesson)
# print(func7(搜索))
def func8(list):
    for l in list:
        print ('value',l)
list1 = {1,'tian','ying'}
print(list1)
print(func8(list1))
# 「施罗伟: #!/usr/bin/env python
# # -*- coding=utf-8 -*-
# # 自定义函数
# pi = 3.14
# # 自定义一个求圆的面积的函数方法
# def my_func1(r):
#     """
#     :param r: int  圆的半径
#     :return:  int  圆的面积
#     """
#     s = pi*r**2
#     return s
#
# print(my_func1(4))
#
#
# print("从别的文件引入函数的使用方法")
#
# def my_func2(r):
#     """
#     :param r: int  圆的半径
#     :return:  int  圆的面积
#     """
#     if not isinstance(r, (int,float)):
#         # raise TypeError("输入的半径参数格式错误")
#         r = 0
#     s = pi*r**2
#     return s
#
#
# print(my_func2(4))
# print(my_func2("wrong"))
#
# # 自定义的函数返回多个值
#
# # 我们在自定义函数的时候，为了保证函数最大程度上的复用，在参数定义上要做很多考虑
# # 参数的种类：
# # 必须参数
# # 默认参数
# # 可变参数
# # 关键字参数
#
# # 例子：
# def func3(name, sex, city="青岛", lesson="Linux"):
#     return {
#         "name": name,
#         "sex": sex,
#         "city": city,
#         "lesson": lesson,
#     }
#
# print(func3("张三","1","济南"))
# # 多个默认参数调用的时候，可以按照顺序提供
# # 当不按照顺序提供默认参数的时候，需要把参数名写上
# # 默认参数必须指向不变对象，str，none
#
# print(func3("李四","0",lesson="Python"))
#
#
# # 可变参数  *args
# def func4(*args):
#     for arg in args:
#         print(arg)
#
# func4("apple", "orange")
#
# fruits = ["apple", "orange", "pear"]
# func4(fruits)
# func4(*fruits)
# # 区别于这两个调用的不同
# # Python允许你在list或tuple前面加一个*号，把list或tuple的元素变成可变参数传进去
# # 这种写法相当有用，而且很常见
#
#
# # 关键字参数
#
# def func5(name, age, **kwargs):
#     """
#     :param name:
#     :param age:
#     :param kwargs:
#     :return:
#     """
#     return {
#         "name": name,
#         "age": age,
#         "others": kwargs
#     }
#
# print(func5("stu1", 22,))
# print(func5("stu2", 22, sex=1,lesson="linux"))
# print(func5("stu3", 22, sex=0,lesson="python",city="青岛"))
# # 我们也可以将dict直接传递到函数的参数中
# stu4_others = {"sex":1,"lesson":"python","city":"济南"}
# print(func5("stu4", 22, **stu4_others))
#
# # 命名关键字参数
# """
# 对于关键字参数的函数，我们可以传入很多自定义的不受限制的关键字参数。
# 我们需要通过kwargs进行检查
# 通过关键字参数防止用户随意的传入我们不需要的参数
# """
#
# def func6(name, age, **kwargs):
#     if "lesson" in kwargs:
#         print(f'lesson is {kwargs.get("lesson")}')
#         print("lesson is {0}".format(kwargs.get('lesson')))
#     return {
#         "name": name,
#         "age": age,
#         "others": kwargs
#     }
# func6('张三',32,lesson="Python")
#
#
# def func7(name, age, *, lesson, city):
#     """
#     测试一个命名关键字参数的函数方法
#     :param name: <str>
#     :param age:     <int>
#     :param lesson:  <str>
#     :param city:    <str>
#     :return: <dict>
#     """
#     return {
#         "name": name,
#         "age": age,
#         "lesson": lesson,
#         "city": city
#     }
#
# # print(f'错我的调用方式')
# # print(func7('张三',23,"Python", "济南"))
# print(func7('张三',23,lesson="Python", city="济南"))
# print(func7('张三',23,lesson="Python", city="济南"))
#
# # 参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数
# # 对于任意函数，都可以通过类似func(*args, **kw)的形式调用它，无论它的参数是如何定义的」
# —————————

