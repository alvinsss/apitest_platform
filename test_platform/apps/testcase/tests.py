from django.test import TestCase

# Create your tests here.
import requests

# files = {'file': ('report.xls', open('apps.py', 'rb'), 'application/vnd.ms-excel', {'Expires': '0'})}
# data = {'key': 'value'}
# r = requests.post('http://httpbin.org/post', files=files,verify=False)
# print(r.text)

str = "url='1111',ip='1111',status=200,time:234"
index1=str.index('time:')
# print(index1)
print(str[index1+5:])
# print(str.index('time') ) # 输出 8