from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from colesk.feeds.models import Question, Answer
from colesk.feeds.forms import QuestionForm, AnswerForm


@login_required
def feeds(request):
    questions = Question.objects.all()
    print("@#$%^&&*",request.user.id)
    return render(request, 'feeds/feeds.html',
                     {'questions': questions})

@login_required
def question(request, title):
    answers = {}
    question = Question.objects.filter(title=title)[0]
    answers = Answer.objects.filter(question=question.pk)
    print(answers)
    return render(request, 'feeds/question_detail.html',
                    {'question': question,
                     'answers': answers})

@login_required
def new(request):
    if request.method == 'POST':
        pass
    else:
        form = QuestionForm()
        return render(request, )