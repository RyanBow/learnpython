# 「施罗伟: #!/usr/bin/env python
# # -*- coding=utf-8 -*-
#
import math
# import random
# """
# random模块
# 从序列中随机获取一个元素
# 序列可以是 list 元祖 字符串
# """
# """
# 函数式编程
# 变量可以指向函数
# 一个函数可以接受另一个函数作为参数
# """
#
# fruits_price = {
#     "peach": 5,
#     "lemon": 7,
#     "pear": 11,
#     "apple": 13,
#     "banana": 23,
# }
#
#
# def double(fruit):
#     if fruits_price.get(fruit):
#         print(fruits_price.get(fruit) * 2)
#     else:
#         pass
#
# def get_random():
#     r = fruits_price.keys()
#     r = list(r)
#     fruit = random.choice(r)
#     double(fruit)
#
# get_random()」
# —————————
# 「Try: #!/usr/bin/env python
# # -*- coding=utf-8 -*-

"""
一个处理日志的程序
日志格式：json字符串
"""
# logs  = [
#     {"remote_addr": "10.163.18.216", "remote_user": "-","time_local": "09/May/2018:16:10:03 +0800","request": "POST /v1.0/toy/push HTTP/1.1","status": "200", "body_bytes_sent":"31","http_referer": "-","http_user_agent": "python-requests/2.18.4", "http_x_forwarded_for":"-","upstream_response_time":"1.649","request_time":"1.649"},
#     {"remote_addr": "10.163.18.216", "remote_user": "-","time_local": "09/May/2018:16:10:03 +0800","request": "POST /v1.0/toy/group HTTP/1.1","status": "200", "body_bytes_sent":"35","http_referer": "-","http_user_agent": "python-requests/2.18.4", "http_x_forwarded_for":"-","upstream_response_time":"1.902","request_time":"1.902"},
#     {"remote_addr": "10.163.18.217", "remote_user": "-","time_local": "09/May/2018:16:15:04 +0800","request": "POST /v1.0/toy/push HTTP/1.1","status": "200", "body_bytes_sent":"31","http_referer": "-","http_user_agent": "python-requests/2.18.4", "http_x_forwarded_for":"-","upstream_response_time":"1.762","request_time":"1.762"},
#     {"remote_addr": "10.163.18.216", "remote_user": "-","time_local": "09/May/2018:16:15:04 +0800","request": "POST /v1.0/toy/group HTTP/1.1","status": "200", "body_bytes_sent":"35","http_referer": "-","http_user_agent": "python-requests/2.18.4", "http_x_forwarded_for":"-","upstream_response_time":"1.969","request_time":"1.969"},
# ]
# # logs.append('1')
# # print(logs)
#
# def get_log_info(log,item="remote_addr"):
#     """
#     默认取出日志中ip地址
#     可以自定义取出的元素
#     :param log: 单条日志
#     :param item: 需要解析的某个元素
#     :return:
#     """
#     # 断言
#     assert item in log, "需要查询的元素内容不在日志中"
#     about_item = log.get(item)
#     return about_item

# 实现方法 之一
# temp = []
# for log in logs:
#     res = get_log_info(log,)
#     print(res)
#     temp.append(res)
# print(temp)
#
# # 实现方法 之二
# """
# map(函数方法，)
# 第一个参数为函数方法
# 第二个参数为可迭代对象参数
# 返回一个可迭代对象
# """
# print(set(map(get_log_info, logs)))
# print(list(map(get_log_info, logs)))
# —————————
# 「施罗伟: #!/usr/bin/env python
# -*- coding=utf-8 -*-

"""
filter()函数用于过滤序列
接收一个函数和序列
filter()把传入的函数依次作用于每个元素
然后根据返回值是True还是False决定保留还是丢弃该元素
能很快的实现一个筛选函数
"""

# 一个很传统的例子
# 将list列表中所有的偶数删除，只保留奇数
# numbs = [2,5,7,12,8,224,57,93,46,78,1]
#
# def is_odd(n):
#     return n % 2 == 1
#
# # print(is_odd(4))
#
# print(list(filter(is_odd, numbs)))

# 对日记进行筛选过滤

# logs_1  = [
#     {"remote_addr": "10.163.18.216", "remote_user": "-","time_local": "09/May/2018:16:10:03 +0800","request": "POST /v1.0/toy/push HTTP/1.1","status": "200", "body_bytes_sent":"31","http_referer": "-","http_user_agent": "python-requests/2.18.4", "http_x_forwarded_for":"-","upstream_response_time":"1.649","request_time":"1.649"},
#     {"remote_addr": "10.163.18.216", "remote_user": "-","time_local": "09/May/2018:16:10:03 +0800","request": "POST /v1.0/toy/group HTTP/1.1","status": "200", "body_bytes_sent":"35","http_referer": "-","http_user_agent": "python-requests/2.18.4", "http_x_forwarded_for":"-","upstream_response_time":"1.902","request_time":"1.902"},
#     {"remote_addr": "10.163.18.216", "remote_user": "-","time_local": "09/May/2018:16:15:04 +0800","request": "POST /v1.0/toy/push HTTP/1.1","status": "200", "body_bytes_sent":"31","http_referer": "-","http_user_agent": "python-requests/2.18.4", "http_x_forwarded_for":"-","upstream_response_time":"1.762","request_time":"1.762"},
#     {"remote_addr": "10.163.18.216", "remote_user": "-","time_local": "09/May/2018:16:15:04 +0800","request": "POST /v1.0/toy/group HTTP/1.1","status": "200", "body_bytes_sent":"35","http_referer": "-","http_user_agent": "python-requests/2.18.4", "http_x_forwarded_for":"-","upstream_response_time":"1.969","request_time":"1.969"},
# ]
#
#
# def filter_log_requestTime(log):
#     item = "request_time"
#     rq = log.get(item)
#     print(rq)
#     if float(rq) > 1.9:
#         return True
# a = []
# def filter_log_status(log):
#     item = "status"
#     rq = log.get(item)
#     if int(rq) == 200:
#         a.append(log.get("request_time"))
#         return True
# def filter_max(log):
#     avg = "request_time"
#     rq = log.get(avg)
#     return rq

# print(list(filter(filter_max,logs_1)))
# print(list(filter(filter_log_status,logs_1)))
# print(list(filter(filter_log_requestTime,logs_1)))
# print(len(list(filter(filter_log_requestTime,logs_1))))
# —————————
# 「施罗伟: #!/usr/bin/env python
# -*- coding=utf-8 -*-

"""
读写文件是最常见的IO操作
在磁盘上读写文件的功能都是由操作系统提供的，现代操作系统不允许普通的程序直接操作磁盘，
所以，读写文件就是请求操作系统打开一个文件对象（通常称为文件描述符），
然后，通过操作系统提供的接口从这个文件对象中读取数据（读文件），
或者把数据写入这个文件对象（写文件）。
"""

# # 读文件
# f = open('../access.log', 'r')
# # 读取文件
# # logs = f.read()
# # type str
# # 遍历文件
# # 错误的方法
# # for log in logs:
# #     print(log)
# for line in f.readlines():
#     # line type str
#     line = line.strip()
#     # #  type dict
#     line_obj = eval(line)
#     print(line_obj.get("remote_addr"))
# # 最后关闭文件
# # 文件必须被关闭，否则文件描述符的数量将会被占用无法释放
# f.close()
#
#
# # 读取的文件不存在的情况
# try:
#     f = open('../unknown.log', 'r')
#     print(f.read())
# except FileNotFoundError as error:
#     print(f'操作文件失败，原因是:{error}')
# finally:
#     if f:
#         f.close()


# 更简单的读取文件的方式
# with open('../access.log', 'r')  as f:
#     for line in f.readlines():
#         line = line.strip()
#         line_obj = eval(line)
#         print(line_obj.get("http_user_agent"))


# 写文件
# w  覆盖写
# a+ 追加
# with open("../hello.txt", 'a+') as f:
#     f.write("hello python houhou again !\n")
# #
# #
# # # 字符编码
# #
# # # 指定字符集的编码进行读取
# # with open('../gbk.txt', 'r', encoding="gbk", errors="ignore")  as f:
# #    print(f.read())
# # 打开多个文件
# with open("file1", 'r') as file1:
#     with open("file2", "r") as file2:
#         file1.read()
#         file2.read()
#
# with open("file1", 'r') as file1:
#     file1.read()
#
# with open("file2", "r") as file2:
#     file2.read()」
# —————————

# f = open("./log.log")
# for line in f.readlines():
#     line = line.strip()
#     line_obj = eval(line)
#     print(line_obj.get("request_time"))
#
# f.close()

# path = "./log.log"
def open_log(log_path,param="request_time"):
    a = []
    f = open(log_path)
    # print(f)
    for line in f.readlines():
        line = line.strip()
        line_obj = eval(line)
        # print(type(line_obj.get(param)))
        # return line_obj.get(param)
        a.append(line_obj.get(param))
    return a
    f.close()
print(max(open_log('log.log',)))
# # 实现方法 之二
# """
# map(函数方法，)
# 第一个参数为函数方法
# 第二个参数为可迭代对象参数
# 返回一个可迭代对象
# """
# print(set(map(get_log_info, logs)))
# print(list(map(get_log_info, logs)))
# def do_filter(log,status=200):
# f = open("./log.log")
# f_new = f.readlines()
# print(f_new.values)
# 「施罗伟: #!/usr/bin/env python
# # -*- coding=utf-8 -*-
#
# """
# 读写文件是最常见的IO操作
# 在磁盘上读写文件的功能都是由操作系统提供的，现代操作系统不允许普通的程序直接操作磁盘，
# 所以，读写文件就是请求操作系统打开一个文件对象（通常称为文件描述符），
# 然后，通过操作系统提供的接口从这个文件对象中读取数据（读文件），
# 或者把数据写入这个文件对象（写文件）。
# """
#
# # # 读文件
# # f = open('../access.log', 'r')
# # # 读取文件
# # # logs = f.read()
# # # type str
# # # 遍历文件
# # # 错误的方法
# # # for log in logs:
# # #     print(log)
# # for line in f.readlines():
# #     # line type str
# #     line = line.strip()
# #     # #  type dict
# #     line_obj = eval(line)
# #     print(line_obj.get("remote_addr"))
# # # 最后关闭文件
# # # 文件必须被关闭，否则文件描述符的数量将会被占用无法释放
# # f.close()
# #
# #
# # # 读取的文件不存在的情况
# # try:
# #     f = open('../unknown.log', 'r')
# #     print(f.read())
# # except FileNotFoundError as error:
# #     print(f'操作文件失败，原因是:{error}')
# # finally:
# #     if f:
# #         f.close()
#
#
# # 更简单的读取文件的方式
# # with open('../access.log', 'r')  as f:
# #     for line in f.readlines():
# #         line = line.strip()
# #         line_obj = eval(line)
# #         print(line_obj.get("http_user_agent"))
#
#
# # 写文件
# # w  覆盖写
# # a+ 追加
# with open("../hello.txt", 'a+') as f:
#     f.write("hello python houhou again !\n")
# #
# #
# # # 字符编码
# #
# # # 指定字符集的编码进行读取
# # with open('../gbk.txt', 'r', encoding="gbk", errors="ignore")  as f:
# #    print(f.read())
# # 打开多个文件
# with open("file1", 'r') as file1:
#     with open("file2", "r") as file2:
#         file1.read()
#         file2.read()
#
# with open("file1", 'r') as file1:
#     file1.read()
#
# with open("file2", "r") as file2:
#     file2.read()」
# —————————
