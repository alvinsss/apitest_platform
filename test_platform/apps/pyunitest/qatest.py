# -*- coding: utf-8 -*-
# @Time    : 2019/6/25 20:12
# @Author  : alvin
# @File    : qatest.py
# @Software: PyCharm
import json
import unittest
import requests
from ddt import ddt,data,file_data,unpack

@ddt   # 在测试类前必须首先声明使用 ddt.ddt
class Mytest(unittest.TestCase):
    def setUp(self):
        # 获取测试接口的url
        self.url = "http://admin-dsp-test.antuzhi.com/admin/login"

    @data({'user_name':'admin1','password':'25d55ad283aa400af464c76d713c07ad'},
          {'user_name': 'admin2', 'password': '25d55ad283aa400af464c76d713c07ad'},
          ({'user_name':'admin4','password':'25d55ad283aa400af464c76d713c07ad'}))
    @unpack
    # 后台人员登录
    def test_login(self,data):
        body = json.dumps(data)
        print("body",body)
        header = {}
        re = requests.post(self.url,data=body,headers = header,verify = False)
        code = re.status_code
        print(re.text,re.status_code)
        # 断言
        self.assertEqual(int(status),int(code))

    def tearDown(self):
        print('tearDown')

if __name__ == '__main__':
    unittest.main()