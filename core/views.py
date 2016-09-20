from django.shortcuts import render, get_object_or_404
from .models import Post
from django.utils import timezone

def main_page(request):
	posts = Post.objects.filter(published_date__lte = timezone.now())
	return render(request, 'core/main_post.html', {'posts' : posts}) #Displaying Post On Main Page

def post_detail(request, pk=None):
	post = get_object_or_404(Post, pk=pk)
	return render(request, 'core/p_detail.html', {'post' : post})

def home(request):
	return render(request, 'core/home.html', {})

def you(request):
	return render(request, 'core/profile.html', {})		