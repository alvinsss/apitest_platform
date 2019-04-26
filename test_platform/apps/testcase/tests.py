from django.test import TestCase

# Create your tests here.
import requests

files = {'file': ('report.xls', open('apps.py', 'rb'), 'application/vnd.ms-excel', {'Expires': '0'})}
data = {'key': 'value'}
r = requests.post('http://httpbin.org/post', files=files)
print(r.text)
