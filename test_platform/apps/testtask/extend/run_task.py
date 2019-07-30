# -*- coding: utf-8 -*-
# @Time    : 2019/6/25 18:17
# @Author  : alvin
# @File    : run_task.py
# @Software: PyCharm
import json
import unittest
from ddt import ddt, data, file_data, unpack
import requests
import xmlrunner
import sys
import baserequestdecode


@ddt
class InterfaceTest( unittest.TestCase ):
    '''
    测试任务的执行
    测试任务的执行比较复杂，整体思路如下。
    1、使用 unittest 实现用例的执行，以及结果的统计。
    2、ddt 基于unittest单元测试框架的数据驱动库，方便读取JOSN文件。 https://github.com/datadriventests/ddt
    3、 xmlrunner 执行 unittest 测试用例并生成 XML 格式的报告。 https://github.com/xmlrunner/unittest-xml-reporting
    4、Requests 实现接口的调用。 https://github.com/kennethreitz/requests
    '''

    @unpack
    @file_data( "test_data_list.json" )
    def test_run_cases(self, url, method, header, parameter_type, parameter_body, assert_type, assert_text, encryption):

        if header == "{}":
            header_dict = {}
        else:
            header_dict = json.loads( header.replace( "\'", "\"" ) )
        print("test_run_cases parameter_body",parameter_body)
        if parameter_body == "{}":
            parameter_dict = {}
        else:
            parameter_dict = json.loads( parameter_body.replace( "\'", "\"" ) )
            print("test_run_cases  parameter_dict",parameter_dict)

        if method == "get":
            # print("run task of case get --->")
            if parameter_type == "from" and encryption == 0:
                requests.packages.urllib3.disable_warnings()
                r = requests.get( url, headers=header_dict, params=parameter_dict ,verify=False)

                if assert_type == "contains":
                    assert_list = assert_text.split( '|' )
                    for assert_str in assert_list:
                        self.assertIn( assert_str, r.text )
                else:
                    self.assertEqual( assert_text, r.text )

        if method == "post":
            if parameter_type == "from" and encryption == 0:
                # print( "run task of case post --->from 0 " )
                requests.packages.urllib3.disable_warnings()
                r = requests.post( url, headers=header_dict, data=parameter_dict,verify=False )
                if assert_type == "contains":
                    assert_list = assert_text.split( '|' )
                    for assert_str in assert_list:
                        self.assertIn( assert_str, r.text )
                else:
                    self.assertEqual( assert_text, r.text )
            elif parameter_type == "from" and encryption == 1:
                print("from encryption == 1 ----> parameter_body",parameter_body)
                r = baserequestdecode.endepost( url, bodydata=parameter_body, key=None, postheaders=None,
                                                      transBinData=False, body_type=None )
                # result_text = json.dumps(r)
                result_text = json.dumps( r )
                print( "parameter_type from and encryption == 1  result_text",result_text )
                if assert_type == "contains":
                    assert_list = assert_text.split( '|' )
                    for assert_str in assert_list:
                        self.assertIn( assert_str, result_text )
                else:
                    self.assertEqual( assert_text, result_text )

            elif parameter_type == "json" and encryption == 0:
                # print( "run task of case post --->json 0 " )
                requests.packages.urllib3.disable_warnings()
                r = requests.post( url, headers=header_dict, json=parameter_dict,verify=False )
                if assert_type == "contains":
                    # self.assertIn( assert_text, r.text )
                    assert_list = assert_text.split( '|' )
                    for assert_str in assert_list:
                        self.assertIn( assert_str, r.text )
                else:
                    self.assertEqual( assert_text, r.text )

            elif parameter_type == "json" and encryption == 1:

                print("json encryption == 1 ----> parameter_body",url,parameter_body)
                r =baserequestdecode.endepost(url, parameter_body, key=None, postheaders=None, transBinData=False, body_type=None)
                result_text = json.dumps(r)
                print( "parameter_type josn and encryption == 1  result_text",result_text)
                if assert_type == "contains":
                    # self.assertIn( assert_text, result_text )
                    assert_list = assert_text.split( '|' )
                    for assert_str in assert_list:
                        self.assertIn( assert_str, result_text )
                else:
                    self.assertEqual( assert_text, result_text)
            else:
                raise NameError( "参数类型错误" )


# 运行测试用例
def run_cases():

    print("------------run_cases start-----------")

    import platform
    if (platform.system() == "Windows"):
        EXTEND_DIR = r"D:\UserData\git\PycharmProjects\apitest_platform\test_platform\apps\testtask\extend\\"
    else :
        EXTEND_DIR = r"/q/tools/python/django_web/test_platform/apps/testtask/extend/"

    print( "-------run_cases platform.system()--------", platform.system() )

    print( "------------run_cases EXTEND_DIR------------", EXTEND_DIR )

    # '''xmlrunner w '''
    with open( EXTEND_DIR + 'results.xml', 'wb' ) as output:
        unittest.main(
            testRunner=xmlrunner.XMLTestRunner( output=output ),
            failfast=False, buffer=False, catchbreak=False
        )
    print("------------run_cases end------------")


if __name__ == '__main__':
    run_cases()
