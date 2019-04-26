from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import requests
import json


# Create your views here.
def testcase_manage(request):
	return render(request, "testcase.html", {"type": "debug"})


@csrf_exempt
def debug(request):
	if request.method == "POST":
		url = request.POST.get("url", "")
		moethd = request.POST.get("moethd", "")
		header = request.POST.get("header", "")
		type_ = request.POST.get("type", "")
		parameter = request.POST.get("parameter", "")
		# csrfmiddlewaretoken=request.POST.get("csrfmiddlewaretoken", "")
		print("url", url)
		print("moethd", moethd)
		print("header", header)
		print("type_", type_)
		print("parameter", parameter)

		# header = str_toJson(header)
		# payload = str_toJson(parameter)
		payload = parameter

		if moethd == "get":
			if parameter == "" and header == "":
				r = requests.get(url)
			elif header == "":
				payload = str_toJson(parameter)
				r = requests.get(url, params=payload)
			elif parameter == "":
				header = str_toJson(header)
				r = requests.get(url, headers=header)
			else:
				header = str_toJson(header)
				payload = str_toJson(parameter)
				r = requests.get(url, params=payload, headers=header)

		if moethd == "post":
			if type_ == "from":
				# http://httpbin.org/post
				# {'file': ('report.xls', open('apps.py', 'rb'), 'application/vnd.ms-excel', {'Expires': '0'})}
				if header == "":
					payload = str_toJson(parameter)
					r = requests.post(url, data=payload)
				elif parameter == "":
					header = str_toJson(header)
					r = requests.post(url, header=header)
				else:
					header = str_toJson(header)
					payload = str_toJson(parameter)
					r = requests.post(url, data=payload, headers=header)

			if type_ == "json":
				# http://httpbin.org/post
				# {'Content-Type':'application/json'}
				# {'some': 'data'}
				if header == "":
					payload = str_toJson(parameter)
					r = requests.post(url, json=payload)
				elif parameter == "":
					header = str_toJson(header)
					r = requests.post(url, header=header)
				else:
					header = str_toJson(header)
					payload = str_toJson(parameter)
					r = requests.post(url, json=payload, headers=header)

		return JsonResponse({"result": r.text})
	else:
		return JsonResponse({"result": "请求方法错误"})


def str_toJson(str1):
	# 单引换双引
	str_re = str1.replace("\'", "\"")
	try:
		str_Json = json.loads(str_re)
	except json.decoder.JSONDecodeError:
		return JsonResponse({"result": "header类型错误"})
	# print("str_Json".format(),str_Json)
	return str_Json
