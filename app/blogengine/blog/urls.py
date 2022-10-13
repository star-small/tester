from django.urls import path
from .views import *
urlpatterns = [
    path('', first_list),
    path('Createtest', createTest_page),
    path('singIn', singIn_page),
    path('singUp', singUp_page),
    path('home', first_list),
]