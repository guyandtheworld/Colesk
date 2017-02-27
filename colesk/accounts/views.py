from django.contrib.auth import authenticate, login as user_login, logout as user_logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from colesk.accounts.forms import SignUpForm

def login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                user_login(request, user)
                return redirect('/')
            else:
                return redirect('/login')    
        else:
            return render(request, 'core/cover.html')    
    else:
        return redirect('/')    

def logout(request):
    user_logout(request)
    return redirect('/')

def signup(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = SignUpForm(request.POST)
            if not form.is_valid():
                return render(request, 'accounts/signup.html',
                                {'form' : form})
            else:
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                email = form.cleaned_data.get('email')
                User.objects.create_user(username=username, email=email,
                                            password=password)
                user = authenticate(username=username, password=password)
                print(user)
                user_login(request, user)
                return redirect('/')
        else:
            form = SignUpForm()
            return render(request, 'accounts/signup.html',
                            {'form' : form})
    else:
        return redirect('/')