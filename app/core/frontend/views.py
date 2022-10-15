from django.shortcuts import render
from django.http import HttpResponse 

def show_home_page(request):
    return render(request,'frontend/home.html')

def show_signIn(request):
    return render(request,'frontend/singIn.html')

def show_signUp(request):
    return render(request,'frontend/singUp.html')