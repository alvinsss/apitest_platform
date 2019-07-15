# -*- coding: utf-8 -*-
# @Time    : 2019/6/17 13:31
# @Author  : alvin
# @File    : run_task_testcase.py
# @Software: PyCharm
import sys
import json
import unittest
from ddt import ddt, data, file_data, unpack
import requests


@ddt
class InterfaceTest( unittest.TestCase ):

    @unpack
    @file_data( "test_data_list.json" )
    def test_run_casess(self, url, method, header, parameter_type, parameter_body,assert_type,assert_text):
        print("test_run_casess is running")
        if header == "{}":
            header_dict = {}
        else:
            hearder_str = header.replace( "\'", "\"" )
            header_dict = json.loads( hearder_str )
        print("test_run_casess parameter_body ",parameter_body)
        if parameter_body == "{}":
            parameter_dict = {}
        else:
            parameter_str = parameter_body.replace( "\'", "\"" )
            print( "test_run_casess parameter_str ", parameter_str )
            parameter_dict = json.loads( parameter_str )
            print( "test_run_casess parameter_dict ", parameter_dict )

        if method == "get":
            if parameter_type == "from":
                r = requests.get( url, headers=header_dict,
                                  params=parameter_dict,verify=False )
                # self.assertIn(assert_text, r.text)

        if method == "post":
            if parameter_type == "from":
                r = requests.post( url, headers=header_dict,
                                   data=parameter_dict ,verify=False)
                # self.assertIn(assert_text, r.text)

            elif parameter_type == "json":
                r = requests.post( url, headers=header_dict,
                                   json=parameter_dict,verify=False )
                # self.assertIn(assert_text, r.text)


# if __name__ == '__main__':
#     unittest.main()
