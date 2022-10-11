from django.urls import path
from .views import *
urlpatterns = [
    path('', post_list),
    path('test', test_list),
]