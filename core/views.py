from django.shortcuts import render,redirect, get_object_or_404
from .models import Post
from django.utils import timezone
from .forms import PostForm

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

def new_post(request):
	if request.method == 'POST':
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit = False)
			post.author = request.user
			post.published_date = timezone.now()
			post.save()
			return redirect('post_detail', pk = post.pk)
	else:
		form = PostForm()
	return render(request, 'core/post_edit.html', {'form' : form})

def login(request):
	return render(request, 'core/login.html', {})	

def sign_up(request):
	return render(request, 'core/sign_up.html',{})	