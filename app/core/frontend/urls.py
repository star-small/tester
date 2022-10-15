from django.urls import path
from .views import *
urlpatterns = [
    path('', show_home_page, name="home_page"),
    path('singIn', show_signIn, name="signIn_page"),
    path('singUp', show_signUp, name="signUp_page"),
]