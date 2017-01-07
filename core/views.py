from django.shortcuts import render,redirect, get_object_or_404
from .models import Post
from django.utils import timezone
from .forms import PostForm, UserForm, UserProfileForm, DocumentForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
import os

def main_page(request):
	posts = Post.objects.all()
	return render(request, 'core/main_post.html', {'posts' : posts[::-1]}) #Displaying Post On Main Page

def post_detail(request, pk):
	post = get_object_or_404(Post, pk=pk)
	return render(request, 'core/post_detail.html', {'post' : post})

def post_edit(request, pk):
	post = get_object_or_404(Post, pk=pk)
	if request.method == 'POST':
		form = PostForm(request.POST, instance = post)
		if form.is_valid():
			post = form.save(commit = False)
			post.author = request.user
			post.published_date = timezone.now()
			post.save()
			return redirect('post_detail', pk = post.pk)
	else:
		form = PostForm(instance = post)
		return render(request, 'core/post_edit.html', {'form' : form})	

def new_post(request):
	if request.method == 'POST':
		form = PostForm(request.POST, request.FILES)
		if form.is_valid():
			post = form.save(commit = False)
			post.docfile.save(content = request.FILES["docfile"],save=False)
			post.author = request.user
			post.published_date = timezone.now()
			post.save()
			return redirect('post_detail', pk = post.pk)
	else:
		form = PostForm()
	return render(request, 'core/post_edit.html', {'form' : form})