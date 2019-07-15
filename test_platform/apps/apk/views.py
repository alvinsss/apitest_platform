from django.shortcuts import render
from project.models import Project
from apk.models import APK_UPLOADFILE
from apk.models import APK_RESULTS
from django.conf import settings
from django.http import JsonResponse ,HttpResponseRedirect,HttpResponse
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.views.decorators.csrf import  csrf_exempt

import platform
import os
import time
# Create your views here.
# 管理页面
# @login_required

def apk_list(request):
    print("apk_list")
    apkfile_all = APK_UPLOADFILE.objects.filter(del_status=0)
    p= Paginator(apkfile_all,15)
    page = request.GET.get('page')
    try:
        apkfile_page = p.page(page)
    except PageNotAnInteger:
        apkfile_page = p.page(1)
    print("apkfile_page:",apkfile_page)
    return render(request, "apk_list.html",{"apkfiles": apkfile_page , "type": "list"})


def add_apk(request):
    print("add apk ")
    return render(request,"apk_add.html")

def result(request,apkid):
    print("URL values result",apkid)
    results = APK_RESULTS.objects.filter(batch_id_id=apkid)
    p= Paginator(results,15)
    page = request.GET.get('page')
    try:
        results = p.page(page)
    except PageNotAnInteger:
        results = p.page(1)
    print("results_page:",results)
    return render(request,"apk_result.html",{"results":results,"type":"result"})



def detail_result(request,resultid):
    print("detail_apkresult",resultid)
    results = APK_RESULTS.objects.filter(id=resultid).order_by("apk_testtype")
    print(results)
    return render(request,"apk_detail_result.html",{"results":results,"type":"apk_detail_result"})

@csrf_exempt
def get_detail_result(request):
    print("get_detail_result result_id is:")
    if request.method == "POST":
        id = request.POST.get("result_id", "")
        if id == "":
            return JsonResponse({"status": 10102, "message": "id不能为空"})
        else:
            #get  JSON serializable, filter 返回非JSON
            r = APK_RESULTS.objects.get( id=id )
            print("--------->", r.detail,type(r.detail))
    return JsonResponse( {"status": 10200, "message": "success", "data": r.detail} )


@csrf_exempt
def save_uploadapkfile(request):

    if request.method == "GET":
        return render(request,"apk_list.html")

    if request.method == "POST":
        module_id  = request.POST.get( "module_id", "" )
        module_id  = "36"
        print("module_id",module_id)
        name_des   = request.POST.get("name_des","")
        uploadfile = request.FILES.get("file_obj",None)    # 获取上传的文件，如果没有文件，则默认为None
        tfid       = request.POST.get("tfid","")
        apk_testtype = request.POST.getlist("apk_testtype","")
        userid     = request.user.id
        username   = request.user
        print(name_des,uploadfile,tfid,username,userid)
        print("apk_testtype----->",apk_testtype,type(apk_testtype))
        if (platform.system() == "Windows"):
            tmp_dirs = 'D:\static\lapk'
            tmp_dir = os.path.join( tmp_dirs, str( username ),
                                    str( time.strftime( "%Y-%m-%d_%H%M%S", time.localtime() ) ) )
            print(tmp_dir)
        else:
            tmp_dir = os.path.join( settings.FILE_APK, str( username ),
                                    str( time.strftime( "%Y-%m-%d_%H:%M:%S", time.localtime() ) ) )
            print(tmp_dir)
        if not os.path.exists( tmp_dir ):
            print( tmp_dir + " not exists ,create dir is starting" )
            os.makedirs( tmp_dir )
        # tfid即新建
        if tfid == "":
            print("tfid is null ,create action")
            if not uploadfile:
                return JsonResponse( {"status": 10200, "message": "上传文件不存在！"} )
            if uploadfile.name.split( '.' )[-1] not in ['zip','apk']:
                return JsonResponse( {"status": 10200, "message": "上传文件类型错误！"} )
            FileName = os.path.join( tmp_dir, uploadfile.name )
            try:
                with open( FileName, 'wb+' ) as f:
                    # 分块写入文件
                    for chunk in uploadfile.chunks():
                        f.write( chunk )
                    if  userid == None  :
                        print("userid is nulll")
                        APK_UPLOADFILE.objects.create(module_id=module_id,userid="9999",username="AnonyUser",name_des=name_des,upfilepath=FileName,apk_testtype=apk_testtype )
                    else:
                        print("userid is has values")
                        APK_UPLOADFILE.objects.create( userid=userid,module_id=module_id,username=username,name_des=name_des,upfilepath=FileName,apk_testtype=apk_testtype )

                    print("APK_UPLOADFILE.objects.create!")
                    #上传文件是zip的格式处理
                    if uploadfile.name.split( '.' )[-1] in ['zip']:
                        cmdinfo = 'unzip'+' '+FileName+' '+'-d'+' '+tmp_dir
                        print("cmdinfo",cmdinfo)
                        os.system(cmdinfo)
                        time.sleep(10)
                        print("upload files type is zip, start unzip file")
                        apk_fileslist =_get_apkpath(tmp_dir)
                        print("apk_fileslist",apk_fileslist)
                        id_list_maxid = APK_UPLOADFILE.objects.values_list('id',flat=True).last()
                        get_testtype = APK_UPLOADFILE.objects.get(id=id_list_maxid).apk_testtype
                        testtype_list = get_testtype[2:-2].split(',')
                        if  userid == None  :
                            print("userid is nulll")
                            for type_test in testtype_list:
                                for files in apk_fileslist:
                                    APK_RESULTS.objects.create( userid="9999",username="AnonyUser",name_des=name_des,apk_testtype=type_test,upfilepath=FileName,apkfile_path=files,batch_id_id=id_list_maxid,module_id=module_id )
                        else:
                            for type_test in testtype_list:
                                for files in apk_fileslist:
                                    APK_RESULTS.objects.create( userid=userid,username=username,name_des=name_des, apk_testtype=type_test,
                                                                upfilepath=FileName,apkfile_path=files,batch_id_id=id_list_maxid,module_id=module_id )


                    else:
                        # values_list方法加个参数flat = True可以获取number的值列表。
                        apk_fileslist =_get_apkpath(tmp_dir)
                        print("upload files type is apk!")
                        id_list_maxid = APK_UPLOADFILE.objects.values_list('id',flat=True).last()
                        print("buildings_list",id_list_maxid)
                        get_testtype = APK_UPLOADFILE.objects.get(id=id_list_maxid).apk_testtype
                        testtype_list = get_testtype[2:-2].split(',')
                        print("testtype_list",testtype_list)
                        if  userid == None  :
                            print("userid is nulll")
                            for type_test in testtype_list:
                                for files in apk_fileslist:
                                    APK_RESULTS.objects.create( userid="9999",username="AnonyUser",name_des=name_des,apk_testtype=type_test,upfilepath=FileName,apkfile_path=files,batch_id_id=id_list_maxid,module_id=module_id )
                        else:
                            for type_test in testtype_list:
                                for files in apk_fileslist:
                                    APK_RESULTS.objects.create( userid=userid,username=us,name_des=name_des,apk_testtype=type_test,upfilepath=FileName,apkfile_path=files,batch_id_id=id_list_maxid,module_id=module_id )

            except Exception as e:
                print( e )
            return JsonResponse( {"status": 10200, "message": "创建成功！", "data": FileName} )
        else:
            if uploadfile == None:
                print("修改，未修改上传文件",uploadfile)
                apk_uploadinfo = APK_UPLOADFILE.objects.get( id=tfid )
                apk_uploadinfo.userid = userid
                apk_uploadinfo.name_des = name_des
                apk_uploadinfo.apk_testtype = apk_testtype
                apk_uploadinfo.save()
                return JsonResponse( {"status": 10200, "message": "修改成功！", "data": apk_uploadinfo.name_des} )
            else:
                print("修改上传文件",uploadfile)
                FileName = os.path.join( tmp_dir, uploadfile.name )
                try:
                    with open( FileName, 'wb+' ) as f:
                        # 分块写入文件
                        for chunk in uploadfile.chunks():
                            f.write( chunk )
                    apk_uploadinfo = APK_UPLOADFILE.objects.get( id=tfid )
                    apk_uploadinfo.userid = userid
                    apk_uploadinfo.name_des = name_des
                    apk_uploadinfo.apk_testtype = apk_testtype
                    apk_uploadinfo.upapkfile = FileName
                    apk_uploadinfo.save()
                except Exception as e:
                    print( e )
                return JsonResponse( {"status": 10200, "message": "修改成功！", "data": FileName} )
        return render(request,"apk_add.html")

@csrf_exempt
def run_apk_task(request):
    if request.method == "POST":
        tid = request.POST.get("tid","")
        print( "run_apk_task", tid )
        if tid == "":
            return JsonResponse({"status": 10102, "message": "id不能为空"})
        task_info = APK_UPLOADFILE.objects.get(id=tid)
        return JsonResponse( {"status": 10200, "message": "执行开始"} )

    pass


def _get_apkpath(dirname):
    filter = [".apk"]#需要获取的文件类型
    result=[]
    for maindir,subdir,file_name_list in os.walk(dirname):
        for filename in file_name_list:
            apath = os.path.join(maindir,filename)
            print("apath",apath)
            ext = os.path.splitext(apath)[1]# 获取文件后缀 [0]获取的是除了文件名以外的内容
            print("ext",ext)
            if ext in filter:
                result.append(apath)
    return result
