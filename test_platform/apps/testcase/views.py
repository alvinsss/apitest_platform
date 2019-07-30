from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.db.models import Q,F
from testcase.models import TestCase
from project.models import Project
from module.models import Module
import requests
import json
import  time
import baserequestdecode

@login_required
def testcase_manage(request):
    # 查询全部数据
    """ 用例列表"""
    # case_list = TestCase.objects.all()
    print("testcase")
    case_list = TestCase.objects.filter(status="1").order_by("-create_time")
    p = Paginator(case_list,15)
    page = request.GET.get('page')
    try:
        contacts = p.page(page)
    except PageNotAnInteger:
        # 如果页数不是整型, 取第一页.
        contacts = p.page(1)
    except EmptyPage:
        # 如果页数超出查询范围，取最后一页
        contacts = p.page(p.num_pages)
    print("contacts is:",contacts)
    return render(request, "case_list.html", {"cases": contacts})
    # return render(request, "case_list.html", {"type": "debug"})

def _dict_generator(indict, pre=None):
    pre = pre[:] if pre else []
    if isinstance(indict, dict):
        for key, value in indict.items():
            if isinstance(value, dict):
                if len(value) == 0:
                    yield pre+[key, '{}']
                else:
                    for d in _dict_generator(value, pre + [key]):
                        yield d
            elif isinstance(value, list):
                if len(value) == 0:
                    yield pre+[key, '[]']
                else:
                    for v in value:
                        for d in _dict_generator(v, pre + [key]):
                            yield d
            elif isinstance(value, tuple):
                if len(value) == 0:
                    yield pre+[key, '()']
                else:
                    for v in value:
                        for d in _dict_generator(v, pre + [key]):
                            yield d
            else:
                yield pre + [key, value]
    else:
        yield indict


@login_required
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
            payload = json.loads(json_par,strict=False)
            # payload = json.loads(json_par)
        except json.decoder.JSONDecodeError:
            return JsonResponse({"result": "参数类型错误"})
        # finally:
        #     print("finally")
        #     payload = json_par

        result_text = None
        if method == "get":
            if header == "":
                requests.packages.urllib3.disable_warnings()
                r = requests.get(url, params=payload,verify=False)
                result_text = r.text
            else:
                requests.packages.urllib3.disable_warnings()
                r = requests.get(url, params=payload, headers=header,verify=False)
                result_text = r.text

        if method == "post":
            if type_ == "form":
                if header == "":
                    requests.packages.urllib3.disable_warnings()
                    r = requests.post(url, data=payload,verify=False)
                    result_text = r.text
                else:
                    requests.packages.urllib3.disable_warnings()
                    r = requests.post(url, data=payload, headers=header,verify=False)
                    result_text = r.text

            if type_ == "json":
                if header == "":
                    requests.packages.urllib3.disable_warnings()
                    r = requests.post(url, json=payload,verify=False)
                    result_text = r.text
                    print("json",r.text)

                else:
                    requests.packages.urllib3.disable_warnings()
                    r = requests.post(url, json=payload, headers=header,verify=False)
                    print("url is:",url,"json is",payload,"header is",header)
                    print("json has header ",r.text)
                    result_text = r.text

            if type_ == "json" and encryption == "1":
                print("encryption=1,type_=json")
                # header = _str_toJson( header )
                print("json encryption == 1 ----> parameter",url,parameter)
                r =baserequestdecode.endepost(url, parameter, key=None, postheaders=None, transBinData=False, body_type=None)
                result_text = json.dumps(r)
                print("result_text",result_text)

            if type_ == "form" and encryption == "1":
                print("encryption=1,type_=form")
                # header = _str_toJson( header )
                print("form encryption == 1 ----> parameter",url,parameter)
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
@login_required
def testcase_assert(request):
    '''
    断言
    :param request:
    :return:
    '''
    if request.method == "POST":
        result_text = request.POST.get("result", "")
        assert_text = request.POST.get("assert", "")
        assert_type = request.POST.get("assert_type", "")
        if result_text == "" or assert_text == "":
            return JsonResponse({"result": "断言的文本不能为空！"})

        if assert_type == "contains":
            # 处理前端数据包含 | 表示并的关系，全部内容包含断言为真
            assert_list = assert_text.split('|')
            print("contains",assert_list)
            for assert_text in assert_list:
                # print("assert_text",assert_text)
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
@login_required
def testcase_save(request):
    """
    用例保存或修改case
    """
    if request.method == "POST":
        selectModule = request.POST.get("selectModule", "")
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

        print("selectModule", selectModule)
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
     case.status = False
     case.save()
     return HttpResponseRedirect("/testcase/")

@csrf_exempt
@login_required
def sendreqsnfun(request):
    """
    测试发送多次
    """
    if request.method == "POST":
        url = request.POST.get("url", "")
        method = request.POST.get("method", "")
        header = request.POST.get("header", "")
        type_ = request.POST.get("type", "")
        parameter = request.POST.get("parameter", "")
        encryption = request.POST.get("encryption","")
        num = int(request.POST.get("sendreqcounts",""))
        print("url", url)
        print("method", method)
        print("header", header)
        print("type_", type_)
        print("parameter", parameter)
        print("num",num)



        if ( num > 500 ):
            return JsonResponse({"result": "请求次数不能大于500"})

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
                requests.packages.urllib3.disable_warnings()
                r = requests.get(url, params=payload,verify=False)
                reqtime_list = []
                reqtotal_counts = num
                reqtotal_time = 0
                while num > 0:
                    num = num - 1
                    start_time = time.clock()
                    result_text = r.text
                    request_time = time.clock() - start_time
                    reqtotal_time = round( request_time, 6 ) + reqtotal_time
                    reqtime_list.append( ("第" + str( (num + 1) ) + "次请求" + str( round( request_time, 6 ) )) )
                response_avg = round( (round( reqtotal_time, 4 ) / reqtotal_counts), 6 )
                reqtime_list.append( ("平均响应时间：" + str( response_avg )) )
                print( "reqtime_list", reqtime_list )
                result_text = reqtime_list
            else:
                reqtime_list = []
                reqtotal_counts = num
                reqtotal_time = 0
                while num > 0:
                    num = num -1
                    start_time = time.clock()
                    requests.packages.urllib3.disable_warnings()
                    r = requests.get(url, params=payload, headers=header,verify=False)
                    request_time = time.clock() - start_time
                    reqtotal_time = round(request_time,4) + reqtotal_time
                    reqtime_list.append(("第"+str((num+1))+"次请求"+str(round(request_time,4))))
                response_avg = round((round(reqtotal_time,4)/reqtotal_counts),4)
                reqtime_list.append(("平均响应时间："+str(response_avg)))
                print("reqtime_list",reqtime_list)
                result_text = reqtime_list


        if method == "post":
            if type_ == "form":
                if header == "":
                    reqtime_list = []
                    reqtotal_counts = num
                    reqtotal_time = 0
                    while num > 0:
                        num = num - 1
                        start_time = time.clock()
                        requests.packages.urllib3.disable_warnings()
                        r = requests.post( url, data=payload,verify=False )
                        request_time = time.clock() - start_time
                        reqtotal_time = round( request_time, 6 ) + reqtotal_time
                        reqtime_list.append( ("第" + str( (num + 1) ) + "次请求" + str( round( request_time, 6 ) )) )
                    response_avg = round( (round( reqtotal_time, 4 ) / reqtotal_counts), 6 )
                    reqtime_list.append( ("平均响应时间：" + str( response_avg )) )
                    print( "reqtime_list", reqtime_list )
                    result_text = reqtime_list

                else:
                    reqtime_list = []
                    reqtotal_counts = num
                    reqtotal_time = 0
                    while num > 0:
                        num = num - 1
                        start_time = time.clock()
                        requests.packages.urllib3.disable_warnings()
                        r = requests.post( url, data=payload, headers=header,verify=False )
                        request_time = time.clock() - start_time
                        reqtotal_time = round( request_time, 6 ) + reqtotal_time
                        reqtime_list.append( ("第" + str( (num + 1) ) + "次请求" + str( round( request_time, 6 ) )) )
                    response_avg = round( (round( reqtotal_time, 4 ) / reqtotal_counts), 6 )
                    reqtime_list.append( ("平均响应时间：" + str( response_avg )) )
                    print( "reqtime_list", reqtime_list )
                    result_text = reqtime_list

            if type_ == "json":
                if header == "":
                    reqtime_list = []
                    reqtotal_counts = num
                    reqtotal_time = 0
                    while num > 0:
                        num = num - 1
                        start_time = time.clock()
                        requests.packages.urllib3.disable_warnings()
                        r = requests.post( url, json=payload ,verify=False)
                        request_time = time.clock() - start_time
                        reqtotal_time = round( request_time, 6 ) + reqtotal_time
                        reqtime_list.append( ("第" + str( (num + 1) ) + "次请求" + str( round( request_time, 6 ) )) )
                    response_avg = round( (round( reqtotal_time, 4 ) / reqtotal_counts), 6 )
                    reqtime_list.append( ("平均响应时间：" + str( response_avg )) )
                    print( "reqtime_list", reqtime_list )
                    result_text = reqtime_list
                else:
                    reqtime_list = []
                    reqtotal_counts = num
                    reqtotal_time = 0
                    while num > 0:
                        num = num - 1
                        start_time = time.clock()
                        requests.packages.urllib3.disable_warnings()
                        r = requests.post( url, json=payload, headers=header,verify=False )
                        request_time = time.clock() - start_time
                        reqtotal_time = round( request_time, 6 ) + reqtotal_time
                        reqtime_list.append( ("第" + str( (num + 1) ) + "次请求" + str( round( request_time, 6 ) )) )
                    response_avg = round( (round( reqtotal_time, 4 ) / reqtotal_counts), 6 )
                    reqtime_list.append( ("平均响应时间：" + str( response_avg )) )
                    print( "reqtime_list", reqtime_list )
                    result_text = reqtime_list

            # 只做POST的json格式的加密处理
            if type_ == "json" and encryption == "1":
                print("encryption=1,type_=json")
                # header = _str_toJson( header )
                reqtime_list = []
                reqtotal_counts = num
                reqtotal_time = 0
                while num > 0:
                    num = num - 1
                    start_time = time.clock()
                    r = baserequestdecode.endepost( url, parameter, key=None, postheaders=None, transBinData=False,
                                                    body_type=None )
                    request_time = time.clock() - start_time
                    reqtotal_time = round( request_time, 6 ) + reqtotal_time
                    reqtime_list.append( ("第" + str( (num + 1) ) + "次请求" + str( round( request_time, 6 ) )) )
                response_avg = round( (round( reqtotal_time, 4 ) / reqtotal_counts), 6 )
                reqtime_list.append( ("平均响应时间：" + str( response_avg )) )
                print( "reqtime_list", reqtime_list )
                result_text = reqtime_list
        return JsonResponse({"result": result_text})

    else:
        return JsonResponse({"result": "请求方法错误"})


# def get_timestamp(request):
#     timestamp = int( round( time.time() * 1000 ) )
#     print( int( round( time.time() * 1000 ) ) )  # 1381419600
#     return JsonResponse({"result": timestamp})

@csrf_exempt
def search_name(request):
    """ 搜索用例名称 """
    case_name = request.GET.get("caseName",None)
    if len(case_name) == 0 :
        return HttpResponseRedirect( "/testcase/" )
    else:
        case_list = TestCase.objects.filter(Q(name__contains=(case_name.strip()))|Q(url__contains=(case_name.strip()))).order_by('-create_time')
        p = Paginator(case_list, 3)
        page = request.GET.get('page')
        try:
            contacts = p.page(page)
        except PageNotAnInteger:
            # 如果页数不是整型, 取第一页.
            contacts = p.page(1)
        except EmptyPage:
            # 如果页数超出查询范围，取最后一页
            contacts = p.page(p.num_pages)
        return render(request, "case_list.html", {"cases": contacts, "name": case_name})


@csrf_exempt
def get_case_info(request):
    """获取case接口数据"""
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
def getselect_data(request):
    """
    获取 "项目>模块" 列表
    :param request:
    :return: 项目接口列表
    项目和任务控制状态，在模块和用例不控制状态
    """
    print("getselect_data")
    if request.method == "GET":
        # project_list = Project.objects.all()
        project_list = Project.objects.filter(del_status=1)
        data_list = []
        for project in project_list:
            project_dict = {
                "id": project.id,
                "name": project.name
            }

            module_list = Module.objects.filter(project_id=project.id,del_status=1)
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
