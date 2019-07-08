# -*- coding: utf-8 -*-
# @Time    : 2019/5/5 17:02
# @Author  : alvin
# @File    : qatest.py
# @Software: PyCharm
from    locust import HttpLocust, TaskSet, task
import  random
import  json

def get_body():
    reuslt = []
    with open('req.new.jsonlines', 'r') as f:
        for line in f:
            reuslt.append(line)
    return reuslt


class UserBehavior(TaskSet):
    @task(1)
    def test_search(self):

        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
        path = f'recommend/dayan'
        bodys = get_body()
        body = random.choice(bodys)
        print(path,body,headers)
        resp = self.client.post(path, body, headers=headers).text
        resp = json.loads(resp)
        id = 'NULL'
        id = resp['id']
        listres = []
        if id !=  'NULL':
            listres.append(resp)
            print("scuess")
        else:
            print("fail")
        print(listres)

class websitUser(HttpLocust):
    task_set = UserBehavior
    # min_wait = 3000
    # max_wait = 6000

if __name__ == '__main__':
    # http://47.104.201.5:18090/api/search/search?curPage=search_result&page=2&limit=20&word=j
    import os
    filename = __file__
    #host = 'http://47.104.31.59/' #走张军代理
    host = 'http://118.190.128.165/' # 不走张军代理
    cmd = f'locust -f {filename} --host={host}'
    os.system(cmd)