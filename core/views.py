from django.shortcuts import render, get_object_or_404
from .models import Post
from django.utils import timezone

def main_page(request):
	posts  = Post.objects.all().order_by('published_date')
	return render(request, 'core/main.html', {'posts' : posts})

def home(request):
	return render(request, 'core/home.html', {})

def you(request):
	return render(request, 'core/profile.html', {})		