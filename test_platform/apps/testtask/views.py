from django.shortcuts import render
from django.http import JsonResponse ,HttpResponseRedirect
from testtask.models import  TestTask
from project.models import Project
from module.models import  Module
from testcase.models import TestCase
from testtask.models import TestResult
from testtask.extend.run_task_thread import TaskThread
from django.contrib.auth.decorators import login_required

from django.views.decorators.csrf import  csrf_exempt
import json
import os

@login_required
def testtask_manage(request):
    """
    任务管理
    """
    task_list = TestTask.objects.filter(del_status=False)
    return render(request, "task_list.html", {
        "type": "list",
        "tasks": task_list
    })

@login_required
def add_task(request):
    """
    返回创建任务页面
    """
    return render(request, "task_add.html", {
        "type": "add"
    })


def edit_task(request, tid):
    """
    返回编辑任务页面
    """
    return render(request, "task_edit.html", {
        "type": "edit"
    })

@login_required
def delete_task(request, tid):
    """
    删除任务 	TestTask.objects.get(id=tid).delete()

    """
    print("delete_task",tid)
    task = TestTask.objects.get(id=tid)
    task.del_status=True
    task.save()

    return HttpResponseRedirect("/testtask/")

@csrf_exempt
@login_required
def save_task(request):
    """
    创建/编辑任务
    """
    if request.method == "POST":
        task_id = request.POST.get("task_id", "")
        name = request.POST.get("name", "")
        desc = request.POST.get("desc", "")
        cases = request.POST.get("cases", "")
        print("name", name, desc)
        print("用例", type(cases), cases)

        if name == "" or cases == "":
            return JsonResponse({"status": 10102, "message": "Parameter is null"})

        print("任务的id--->", task_id)
        if task_id == "0":
            TestTask.objects.create(name=name, describe=desc, cases=cases)
        else:
            task = TestTask.objects.get(id=task_id)
            task.name = name
            task.describe = desc
            task.cases = cases
            task.save()

        return JsonResponse({"status": 10200, "message": "success"})
    else:
        return JsonResponse({"status": 10101, "message": "请求方法错误"})

@csrf_exempt
def get_case_tree(request):
    """
    获得用例树形结构
    """
    if request.method == "GET":
        # 过滤项目状态是关闭和是否删除标致
        projects = Project.objects.filter(del_status=1,status=1)
        data_list = []
        for project in projects:
            print("GET get_case_tree  select project is ",project)
            project_dict = {
                "name": project.name,
                "isParent": True
            }

            modules = Module.objects.filter(project_id=project.id,del_status=1)
            module_list = []
            for module in modules:
                module_dict = {
                    "name": module.name,
                    "isParent": True
                }
                # 过滤逻辑删除状态数据
                cases = TestCase.objects.filter(module_id=module.id,status=1)
                case_list = []
                for case in cases:
                    case_dict = {
                        "name": case.name,
                        "isParent": False,
                        "id": case.id,
                    }
                    case_list.append(case_dict)

                module_dict["children"] = case_list
                module_list.append(module_dict)

            project_dict["children"] = module_list
            data_list.append(project_dict)

        return JsonResponse({"status": 10200, "message": "success", "data": data_list})

    if request.method == "POST":
        tid = request.POST.get("tid", "")
        print("任务的id", tid)
        if tid == "":
            return JsonResponse({"status": 10200, "message": "任务id不能为空"})

        task = TestTask.objects.get(id=tid)
        casesList = json.loads(task.cases)
        task_data = {
            "name": task.name,
            "desc": task.describe
        }

        projects = Project.objects.filter(del_status=1,status=1)
        data_list = []
        for project in projects:
            print("POST get_case_tree  select project is ",project)
            project_dict = {
                "name": project.name,
                "isParent": True
            }

            modules = Module.objects.filter(project_id=project.id,del_status=1)
            module_list = []
            for module in modules:
                module_dict = {
                    "name": module.name,
                    "isParent": True
                }

                cases = TestCase.objects.filter(module_id=module.id,status=1)
                case_list = []
                for case in cases:
                    if case.id in casesList:
                        case_dict = {
                            "name": case.name,
                            "isParent": False,
                            "id": case.id,
                            "checked": True,
                        }
                    else:
                        case_dict = {
                            "name": case.name,
                            "isParent": False,
                            "id": case.id,
                            "checked": False,
                        }
                    case_list.append(case_dict)

                module_dict["children"] = case_list
                module_list.append(module_dict)

            project_dict["children"] = module_list
            data_list.append(project_dict)
        task_data["cases"] = data_list
        return JsonResponse({"status": 10200, "message": "success", "data": task_data})


@csrf_exempt
def run_task_stand(request):
    """ 运行任务 -廢棄 """
    if request.method == "POST":
        tid = request.POST.get( "task_id", "" )
        if tid == "":
            return JsonResponse( {"status": 10200, "message": "task id is null"} )
        task = TestTask.objects.get( id=tid )
        print( task.cases )
        case_list = json.loads( task.cases )
        print( "===>", case_list )
        test_data = {}
        for cid in case_list:
            case = TestCase.objects.get( id=cid )
            if case.method == 1:
                method = "get"
            elif case.method == 2:
                method = "post"
            else:
                method = "null"

            if case.parameter_type == 1:
                parameter_type = "from"
            else:
                parameter_type = "json"

            if case.assert_type == 1:
                assert_type = "contains"
            else:
                assert_type = "mathches"

            test_data[case.id] = {
                "url": case.url,
                "method": method,
                "header": case.header,
                "parameter_type": parameter_type,
                "parameter_body": case.parameter_body,
                "assert_type": assert_type,
                "assert_text": case.assert_text,
            }
        print( "任务下面的用例", json.dumps( test_data ) )
        case_data = json.dumps( test_data )

        from test_platform import settings
        EXTEND_DIR = settings.EXTEND_DIR
        print( "项目EXTEND_DIR的基本路径", EXTEND_DIR )
        with(open( (EXTEND_DIR + "test_data_list.json"), "w" )) as f:
            f.write( case_data )
        run_cmd = "pytest -vs " + EXTEND_DIR + "run_task_testcase.py --junitxml=" + EXTEND_DIR + "log.xml"
        print( "运行的命令", run_cmd )
        os.system( run_cmd )
        return JsonResponse( {"status": 10200, "message": "任务执行完成"} )
    else:
        return JsonResponse( {"status": 10200, "message": "failed"} )


@csrf_exempt
def run_task(request):
    """ 运行任务 """
    print("run_task----------------------->")
    if request.method == "POST":
        tid = request.POST.get("task_id", "")
        if tid == "":
            return JsonResponse({"status": 10200, "message": "task id is null"})

        # 1、在执行线程之前，判断当前有没有任务在执行
        tasks = TestTask.objects.all()
        for t in tasks:
            if t.status == 1:
                return JsonResponse({"status": 10200, "message": "当前有任务正在执行！"})

        # 2. 修改任务的状态为：1-执行中
        task = TestTask.objects.get(id=tid)
        task.status = 1
        task.save()

        # 通过多线程运行测试任务
        # TaskThread(tid).run()
        try:
            TaskThread( tid ).run()
        except Exception as e:
            print(e)
        finally:
            pass
            # task.status=2
            # task.save()

        return JsonResponse({"status": 10200, "message": "任务开始执行！"})

    else:
        return JsonResponse({"status": 10200, "message": "请求方法错误"})


def result(request, tid):
    # '''
    # 展示当前任务下的全部执行结果数据
    # :param request:
    # :param tid:
    # :return:
    # ''''''
    print("result tid",tid)
    result = TestResult.objects.filter(task_id=tid).order_by('-create_time')
    print(result)
    return render(request, "task_result.html", {"results": result, "type": "result"})


def resultdetail(request,did):
    # '''
    # 展示具体一条测试结果的详情数据
    # :param request:
    # :param did:
    # :return:
    # ''''''
    print("resultdetail did is:",did)
    resultdetail = TestResult.objects.filter(id=did)
    print(resultdetail)
    return render(request, "task_resultdetail.html", {"resultdetail": resultdetail, "type": "resultdetail"})


