from django import forms
from .models import Contact
from material import Layout, Row

class ContactForm(forms.ModelForm):
    class Meta:
        model= Contact 
        fields  = ['name','email','phone','location']

    layout = Layout(Row('name','email','phone','location'))