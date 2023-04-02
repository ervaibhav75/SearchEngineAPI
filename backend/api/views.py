from django.shortcuts import render
import json
# Create your views here.

from django.http import JsonResponse

def api_home(request, *args, **kwargs):
    body = request.body #byte string of json data
    print("hii")
    print(request.GET)
    data ={}
    try:
        data = json.loads(body)

    except:
        pass

    #data['headers'] = request.headers
    data['content_type'] = request.content_type
    data['params'] = dict(request.GET)
    print(data)
    return JsonResponse(data)

