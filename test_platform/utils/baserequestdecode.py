# -*- coding: utf-8 -*-
import requests
import json
import base64
import re

ENDEAPI = 'http://qa.baice100.com:9009/ende'
_global_dict = {}


def _init():
    global _global_dict
    _global_dict = {}


def set_value(name, value):
    _global_dict[name] = value


def get_value(name, defValue=None):
    try:
        return _global_dict[name]
    except KeyError:
        return defValue


try:
    APICONF = get_value( 'apiconf' )
except Exception:
    pass

if not APICONF:
    url = ENDEAPI
    print( url )
    headerDict = {"Content-Type": "application/json"}
    postbody = {
        "method": "post",
        "body_type": "GetSupportBodyType"
    }

    headers = "Content-Type:application/json"
    response = requests.post( url, postbody, headers )
    if response.status_code != 200:
        print( "code is %s" % response.status_code )
    else:
        APICONF = response.content.decode()
        print( APICONF )
        set_value( 'apiconf', APICONF )


def httpReqPost(url, data, headers):
    response = requests.post( url, data, headers )
    return response


def reReplase(reg, replaseStr, content, dataDecode=False):
    if dataDecode:
        content = content.decode()
    comReg = re.compile( reg )
    m = comReg.search( content )
    if m:
        resultStr = comReg.sub( replaseStr, content )
        return resultStr
    else:
        return content


def ifjson(teststr):
    retstr = teststr
    if isinstance( retstr, str ):
        for i in range( 99999 ):
            nReg = re.compile( r'\n' )
            n = nReg.search( retstr )
            if n:
                retstr = reReplase( r'\n\s+', "", retstr )
                retstr = reReplase( r'\n', "", retstr )
            else:
                break
        mReg = re.compile( r'^\{.*}$' )
        m = mReg.search( retstr )
        if m:
            return True
    return False


def encode(url, en_data, key=None, transBinData=False, outType=None, body_type=None):
    endeurl = ENDEAPI
    print( "encode endeurl is :", endeurl )
    # 请求体加密
    en_body = {
        "method": "post",
        "type": "encode",
        "url": url,
        "body_data": en_data
    }

    if transBinData:
        en_body["key"] = key
        en_body["body_type"] = "json"
    jsonTypeFlag = True
    if ('"%s"' % body_type) in APICONF:
        en_body["body_type"] = body_type
        jsonTypeFlag = False
    headers = "Content-Type:application/json"
    response_adreq = httpReqPost( endeurl, en_body, headers )  # 如果是RC4，返回的是字符串数据，需要转二进制

    data = None

    if response_adreq.status_code != 200:
        print( "code is %s" % response_adreq.status_code )
    else:
        resdata_adreq = response_adreq.content.decode()
        if jsonTypeFlag:
            resdata_adreq = json.loads( resdata_adreq )
            data = resdata_adreq["body_data"]
        else:
            data = resdata_adreq
        if transBinData and ("decode_type" in resdata_adreq.keys()):
            if resdata_adreq["decode_type"] == "decode":
                data = data.encode()
                data = base64.b64decode( data )  # 字符串数据转换成原来的二进制数据传输
        return data
    return None


def decode(url, de_data, key=None, transBinData=False, outType=None, body_type=None, content_type=None):
    endeurl = ENDEAPI
    if not transBinData and isinstance( de_data, bytes ):
        de_data = de_data.decode()
    elif transBinData and isinstance( de_data, bytes ):  # 如果是二进制，转成字符串传输，请求加解密接口
        de_data = base64.b64encode( de_data )
        de_data = de_data.decode()

    # 返回体解密
    de_body = {
        "method": "post",
        "type": "decode",
        "url": url,
        "body_data": de_data
    }

    if transBinData:
        de_body["key"] = key
        de_body["decode_type"] = "decode"
    jsonTypeFlag = True

    if ('"%s"' % body_type) in APICONF:
        de_body["body_type"] = body_type
        jsonTypeFlag = False

    if content_type:  # for proxy decode (cm)
        de_body["content_type"] = content_type

    headers = "Content-Type:application/json"
    response_adresp = httpReqPost( endeurl, de_body, headers )  # 如果是RC4，解密前要二进制转字符串传输
    data = None

    if response_adresp.status_code != 200:
        print( "code is %s" % response_adresp.status_code )
        retresponse = response_adresp.content.decode()
        print( retresponse )
    else:
        retresponse = response_adresp.content.decode()
        if jsonTypeFlag:
            retresponse = json.loads( retresponse )
            data = retresponse["body_data"]
        else:
            data = retresponse
        if transBinData:
            if ifjson( data ):
                return json.loads( data )
            return data
        if jsonTypeFlag:
            if ifjson( data ):
                return json.loads( data )
            return data
        return data
    return None


def endepost(url, bodydata, key=None, postheaders=None, transBinData=False, body_type=None):
    reqdata = encode( url, bodydata, transBinData=transBinData, body_type=body_type )  # 先将请求体加密
    print( "endepost reqdata is :", reqdata )
    headers = postheaders
    response = httpReqPost( url, reqdata, headers )  # 请求接口

    if response.status_code != 200:
        print( "code is %s" % response.status_code )
        print( response.json() )
    else:
        resptime = response.elapsed.total_seconds()
        if transBinData:
            resdata = response.content
            resdata = base64.b64encode( resdata )
            resdata = resdata.decode()  # 如RC4，二进制数据转换成字符串数据进行传输
        else:
            resdata = response.content.decode()
        de_resp = decode( url, resdata, transBinData=transBinData, body_type=body_type )  # 最后将接口返回解密
        rettuple = (de_resp, resptime)
        return rettuple
    return None
