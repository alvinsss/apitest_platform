from django.shortcuts import render
from django.http import JsonResponse ,HttpResponseRedirect,HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import  csrf_exempt
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
import os,time,re
import platform
import requests
from module.models import Module
from pyunitest.models import UnittestScript
from test_platform import settings


@csrf_exempt
@login_required
def unittestmanager(request):
	# pyunittest管理
    py_unittest = UnittestScript.objects.filter(del_status=0)
    print(py_unittest)
    p = Paginator(py_unittest,15)
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
    return render( request, "unittest_list.html", {"py_unittests": contacts} )


def add_unittesttfile(request):
    return  render(request,"unittest_add.html")



@csrf_exempt
def save_unittesttfile(request):
    '''
    新建或修改保存根据 pyfid 确定
    :param request:
    :return:
    '''
    print("---------------save_unitest file -----------------------")

    if request.method == "GET":
        return render(request,"unittest_add.html")
    if request.method == "POST":    # 请求方法为POST时，进行处理
        userid = request.user.id
        username = request.user
        module_id = request.POST.get("module_id", "")
        unittestscript_name = request.POST.get("unittestscript_name","")
        uploadfile =request.FILES.get("file_obj",None)    # 获取上传的文件，如果没有文件，则默认为None
        pyfid = request.POST.get("pyfid","")
        print("module_id",module_id)
        print("userid",userid)
        print("username",username)
        print("unittestscript_name",unittestscript_name)
        print("uploadfile",uploadfile)
        print("pyfid",pyfid)
        if (platform.system() == "Windows"):
            tmp_dirs = 'D:\static'
            tmp_dir = os.path.join( tmp_dirs, str( userid ),
                                    str( time.strftime( "%Y-%m-%d_%H%M%S", time.localtime() ) ) )
        else:
            tmp_dir = os.path.join( settings.FILE_PYROOT, str( userid ),
                                    str( time.strftime( "%Y-%m-%d_%H:%M:%S", time.localtime() ) ) )
        if not os.path.exists( tmp_dir ):
            print( tmp_dir + " not exists ,create dir is starting" )
            os.makedirs( tmp_dir )
            # os.system( r"touch {}".format( tmp_dir ) )  # 调用系统命令行来创建文件
        # pyfid空即新建
        if pyfid == "":
            print("pyfid is null create unittest upload file info")
            if not uploadfile:
                return JsonResponse( {"status": 10200, "message": "上传文件不存！"} )
            if uploadfile.name.split( '.' )[-1] not in ['xlsx','py','json']:
                return JsonResponse( {"status": 10200, "message": "上传文件类型错误！"} )
            FileName = os.path.join( tmp_dir, uploadfile.name )
            # 到分钟级别的创建目录，一般不会重复
            # if os.path.exists(FileName):
            #     os.remove(FileName)
            # else:
            #     print("需要上传的文件不存在，可以直接上传文件")
            print("需要上传的文件名是-->",FileName)

            try:
                with open( FileName, 'wb+' ) as f:
                    # 分块写入文件
                    for chunk in uploadfile.chunks():
                        f.write( chunk )
                    print(FileName+"write file is over !")
                    UnittestScript.objects.create( userid=userid, scriptname=unittestscript_name,py_file=FileName,uploadfilename=uploadfile,module_id=module_id,username=username )
                cp_file = FileName
                python_script = settings.PYTHON_UNITTEST_JENKINS_DIR
                cmd = r'cp ' + cp_file + ' ' + python_script
                print( "copy py into jenkins dir exec_cmd", cmd )
                exec_cmd = os.popen( cmd )
                exec_cmd.close()
            except Exception as e:
                print( e )

            return JsonResponse( {"status": 10200, "message": "创建成功！", "data": FileName} )
        else:
            if uploadfile == None:
                print("修改，未修改上传文件",uploadfile,pyfid)
                py_unittest = UnittestScript.objects.get(id=pyfid)
                py_unittest.userid = userid
                py_unittest.module_id = module_id
                # UnittestScript.username = username
                py_unittest.py_file = str(py_unittest.py_file)
                py_unittest.save()
                return JsonResponse( {"status": 10200, "message": "修改成功！", "data": py_unittest.py_file} )
            else:
                print("修改上传文件",uploadfile,pyfid)
                FileName = os.path.join( tmp_dir, uploadfile.name )
                try:
                    with open( FileName, 'wb+' ) as f:
                        # 分块写入文件
                        for chunk in uploadfile.chunks():
                            f.write( chunk )
                        py_unittest = UnittestScript.objects.get( id=pyfid )
                        py_unittest.scriptname = unittestscript_name
                        py_unittest.py_file = FileName
                        py_unittest.uploadfilename=uploadfile
                        py_unittest.userid = userid
                        py_unittest.module_id = module_id
                    # py_unittest.username = username
                        py_unittest.save()
                    cp_file = FileName
                    python_script = settings.PYTHON_UNITTEST_JENKINS_DIR
                    cmd = r'cp ' + cp_file + ' ' + python_script
                    exec_cmd = os.popen( cmd )
                    exec_cmd.close()
                    print( "pyfid has values copy py into jenkins dir exec_cmd", cmd )
                except Exception as e:
                    print( e )
                return JsonResponse( {"status": 10200, "message": "修改成功！", "data": FileName} )
        return render(request,"unittest_add.html")

@csrf_exempt
def uploadfile(request):

    print("_-------------------up unittest file-----------------")
    if request.method == "POST":
        print(request.FILES)
        File = request.FILES.get("uploadfile",None)
        userid = request.user.id
        print("File",File)
        if File is None:
            return HttpResponse( "没有需要上传的文件" )
        else:
            # 打开特定的文件进行二进制的写操作
            if (platform.system() == "Windows"):
                tmp_dirs = 'D:\static'
                tmp_dir = os.path.join(tmp_dirs,str( userid ),
                                    str( time.strftime( "%Y-%m-%d_%H%M%S", time.localtime() ) ) )
            else :
                tmp_dir = os.path.join( settings.FILE_PYROOT, str( userid ),
                                    str( time.strftime( "%Y-%m-%d_%H:%M:%S", time.localtime() ) ) )
            print("tmp_dir",tmp_dir)
            if not os.path.exists(tmp_dir):
                print(tmp_dir+" not exists ,create dir is starting")
                os.makedirs(tmp_dir)
                # os.system( r"touch {}".format( tmp_dir ) )  # 调用系统命令行来创建文件
            FileName = os.path.join(tmp_dir,File.name)
            with open(FileName,'wb+') as f:
                # 分块写入文件
                for chunk in File.chunks():
                    f.write( chunk )
            return JsonResponse({"status": 10200, "message": "创建成功！","data":FileName})
    else:
        return  render(request, "locust_list.html")


@csrf_exempt
def delete_py_unittest(request,pyfid):
    '''
    进行逻辑删除，db和上传的文件目前没有处理，保存不动
    :param request:
    :param pyfid:
    :return: HttpResponseRedirect 重定向
    '''
    print("delete_py_unittest id",pyfid)
    if request.method == "GET":
        if pyfid:
            try:
                f = UnittestScript.objects.get(id=pyfid)
            except UnittestScript.DoesNotExist:
                return HttpResponseRedirect("/unittest/")
            else:
                f.del_status = 1
                f.save()
                return HttpResponseRedirect("/unittest/")
    elif request.method == "POST":
        return HttpResponseRedirect( "/unittest/" )

def edit_py_unittest(request,pyfid):
    print("编辑的pyfid ",pyfid)
    return render(request,"unittest_edit.html")

@csrf_exempt
def get_unittestlist_info(request):
    '''
    修改页面获取数据返回给前端调用的地址
    :param request:
    :return: JsonResponse "status": 10200为成功，其它为失败
    '''
    print("get_py_unittest_info")
    if request.method == "POST":
        pyfid = request.POST.get("pyfid", "")
        print("pyfid",pyfid)
        file_obj = UnittestScript.objects.get(id=pyfid)
        print(file_obj)
        module = Module.objects.get(id=file_obj.module.id)
        project_id = module.project.id
        pyunittest_dict={
            "project_id":project_id,
            "module_id":file_obj.module.id,
            "uploadfile": r''+str(file_obj.py_file),
            "unittestscript_name":file_obj.scriptname,
            "id": file_obj.id,
        }
        print(pyunittest_dict)
        return JsonResponse({"status": 10200,
                             "message": "请求成功",
                             "data": pyunittest_dict})
    else:
        return JsonResponse({"status": 10100, "message": "请求方法错误"})


@csrf_exempt
def run_unittest_task(request):
    '''
    通过调用jenkins的方式执行unittest测试文件
    :param request:
    :return: JsonResponse
    '''
    print("run_unittest_task")
    try:
        url="http://172.31.1.3:8084/jenkins/job/interface_apitestByunitest_jenkins/"
        token="build?token=BIt9enzUbO4x8bYmLHBi"
        r = requests.get(url+token)
    except Exception as e:
        print(e)
    print("r.status_code",r.status_code)
    # 这个接口成功就返回201
    if r.status_code == 201 :
        return  JsonResponse({"status":10200,"message":"请求成功,查看结果"+url})
    else:
        return  JsonResponse({"status":10200,"message":"请求失败"})

