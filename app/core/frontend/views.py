from django.shortcuts import render
from django.http import HttpResponse 

def show_home_page(request):
    return render(request,'frontend/home.html')

def show_signIn(request):
    #login
    return render(request,'frontend/signIn.html')

def show_signUp(request):
    #registration
    return render(request,'frontend/signUp.html')