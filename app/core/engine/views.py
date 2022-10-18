from django.shortcuts import render
from django.shortcuts import redirect
from .models import *
# Create your views here.


def set_test(request):
    return render(request,'frontend/setTest.html')


def show_tests_list(request):
    return render(request, 'frontend/testsList.html')



def get_test_info(request):
    test_name = request.POST['test_name'] # parse from post request
    test = Test.objects.create(title=test_name) # creating new test

    # get id: print(test.id)
    return redirect(f"/test/questions/{1}/{test.id}")
    
def create_question(request, question_id, test_id):
    if question_id == 1: # if this question is the first - we are nothing to do
        return render(request, 'frontend/questions.html', context={'question_id': question_id, 'test_id': test_id})
    else:
        question_text = request.POST['question']  
        right_positions = [int(i) for i in request.POST.getlist('right_position')] # [0, 2] 
        answers = request.POST.getlist('answers') # ['a', 'b', 'c']
        right_answers = [answers[i] for i in right_positions] # ['a', 'c']

        #/1/2
        q = Question.objects.create(text=question_text, question_num=question_id-1)
        for i in range(len(answers)):
            is_true = True if i in right_positions else False # True/False
            #print(q, answers[i], is_true)
            Answer.objects.create(question=q, text=answers[i], right=is_true)
        
        #q = Question.objects.create(text=question_text)
        
        return render(request, 'frontend/questions.html', context={'question_id': question_id, 'test_id': test_id})
