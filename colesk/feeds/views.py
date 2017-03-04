from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from colesk.feeds.models import Question, Answer
from colesk.feeds.forms import QuestionForm, AnswerForm


@login_required
def feeds(request):
    questions = Question.objects.all()
    print(questions)
    return render(request, 'feeds/feeds.html',
                     {'questions': questions})

@login_required
def question(request):
    pass
