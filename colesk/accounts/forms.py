from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class LoginForm(forms.ModelForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=True)
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        required=True)

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs) 

    def clean(self):
        super(LoginForm, self).clean()
        return self.cleaned_data

class SignUpForm(forms.ModelForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        max_length=30,
        required=True)
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.CharField(
        widget=forms.EmailInput(attrs={'class': 'form-control'}),
        max_length=75,
        required=True)

    class Meta:
        model = User
        exclude = ['last_login', 'date_joined']
        fields = ['username', 'password', 'email']

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs) 

    def clean(self):
        super(SignUpForm, self).clean()
        return self.cleaned_data