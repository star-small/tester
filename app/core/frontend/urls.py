from django.urls import path
from .views import *
urlpatterns = [
    path('', show_home_page, name="home_page"),
    path('signIn', show_signIn, name="signIn_page"),
    path('signUp', show_signUp, name="signUp_page"),
]