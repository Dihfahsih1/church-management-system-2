from django.shortcuts import render
import requests

def dashboard(request):
    api_url = "http://127.0.0.1:8000/api/accounts/" 
    response = requests.get(api_url)
    accounts = response.json() if response.status_code == 200 else []

    return render(request, "dashboard.html", {"accounts": accounts})
