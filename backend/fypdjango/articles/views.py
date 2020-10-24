import json

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def testingReact(request):

    x = '{ "name":"John", "age":30, "city":"New York"}'
    y = json.loads(x)

    return HttpResponse(y["age"])
