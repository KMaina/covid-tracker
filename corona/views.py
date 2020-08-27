from django.shortcuts import render
import requests

# Create your views here.
def home(request):
    cov_response = requests.get('https://api.thevirustracker.com/free-api?countryTotals=ALL')
    cov_data = cov_response.json()
    ref_data = cov_data['countryitems']
    
    return render(request, 'covid/home.html', {"cov_data": ref_data})

def index_test(request):
    title = "Covid Index Bootstrap Test"

    return render(request, 'index.html', {"title": title})
