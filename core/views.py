from django.shortcuts import render, get_object_or_404
from .models import Post
from django.utils import timezone

def main_page(request):
	posts = Post.objects.all()
	return render(request, 'core/main_post.html', {'posts' : posts[::-1]}) #Displaying Post On Main Page

def post_detail(request, pk):
	post = get_object_or_404(Post, pk=pk)
	return render(request, 'core/post_detail.html', {'post' : post})

def networks(request):
	return render(request, 'core/networks.html', {})

def profile(request):
	return render(request, 'core/profile.html', {})		

def my_feed(request):
	return render(request, 'core/my_feed.html', {})	