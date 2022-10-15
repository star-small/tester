from django.urls import path
from .views import *
urlpatterns = [
    path('', show_tests_list, name="tests_list_page"),
    path('setTest', set_test, name="set_test_page"),
    path('testCreating', get_test_info, name="get_test_info_page"),
    path('questions/<int:question_id>/<str:test_name>', create_question, name="create_question_page")

]