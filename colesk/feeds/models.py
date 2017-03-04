from django.contrib.auth.models import User
from django.db import models 

class Tag(models.Model):
    word = models.CharField(max_length=255)

class Question(models.Model):
    user = models.ForeignKey(User)
    title = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Answer(models.Model):
    user = models.ForeignKey(User)
    question = models.ForeignKey(Question)
    description = models.TextField(max_length=1000)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.description[:20]