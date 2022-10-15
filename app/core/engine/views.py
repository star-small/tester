from django.shortcuts import render
from django.shortcuts import redirect
from .models import *
# Create your views here.


def set_test(request):
    return render(request,'frontend/setTest.html')


def show_tests_list(request):
    return render(request, 'frontend/testsList.html')



def get_test_info(request):
    theme_name = request.POST['theme_name']
    test_name = request.POST['test_name']
    
    test = Test.objects.create(title=test_name)
    topic = Topic.objects.create(title=test_name, theory="wfwe")
    
    topic.tests.add(test) # many to many
    # get id: print(test.id)
    return redirect(f"/test/questions/{1}/{test.title}")
    
def create_question(request, question_id, test_name):
    return render(request, 'frontend/questions.html', context={'question_id': question_id, 'test_name': test_name})
