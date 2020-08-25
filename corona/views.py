from django.shortcuts import render

# Create your views here.
def home(request):
    pass

def index_test(request):
    title = "Covid Index Bootstrap Test"

    return render(request, 'index.html', {"title": title})
