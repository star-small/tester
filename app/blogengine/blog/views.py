from django.shortcuts import render
from django.http import HttpResponse 

def first_list(request):
    return render(request,'blog/index.html')

def createTest_page(request):
    return render(request,'blog/createtest.html')

def singIn_page(request):
    return render(request,'blog/singIn.html')

def singUp_page(request):
    return render(request,'blog/singUp.html')