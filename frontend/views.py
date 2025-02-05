from decimal import Decimal
from django.shortcuts import render
import requests

from accounts.models import Account, AccountType, Income, Expenditure
from django.utils import timezone
from datetime import timedelta
from django.db.models import Sum


def dashboard(request):
    today = timezone.localdate()   
    start_of_week = today - timedelta(days=today.weekday()) 

    total_income = Income.objects.filter(date__gte=start_of_week).aggregate(total=Sum('amount')).get('total', Decimal('0.00'))
    total_expenses = Expenditure.objects.filter(date__gte=start_of_week).aggregate(total=Sum('amount')).get('total', Decimal('0.00'))

    total_accounts_types = AccountType.objects.count()
    total_accounts = Account.objects.count()

    return render(request, "dashboard.html", {"total_accounts_types":total_accounts_types,"total_expenses":total_expenses,"total_income":total_income,"total_accounts":total_accounts})

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


