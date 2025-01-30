from django.shortcuts import render
import requests

def dashboard(request):
    api_url = "http://127.0.0.1:8000/api/accountstypes/list/"
    response = requests.get(api_url)
    
    if response.status_code == 200:
        accounts = response.json()
        account_count = len(accounts)  # Count the number of account types
    else:
        accounts = []
        account_count = 0

    return render(request, "dashboard.html", {"accounts": accounts, "account_count": account_count})

def create_account_type_form(request):
    return render(request, "Accounts/create_account_type.html")