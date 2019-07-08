# -*- coding: utf-8 -*-
# @Time    : 2019/5/15 16:59
# @Author  : alvin
# @File    : basedecode.py
# @Software: PyCharm

import json
import requests
import sys
import baserequestdecode

def qatest():
    # 雄鸡接口请求
    url = "http://t-fir.antuzhi.com/fir/e/v1/pw?p=1&v=14&t=1557310286989&g=2"
    bodydata = '{"imei":"865110030338900","m1":"b8ec57b1c30ca68ccdac311a1fe481ed","cpu_id":"","solution":"Meizu","brand":"Meizu","model":"M721C","channel":"","install_app_ver_list":[{"pkgname":"com.qiyi.video","vercode":81230},{"pkgname":"com.ss.android.ugc.live","vercode":570},{"pkgname":"com.sina.news","vercode":570}],"pub_id":"1","proto_version":"1.0","lbs":{"bt":"-1,1,41053,7187835,-63","bt_t":"1553494295182","wf":"dcda809ff9e058+3a3a4d22441b50+dcda809ff80037+dcda809ff80137+dcda809ff9e155+06d3b073943968+74a78e831eb967+dcda80a010a062+dcda80a010a163+dcda80a001c073+dcda80a001c173+089b4b9a221981+0a9b4b9a221981+dcda80a001d172+dcda80a00c6073+dcda80a00c6172+7cd95cad74b585+dcda80a010b058+dcda80a010b158","wf_t":"1553494295185","wm":"dcda809ff9e059","gps_s":"0.0","gps_r":"30.0","lat":"39.910609","lon":"116.506482","gps_t":"1553494290367"},"exec_state":[{"offer_pkg_name":"com.ss.android.ugc.aweme","agent_id":"7","material_id":"c9ddfaa51671fb4249b392bb67d2cc43","ver_name":"5.0.0","ver_code":500,"pull_way":"pull_app_launch","pull_times":0,"left_pull_times":2},{"offer_pkg_name":"com.jiushizhuan.release","agent_id":"8","material_id":"c8067eefcb00ef6625910e9d174daefc","ver_name":"3.2.0","ver_code":8331,"pull_way":"pull_app_launch","pull_times":0,"left_pull_times":1}],"version_name":"1.9.002_VER_32535899255715"}'
    headers = None
    ret = baserequestdecode.endepost( url, bodydata, postheaders=headers, transBinData=True )
    print( ret )

def qatest2():
    # 熊猫广告接口请求
    url = "http://t.hye.antuzhi.com/malacca/sdkPullAds.do?g=1"
    bodydata = '{"adspaces":[{"adspace_id":"528","adspace_position":0,"adspace_type":2,"allowed_html":false,"asset":[1,2,3,4],"height":1626,"impression_num":1,"impression_time":8,"interaction_type":[2,3,7],"keywords":"","open_type":0,"page_id":"","rec_type":0,"session_data":"","width":1080}],"api_version":"1.0","app":{"app_id":"53","app_key":"wP4KCkMvI5o1NyVF6XsupWgwj2AlQH69","app_keywords":"","app_name":"头条001","app_version":"1000","category":"","channel_id":"","package_name":"com.yanggan.toutiao"},"bid":"D92F99E92C310E7E6D95F6DFD5671317","cache_hit_count":0,"device":{"brand":"Meizu","channel":"no channel number","device_id":[{"device_id":"fedb25c52a149c22","device_id_type":3,"hash_type":0},{"device_id":"460021887814030","device_id_type":8,"hash_type":0},{"device_id":"d8:6c:02:ef:79:0d","device_id_type":4,"hash_type":0},{"device_id":"869086031367120","device_id_type":10,"hash_type":0},{"device_id":"1113d250c6a384bab51ea845edb14380","device_id_type":1,"hash_type":0},{"device_id":"13bc9a5cf869669deff9c31a4ef79efbd36c860f","device_id_type":9,"hash_type":0}],"device_type":2,"jailbreaked":false,"language":"zh","model":"M1852","os_type":2,"os_version":"8.1.0","os_version_code":27,"screen_density":3,"screen_height":2076,"screen_orientation":1,"screen_width":1080},"is_debug":false,"launch_miniprogram_support":true,"need_cache_asset":true,"network":{"bt":"","carrier_id":70120,"cellular_id":{"CID":-1,"LAC":-1,"MCC":"460","MNC":"02"},"ip":"172.21.50.44","is_abroad":0,"network_type":1,"real_carrier_id":"460021887814030","wifi_aps":[{"bssid":"020000000000","is_connected":true,"name":"<unknown ssid>","rssi":-61}]},"request_last_count":0,"sdk_type":"clover","sdk_version_code":"10200","ua":"Mozilla/5.0 (Linux; Android 8.1.0; M1852 Build/OPM1.171019.026; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/65.0.3325.109 Mobile Safari/537.36" ,"launch_miniprogram_support":true}'
    ret = baserequestdecode.endepost(url, bodydata, postheaders=None, transBinData=False)
    print(ret)


def sdkPullAds():
    # 熊猫广告接口请求
    url = "http://t.hye.antuzhi.com/malacca/sdkPullAds.do"
    bodydata = '{"adspaces":[{"adspace_id":"595","adspace_position":0,"adspace_type":4,"allowed_html":false,"asset":[],"channel":"","height":0,"impression_num":2,"impression_time":8,"interaction_type":[2,3,7,8],"keywords":"","open_type":0,"page_id":"","rec_type":0,"session_data":"","width":0}],"api_version":"0","app":{"app_id":"48","app_key":"wP4KCkMvI5o1NyVF6XsupWgwj2AlQH66","app_keywords":"","app_name":"ifbiz","app_version":"201080","category":"","channel_id":"","from_package_name":"","newstype":"keji","package_name":"com.bc.if.biz","pgnum":1},"bid":"08040dde73bd0074e3af7b427c7f1213","browser_ua":"","cache_hit_count":0,"device":{"brand":"HONOR","channel":"","device_id":[{"device_id":"9f0685fac469914d","device_id_type":10,"hash_type":0},{"device_id":"9f0685fac469914d","device_id_type":3,"hash_type":0},{"device_id":"2d2a9f12a466d21c46a1bf7fe5cf67f3","device_id_type":1,"hash_type":0},{"device_id":"","device_id_type":8,"hash_type":0}],"device_type":2,"installer_package_version":"","jailbreaked":false,"language":"","model":"STF-AL10","os_type":2,"os_version":"8.0.0","screen_density":3,"screen_height":1920,"screen_orientation":1,"screen_width":1080},"ext":"","gps":{"accuracy":"","latitude":"","longitude":"","speed":"0.0","timestamp":1558335222858,"type":1},"is_debug":false,"launch_miniprogram_support":false,"need_cache_asset":false,"network":{"bt":"","carrier_id":0,"cellular_id":{"CID":0,"LAC":0,"MCC":"CN","MNC":""},"ip":"124.127.205.82","is_abroad":0,"network_type":1,"real_carrier_id":""},"request_last_count":0,"sdk_type":"clover","sdk_version":"1.0","sdk_version_code":"0","ua":"Mozilla/5.0 (Linux; Android 6.0; 1503-A01 Build/MRA58K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.95 Mobile Safari/537.36"}'
    ret = baserequestdecode.endepost(url, bodydata, postheaders=None, transBinData=False)
    t_s = json.dumps(ret)
    print("ret",type(ret),type(t_s))
    rets=requests.post(url,bodydata,verify=False)
    print("rets.text is:",rets.text)
    print("ret.text is:",ret)
    print("t_s is:",t_s)



def qatest3():
    #常用软件的base64算法，解密
    destr = "FbCYNMCcCaF="
    url = "http://t.hye.antuzhi.com/malacca/sdkPullAds.do?g=1"
    ret = baserequestdecode.decode(url, destr, body_type="BCbase64")
    print(type(ret),ret)
    if isinstance(ret, dict):
       ret = json.dumps(ret)

if __name__ == "__main__":
    qatest2()

    # '''
    # baserequestdecode 拷贝到$python_dir/Lib目录下
    # '''