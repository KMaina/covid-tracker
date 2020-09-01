from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .models import User, Report, Patient, Doctor

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
        exclude = ["user"]

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        exclude = ["user"]

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        exclude = ["user"]

#class SignupForm(UserCreationForm):
#    email = forms.EmailField(max_length=200, help_text='Required')    
#        
#    def __init__(self, *args, **kwargs):
#        super(SignupForm, self).__init__(*args, **kwargs)
#
#        for fieldname in ['username', 'password1', 'password2']:
#            self.fields[fieldname].help_text = None