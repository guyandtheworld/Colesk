from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from colesk.feeds.models import Question, Answer
from colesk.feeds.forms import QuestionForm, AnswerForm


@login_required
def feeds(request):
    questions = Question.objects.all()
    return render(request, 'feeds/feeds.html',
                     {'questions': questions})

@login_required
def question_detail(request, pk):
    answers = {}
    question = Question.objects.filter(pk=pk)[0]
    answers = Answer.objects.filter(question=question.pk)
    return render(request, 'feeds/question_detail.html',
                    {'question': question,
                     'answers': answers})

@login_required
def new_question(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = Question()
            print(form)
            question.title = form.cleaned_data.get('title')
            question.user_id = request.user.id
            question.save()
            return redirect('/')
        else:
            return render(request, 'feeds/new_post.html', {'form': form})
    else:   
        form = QuestionForm()
        return render(request, 'feeds/new_post.html',
                     {'form': form,})