from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .models import User, Report, Patient, Doctor, Contact
from material import Layout, Row

class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200)

    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None
                        
    class Meta:
        model = User
        fields = ('username', 'username', 'password1', 'password2')
        

class LoginForm(AuthenticationForm):    
    class Meta:
        model = User
        fields = ['username', 'password']        

class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        exclude = ["user","doctor","post_date"]

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
        exclude  = ["user"]
    
