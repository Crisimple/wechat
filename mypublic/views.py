from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.views.decorators.csrf import csrf_exempt

import hashlib
import xml.etree.ElementTree as ET


# Create your views here.
# django默认开启了csrf防护，@csrf_exempt是去掉防护
@csrf_exempt
def weixin(request):
    if request.method == "GET":
        print("request: ", request)
        # 接受微信服务器get请求发过来的参数
        signature = request.GET.get('signature', None)
        timestamp = request.GET.get('timestamp', None)
        nonce = request.GET.get('nonce', None)
        echostr = request.GET.get('echostr', None)
        # 微信公众号处配置的token
        token = str("Txy159wx")
        # 将参数梵高list中排序合成字符串，再用sha1加密得到新的字符串与微信发过来的signature对比，如果相同就返回echostr给服务器，校验通过
        # ISSUES: TypeError: '<' not supported between instances of 'NoneType' and 'str'
        hashlist = [token, timestamp, nonce]
        hashlist.sort()
        hashstr = ''.join([s for s in hashlist]).encode('utf-8')
        hashstr = hashlib.sha1(hashstr).hexdigest()
        if hashstr == signature:
            return HttpResponse(echostr)
        else:
            return HttpResponse("false")
    else:
        otherContent = autoreply(request)
        return HttpResponse(otherContent)


# 自动回复
def autoreply(request):
    try:
        pass
    except Exception as e:
        return e
