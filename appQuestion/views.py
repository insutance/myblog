from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Question

# Create your views here.
def question(request):
    questions = Question.objects
    return render(request, 'question.html', {'questions' : questions})

def read_question(request, question_id):
    read_questions = get_object_or_404(Question, pk = question_id)
    return render(request, 'read_question.html', {'read_questions' : read_questions})

def write_question(request):
    return render(request, 'write_question.html')

def create(request):
    question = Question()
    question.title = request.GET['title']
    question.description = request.GET['description']     #이거 왜 body로 해야되지 ..? 나는 description 으로 해놨는데 .. write_decriptrion에서 textarea의 name을 body로 해놔서 그랬음. 
    question.pub_date = timezone.datetime.now()
    question.save()
    return redirect('/question/' + str(question.id))