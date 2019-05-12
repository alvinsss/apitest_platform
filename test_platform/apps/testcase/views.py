from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from testcase.models import TestCase
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
				payload = _str_toJson(parameter)
				r = requests.get(url, params=payload)
			elif parameter == "":
				header = _str_toJson(header)
				r = requests.get(url, headers=header)
			else:
				header = _str_toJson(header)
				payload = _str_toJson(parameter)
				r = requests.get(url, params=payload, headers=header)

		if moethd == "post":
			if type_ == "from":
				# http://httpbin.org/post
				# {'file': ('report.xls', open('apps.py', 'rb'), 'application/vnd.ms-excel', {'Expires': '0'})}
				if header == "":
					payload = _str_toJson(parameter)
					r = requests.post(url, data=payload)
				elif parameter == "":
					header = _str_toJson(header)
					r = requests.post(url, header=header)
				else:
					header = _str_toJson(header)
					payload = _str_toJson(parameter)
					r = requests.post(url, data=payload, headers=header)

			if type_ == "json":
				# http://httpbin.org/post
				# {'Content-Type':'application/json'}
				# {'some': 'data'}
				if header == "":
					payload = _str_toJson(parameter)
					r = requests.post(url, json=payload)
				elif parameter == "":
					header = _str_toJson(header)
					r = requests.post(url, header=header)
				else:
					header = _str_toJson(header)
					payload = _str_toJson(parameter)
					r = requests.post(url, json=payload, headers=header)

		return JsonResponse({"result": r.text})
	else:
		return JsonResponse({"result": "请求方法错误"})


def _str_toJson(str1):
	# 单引换双引
	str_re = str1.replace("\'", "\"")
	try:
		str_Json = json.loads(str_re)
	except json.decoder.JSONDecodeError:
		return JsonResponse({"result": "header类型错误"})
	# print("str_Json".format(),str_Json)
	return str_Json


@csrf_exempt
def testcase_assert(request):
	if request.method == "POST":
		result_text = request.POST.get("result", "")
		assert_text = request.POST.get("assert", "")
		assert_type = request.POST.get("assert_type", "")
		if result_text == "" or assert_text == "":
			return JsonResponse({"result": "断言的文本不能为空！"})

		if assert_type == "contains":
			print("contains")
			if assert_text not in result_text:
				return JsonResponse({"result": "断言失败！"})
			else:
				return JsonResponse({"result": "断言成功！"})
		elif assert_type == "mathches":
			if assert_text != result_text:
				return JsonResponse({"result": "断言失败！"})
			else:
				return JsonResponse({"result": "断言成功！"})

	else:
		return JsonResponse({"result": "请求方法错误！"})


@csrf_exempt
def testcase_save(request):
	"""
	用例保存
	"""
	if request.method == "POST":
		url = request.POST.get("url", "")
		method = request.POST.get("method", "")
		header = request.POST.get("header", "")
		parameter_type = request.POST.get("par_type", "")
		parameter_body = request.POST.get("par_body", "")
		assert_type = request.POST.get("ass_type", "")
		assert_text = request.POST.get("ass_text", "")
		module_id = request.POST.get("mid", "")
		name = request.POST.get("name", "")

		# print("url", url)
		# print("method", method)
		# print("header", header)
		# print("parameter_type", parameter_type)
		# print("parameter_body", parameter_body)
		# print("assert_type", assert_type)
		# print("assert_text", assert_text)
		# print("module_id", module_id)
		# print("name", name)

		if name == "":
			return JsonResponse({"status": 10101, "message": "用例名称不能为空"})

		if module_id == "":
			return JsonResponse({"status": 10103, "message": "所属的模块不能为空"})

		if assert_type == "" or assert_text == "":
			return JsonResponse({"status": 10102, "message": "断言的类型或文本不能为空"})

		# ...
		if method == "get":
			module_number = 1
		elif method == "post":
			module_number = 2
		elif method == "delete":
			module_number = 3
		elif method == "put":
			module_number = 4
		else:
			return JsonResponse({"status": 10104, "message": "未知的请求方法"})

		if parameter_type == "form":
			parameter_number = 1
		elif parameter_type == "json":
			parameter_number = 2
		else:
			return JsonResponse({"status": 10104, "message": "未知的参数类型"})

		if assert_type == "contains":
			assert_number = 1
		elif assert_type == "mathches":
			assert_number = 2
		else:
			return JsonResponse({"status": 10104, "message": "未知的断言类型"})

		ret = TestCase.objects.create(name=name, module_id=module_id,
		                              url=url, method=module_number, header=header,
		                              parameter_type=parameter_number, parameter_body=parameter_body,
		                              assert_type=assert_number, assert_text=assert_text)
		print(ret)

		return JsonResponse({"status": 10200, "message": "创建成功！"})

	else:
		return JsonResponse({"status": 10100, "message": "请求方法错误"})
