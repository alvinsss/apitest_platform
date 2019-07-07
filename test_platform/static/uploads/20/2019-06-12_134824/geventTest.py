from gevent import monkey; monkey.patch_all() #猴子补丁，改变python的库，改成非阻塞的
import gevent
import requests
import time
import gevent
import random
from gevent.queue import Queue
#
# def f(n):
#     for i in range(n):
#         print (gevent.getcurrent(), i)
#         gevent.sleep(0)
#
# g1 = gevent.spawn(f, 5)
# g2 = gevent.spawn(f, 5)
# g3 = gevent.spawn(f, 5)
# g1.join()
# g2.join()
# g3.join()

# def f(url):
#     print('GET: %s' % url)
#     resp = requests.get(url)
#     # data = resp.text
#     data = resp.content
#     print('%d bytes received from %s.' % (len(data), url))
#
# # gevent.joinall([])会等待所有传入的协程运行结束后再退出
# gevent.joinall([
#         gevent.spawn(f, 'https://www.python.org/'),
#         gevent.spawn(f, 'https://www.yahoo.com/'),
#         gevent.spawn(f, 'https://www.baidu.com/'),
# ])

# """
#     gevent 比 greenlet 更强. 协程库
#    协程是单线程, 遇到time.sleep() 是不能切换的.
#
#    gevent基于greenlet, 不需要手动切换, 遇到阻塞自动切换. 但是越到延时不切换.
#    gevent.sleep(2)  模拟阻塞, 会切换.
#    gevent.spawn(func)  启动协程对象.
#    gevent.joinall(list)    等待指定的greenlet走完, 再走.
# """


q = Queue(2)


def consumer():
    while True:
        item = q.get()
        print("consumer {}".format(item))
        time.sleep(2)  # 会延时.


def producer():
    while True:
        item = random.randint(0, 99)  # 0到99的随机整数.
        q.put(item)
        print("producer {}".format(item))
        time.sleep(2)

p = gevent.spawn(producer)  # 启动协程. 还可以 , + 函数参数.
c = gevent.spawn(consumer)
gevent.joinall([p, c])  # 阻塞当前流程, 执行完给定的greenlet, 才继续走.


