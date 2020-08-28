from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import SignupForm

# Create your views here.
def home(request):
    pass

def index_test(request):
    title = "Covid Index Bootstrap Test"

    return render(request, 'index.html', {"title": title})

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
        return redirect ('index')
    else:
        form = SignupForm()
    return render( request, 'registration/registration_form.html', {'form': form} )
