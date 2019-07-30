from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.views.decorators.csrf import csrf_exempt

import hashlib

# Create your views here.
@csrf_exempt
def weixin(request):
    if request.method == "GET":
        signature = request.GET.get('signature')
        timestamp = request.GET.get('timestamp')
        nonce = request.GET.get('nonce')
        echostr = request.GET.get('echostr')
        token = "Txy159wx"
        tmpArr = [token, timestamp, nonce]
        tmpArr.sort()
        string = ''.join(tmpArr).encode('utf-8')
        string = hashlib.sha1(string).hexdigest()
        if string == signature:
            return HttpResponse(echostr)
        else:
            return HttpResponse("false")
