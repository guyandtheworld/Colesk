from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
#from colesk.actions.models import actions

class Feed(models.Model):
	user = models.ForeignKey(User)
	date = models.DateTimeField(auto_now_add = True)
	post = models.TextField(max_length = 300)
	parent = models.ForeignKey('Feed', null = True, blank = True)
	likes = models.IntegerField(default = 0)
	comments = models.IntegerField(default = 0)