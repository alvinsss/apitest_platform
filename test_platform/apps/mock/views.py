from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from django.views.decorators.csrf import csrf_exempt
import os
import json
# Create your views here.
def mokcmanage(request):

    return JsonResponse({"status":200,"msg":"OK","data":"result"})

@csrf_exempt
def sdkPullAds(request):
    """
    mock sdkPullAds接口的返回信息
    :param request: NULL
    :return: json data
    """
    with open (os.path.join(os.getcwd(), "apps\\mock\\adresp.json"),"r",encoding='UTF-8' ) as f:
        res = json.loads(f.read())
    return JsonResponse(res,safe=False)

@csrf_exempt
def uploadhtml(request):
    return render( request, "upload.html")

@csrf_exempt
def uploadfile(request):
    if request.method == "POST":
        company = request.POST.get( "companyF" )
        file = request.FILES.get( 'img' )  # 所有提交的文件
        coverFile = request.POST.get( "coverFile" )

        file_name = file.name
        path = "D:/static"+ '/'+ request.user.username + '/' + company + '/'
        all_path = path + file_name
        if os.path.exists( path ) is False:
            os.makedirs( path )

        if os.path.exists( all_path ) and coverFile == 'False':
            return HttpResponse( 'exists' )
        with open( all_path, 'wb' ) as f:
            for chunk in file.chunks():
                f.write( chunk )
        return HttpResponse( "ok" )


def fileExistsOrNot(request):
    company_name = request.POST.get( "company_name" )
    file_name = request.POST.get( "file_name" )
    path = "D:/static"+ '/' + company_name + '/' + file_name
    if os.path.exists( path ):
        return HttpResponse( "文件名已存在" )
    else:
        return HttpResponse( "OK" )