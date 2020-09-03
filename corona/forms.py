from django import forms
from material import Layout, Row
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .models import User, Report, Patient, Doctor, Contact

class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']

class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        exclude = ["user"]

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        exclude = ["user","post_date"]

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        exclude = ["user","post_date"]
        
class ContactForm(forms.ModelForm):
    class Meta:
        model= Contact 
        fields  = ['name','email','phone','location']
    
