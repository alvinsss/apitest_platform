# -*- coding: utf-8 -*-
# @Time    : 2019/5/5 16:33
# @Author  : alvin
# @File    : qatest.py
# @Software: PyCharm
import os
from locust import HttpLocust, TaskSet, task


class UserBehavior(TaskSet):

    @task(1)
    def qatest(self):
        res = self.client.get("/")
        if res.status_code == 200 :
            print("qatest scuess")
        else:
            print("qatest fail")

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 1
    max_wait = 1

if __name__ == '__main__':
    filename = __file__
    host = 'http://www.baidu.com'
    cmd = f'locust -f {filename} --host={host}'
    print(" http://localhost:8089")
    os.system(cmd)