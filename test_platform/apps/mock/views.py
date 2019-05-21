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