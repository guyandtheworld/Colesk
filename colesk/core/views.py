from django.shortcuts import render, redirect
from django.http import HttpResponse

def home(request):
    if request.user.is_authenticated:
        return HttpResponse("<h1>Home</h1>")
    else:
        return redirect('login')