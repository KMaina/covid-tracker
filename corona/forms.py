from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .models import User, Profile, Report

class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile        
        exclude=["user"]        

class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        exclude=["user"]        
