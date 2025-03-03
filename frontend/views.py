from decimal import Decimal
from django.shortcuts import render
import requests

from accounts.models import Account, AccountType, Income, Expenditure
from django.utils import timezone
from datetime import timedelta
from django.db.models import Sum
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth.decorators import login_required

@login_required(login_url='/auth/') 
def dashboard(request):
    today = timezone.localdate()   
    start_of_week = today - timedelta(days=today.weekday()) 

    total_income = Income.objects.filter(date__gte=start_of_week).aggregate(total=Sum('amount')).get('total', Decimal('0.00'))
    total_expenses = Expenditure.objects.filter(date__gte=start_of_week).aggregate(total=Sum('amount')).get('total', Decimal('0.00'))

    total_accounts_types = AccountType.objects.count()
    total_accounts = Account.objects.count() 
    return render(request, "dashboard.html", {"total_accounts_types":total_accounts_types,"total_expenses":total_expenses,
                                              "total_income":total_income,"total_accounts":total_accounts
                                            })
@login_required(login_url='/auth/') 
def create_account_type_form(request):
    return render(request, "Accounts/create_account_type.html")

@login_required(login_url='/auth/') 
def create_account_form(request):
    return render(request, "Accounts/create_account_form.html")

@login_required(login_url='/auth/') 
def create_income_category_form(request):
    return render(request, "Categories/create_income_category_form.html")

@login_required(login_url='/auth/') 
def create_expenditure_category_form(request):
    return render(request, "Categories/create_expenditure_category_form.html")

@login_required(login_url='/auth/') 
def add_expenditure_form(request):
    return render(request, "Expenditure/add_expenditure_form.html")

@login_required(login_url='/auth/') 
def add_income_form(request):
    return render(request, "Incomes/add_income_form.html")

def auth_view(request):
    return render(request, 'auth.html')

def generate_balance_sheet(request):
    return render(request,'balance_sheet.html')


