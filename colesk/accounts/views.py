from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from colesk.accounts.forms import SignUpForm

def signup(request):
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
            login(request, user)
            return redirect('/')
    else:
        form = SignUpForm()
        return render(request, 'accounts/signup.html',
                        {'form' : form})
