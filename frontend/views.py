from django.shortcuts import render
import requests

from accounts.models import Account, Income
from django.utils import timezone
from datetime import timedelta
from django.db.models import Sum

def dashboard(request):
    today = timezone.now().date()
    start_of_week = today - timedelta(days=today.weekday())
    total_income = Income.objects.filter(date__gte=start_of_week).aggregate(total=Sum('amount'))
    api_url = "http://127.0.0.1:8000/api/accountstypes/list/"
    total_accounts = Account.objects.count()
    response = requests.get(api_url)
    
    if response.status_code == 200:
        accounts = response.json()
        account_count = len(accounts)  # Count the number of account types
    else:
        accounts = []
        account_count = 0

    return render(request, "dashboard.html", {"total_income":total_income,"total_accounts":total_accounts,"accounts": accounts, "account_count": account_count})

def create_account_type_form(request):
    return render(request, "Accounts/create_account_type.html")

def create_account_form(request):
    return render(request, "Accounts/create_account_form.html")

def create_income_category_form(request):
    return render(request, "Categories/create_income_category_form.html")

def create_expenditure_category_form(request):
    return render(request, "Categories/create_expenditure_category_form.html")

def add_expenditure_form(request):
    return render(request, "Expenditure/add_expenditure_form.html")

def add_income_form(request):
    return render(request, "Incomes/add_income_form.html")


