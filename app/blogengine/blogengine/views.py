# from http.client import HTTPResponse
from django.http import HttpResponse 

def hello(request):
    return HttpResponse('<h1>hellos</h1>')