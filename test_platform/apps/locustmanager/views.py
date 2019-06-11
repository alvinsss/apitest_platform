from django.shortcuts import render
from django.http import JsonResponse ,HttpResponseRedirect,HttpResponse
from locustmanager.models import LocustScript
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import  csrf_exempt
from django.conf import settings
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
import json
import  os,time
import platform
import  sys

@csrf_exempt
@login_required
def locustmanager(request):
	# locust管理
    locustlist = LocustScript.objects.filter(del_status=0)
    print(locustlist)
    p = Paginator(locustlist,15)
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
    return render( request, "locust_list.html", {"locustlists": contacts} )


def add_locustfile(request):
    return  render(request,"locust_add.html")



@csrf_exempt
def save_locustfile(request):
    print("---------------save_locustfile -----------------------")
    if request.method == "GET":
        return render(request,"locust_add.html")
    if request.method == "POST":    # 请求方法为POST时，进行处理
        module_id = request.POST.get("module_id", "")
        encryption = request.POST.get("encryption", "")
        scriptname = request.POST.get("lscript_name","")
        host = request.POST.get("host","")
        userid = request.user.id
        username = request.user
        uploadfile =request.FILES.get("file_obj",None)    # 获取上传的文件，如果没有文件，则默认为None
        slave_num =request.POST.get("slave_num","")
        print("module_id",module_id)
        print("encryption",encryption)
        print("scriptname",scriptname)
        print("userid",userid)
        print("host",host)
        print("uploadfile",uploadfile)
        print("file type",(uploadfile.name.split('.')[-1]))
        print("file_Name",uploadfile.name)
        print("slave_num",slave_num)

        if not uploadfile:
            return JsonResponse( {"status": 10200, "message": "上传文件不存！"} )
        if uploadfile.name.split('.')[-1] not in ['xlsx','py']:
            return JsonResponse( {"status": 10200, "message": "上传文件类型错误！"} )

        if (platform.system() == "Windows"):
            tmp_dirs = 'D:\static'
            tmp_dir = os.path.join( settings.FILE_ROOT, str( userid ),
                                    str( time.strftime( "%Y-%m-%d_%H%M%S", time.localtime() ) ) )
        else:
            tmp_dir = os.path.join( settings.FILE_ROOT, str( userid ),
                                    str( time.strftime( "%Y-%m-%d_%H:%M:%S", time.localtime() ) ) )
            # cmd_res = os.system("chattr +i /q/tools/python/wwwroot/test_platform/static/uploads/*")
            # if cmd_res == 0:
            #     print("exec os chattr is ok")
            # else:
            #     sys.exit(0);
        if not os.path.exists( tmp_dir ):
            print( tmp_dir + " not exists ,create dir is starting" )
            os.makedirs( tmp_dir )
            # os.system( r"touch {}".format( tmp_dir ) )  # 调用系统命令行来创建文件

        FileName = os.path.join( tmp_dir, uploadfile.name )
        try:
            with open( FileName, 'wb+' ) as f:
                # 分块写入文件
                for chunk in uploadfile.chunks():
                    f.write( chunk )
                LocustScript.objects.create( userid=userid,scriptname=scriptname, host=host, encryption=encryption,
                                             locustfile=FileName,module_id=module_id,username=username,slave_num=slave_num )
                return JsonResponse( {"status": 10200, "message": "创建成功！", "data": FileName} )
        except Exception as e:
                print(e)
        return render(request,"locust_add.html")

@csrf_exempt
def uploadfile(request):
    print("_-------------------uploadfile-----------------")
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
                tmp_dir = os.path.join( settings.FILE_ROOT, str( userid ),
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
def delete_locustlist(request,locustfid):
    print("delete_locustlist id",locustfid)
    if request.method == "GET":
        if locustfid:
            try:
                f = LocustScript.objects.get(id=locustfid)
            except LocustScript.DoesNotExist:
                return HttpResponseRedirect("/locustmanager")
            else:
                f.del_status = 1
                f.save()
                return HttpResponseRedirect("/locustmanager")
    elif request.method == "POST":
        return HttpResponseRedirect( "/locustmanager" )

def edit_locustlist(request,locustfid):
    pass
    return HttpResponseRedirect( "/locustmanager" )
