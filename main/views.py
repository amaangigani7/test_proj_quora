from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
# Create your views here.

def home(request):
    questions = Question.objects.all()
    return render(request, 'main/home.html', {'questions': questions})

def question_detail(request, pk):
    question = Question.objects.get(pk=pk)
    form = AnswerForm()
    return render(request, 'main/question_detail.html', {'question': question, 'form': form})

@login_required
def add_question(request):
    if request.method == 'GET':
        form = QuestionForm()
        return render(request, 'main/add_question.html', {'form': form})
    elif request.method == 'POST':
        data = request.POST
        question = Question.objects.create(user=request.user, title=data['title'], content=data['content'])
        return redirect('question_detail', pk=question.pk)

@login_required
def add_answer(request, pk):
    data = request.POST
    Answer.objects.create(question=Question.objects.get(pk=pk), user=request.user, content=data['content'])
    question = Question.objects.get(pk=pk)
    return redirect('question_detail', pk=pk)

@login_required
def add_like(request, pk):
    question = Question.objects.get(pk=pk)
    like_map = LikeMap.objects.filter(question=question, user=request.user)
    if not like_map:
        question.likes += 1
        LikeMap.objects.create(question=question, user=request.user)
    else:
        question.likes -= 1
        like_map[0].delete()
    question.save()
    return redirect('question_detail', pk=pk)
