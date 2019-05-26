from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from testcase.models import TestCase
from project.models import Project
from module.models import Module
from utils import  baserequestdecode
import requests
import json



# Create your views here.
def testcase_manage(request):
    # 查询全部数据
    case_list = TestCase.objects.all()
    return render(request, "case_list.html", {"cases": case_list})
    # return render(request, "case_list.html", {"type": "debug"})

@csrf_exempt
def testcase_debug(request):
    """
    测试用例的调试
    """
    if request.method == "POST":
        url = request.POST.get("url", "")
        method = request.POST.get("method", "")
        header = request.POST.get("header", "")
        type_ = request.POST.get("type", "")
        parameter = request.POST.get("parameter", "")
        encryption = request.POST.get("encryption","")
        print("url", url)
        print("method", method)
        print("header", header)
        print("type_", type_)
        print("parameter", parameter)
        print("encryption",encryption)

        json_header = header.replace("\'", "\"")
        try:
            header = json.loads(json_header)
        except json.decoder.JSONDecodeError:
            return JsonResponse({"result": "header类型错误"})

        json_par = parameter.replace("\'", "\"")
        try:
            payload = json.loads(json_par)
        except json.decoder.JSONDecodeError:
            return JsonResponse({"result": "参数类型错误"})

        result_text = None
        if method == "get":
            if header == "":
                r = requests.get(url, params=payload)
                result_text = r.text
            else:
                r = requests.get(url, params=payload, headers=header)
                result_text = r.text

        if method == "post":
            if type_ == "form":
                if header == "":
                    r = requests.post(url, data=payload)
                    result_text = r.text
                else:
                    r = requests.post(url, data=payload, headers=header)
                    result_text = r.text

            if type_ == "json":
                if header == "":
                    r = requests.post(url, json=payload)
                    result_text = r.text
                else:
                    r = requests.post(url, json=payload, headers=header)
                    result_text = r.text

            # 只做POST的json格式的加密处理
            if type_ == "json" and encryption == "1":
                print("encryption=1,type_=json")
                # header = _str_toJson( header )
                r =baserequestdecode.endepost(url, parameter, key=None, postheaders=None, transBinData=False, body_type=None)
                result_text = json.dumps(r)
                print("result_text",result_text)

        return JsonResponse({"result": result_text})
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
        encryption = request.POST.get("encryption","")
        cid = request.POST.get("cid","")

        print("url", url)
        print("method", method)
        print("header", header)
        print("parameter_type", parameter_type)
        print("parameter_body", parameter_body)
        print("assert_type", assert_type)
        print("assert_text", assert_text)
        print("module_id", module_id)
        print("encryption", encryption)
        print("cid", cid)

        if name == "":
            return JsonResponse({"status": 10101, "message": "用例名称不能为空"})

        if module_id == "":
            return JsonResponse({"status": 10103, "message": "所属的模块不能为空"})

        if assert_type == "" or assert_text == "":
            return JsonResponse({"status": 10102, "message": "断言的类型或文本不能为空"})

        # ...
        if method == "get":
            method_number = 1
        elif method == "post":
            method_number = 2
        elif method == "delete":
            method_number = 3
        elif method == "put":
            method_number = 4
        else:
            return JsonResponse({"status": 10104, "message": "未知的请求方法"})

        if parameter_type == "form":
            parameter_number = 1
        elif parameter_type == "json":
            parameter_number = 2
        else:
            return JsonResponse({"status": 10104, "message": "未知的参数类型"})

        # //1加密，0不加密
        if encryption == "1":
            encryption = 1
        elif encryption == "0":
            encryption = 0
        else:
            return JsonResponse({"status": 10104, "message": "未知加密选项"})


        if assert_type == "contains":
            assert_number = 1
        elif assert_type == "mathches":
            assert_number = 2
        else:
            return JsonResponse({"status": 10104, "message": "未知的断言类型"})

        # 根据cid判断是创建还是修改
        if cid == "":
            ret = TestCase.objects.create(name=name, module_id=module_id,
                                          url=url, method=method_number, header=header,
                                          parameter_type=parameter_number, parameter_body=parameter_body,
                                          assert_type=assert_number, assert_text=assert_text,encryption = encryption)
        else:
            case = TestCase.objects.get(id=cid)
            case.name = name
            case.module_id = module_id
            case.url = url
            case.method = method_number
            case.header = header
            case.parameter_type = parameter_number
            case.parameter_body = parameter_body
            case.assert_type = assert_number
            case.assert_text = assert_text
            case.encryption = encryption
            case.save()

        return JsonResponse({"status": 10200, "message": "创建成功！"})

    else:
        return JsonResponse({"status": 10100, "message": "请求方法错误"})


def add_case(request):
    return render(request, "case_add.html", )

def edit_case(request, cid):
    """编辑用例"""
    print("编辑的用例id", cid)
    return render(request, "case_edit.html",)

def  delete_case(request,cid):
     case = TestCase.objects.get(id=cid)
     case.delete()
     return HttpResponseRedirect("/testcase")

@csrf_exempt
def get_case_info(request):
    """获取接口数据"""
    if request.method == "POST":
        cid = request.POST.get("cid", "")
        case = TestCase.objects.get(id=cid)
        module = Module.objects.get(id=case.module.id)
        project_id = module.project.id;

        case_dict = {
            "id": case.id,
            "encryption":case.encryption,
            "url": case.url,
            "name": case.name,
            "method": case.method,
            "header": case.header,
            "parameter_type": case.parameter_type,
            "parameter_body": case.parameter_body,
            "assert_type": case.assert_type,
            "assert_text": case.assert_text,
            "module_id": case.module.id,
            "project_id": project_id,
        }
        return JsonResponse({"status": 10200,
                             "message": "请求成功",
                             "data": case_dict})

    else:
        return JsonResponse({"status": 10100, "message": "请求方法错误"})

@csrf_exempt
def get_select_data(request):
    """
    获取 "项目>模块" 列表
    :param request:
    :return: 项目接口列表
    """
    if request.method == "GET":
        project_list = Project.objects.all()
        data_list = []
        for project in project_list:
            project_dict = {
                "id": project.id,
                "name": project.name
            }

            module_list = Module.objects.filter(project_id=project.id)
            module_name = []
            for module in module_list:
                module_name.append({
                    "id": module.id,
                    "name": module.name,
                })

            project_dict["moduleList"] = module_name
            data_list.append(project_dict)

        return JsonResponse({"status": 10200, "message": "success", "data": data_list})

    else:
        return JsonResponse({"status": 10100, "message": "请求方法错误"})