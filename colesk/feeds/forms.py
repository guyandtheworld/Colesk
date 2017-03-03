from django import forms
from .models import Question, Answer

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['title']

class AnswerFrom(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['description']        