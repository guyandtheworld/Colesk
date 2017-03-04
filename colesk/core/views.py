from django.shortcuts import render, redirect

from colesk.feeds.views import feeds

def home(request):
    if request.user.is_authenticated:
        return feeds(request)
    else:
        return redirect('login')