from decimal import Decimal
from django.shortcuts import render
import requests

from accounts.models import Account, AccountType, ExpenditureCategory, Income, Expenditure, IncomeCategory
from django.utils import timezone
from datetime import timedelta,date
from django.db.models import Sum
from rest_framework.decorators import api_view, permission_classes
from django.db.models.functions import TruncMonth
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth.decorators import login_required

@login_required(login_url='/auth/')  

def dashboard(request):
    today = timezone.localdate()
    start_of_year = date(today.year, 1, 1)  # Start of the current year

    # Yearly income and expenses
    total_income = Income.objects.filter(date__gte=start_of_year).aggregate(total=Sum('amount')).get('total', Decimal('0.00'))
    total_expenses = Expenditure.objects.filter(date__gte=start_of_year).aggregate(total=Sum('amount')).get('total', Decimal('0.00'))

    # Monthly income and expenses
    monthly_income = (
        Income.objects
        .filter(date__gte=start_of_year)
        .annotate(month=TruncMonth('date'))  # Group by month
        .values('month')  # Select the month
        .annotate(total=Sum('amount'))  # Sum income for each month
        .order_by('month')  # Order by month
    )

    monthly_expenses = (
        Expenditure.objects
        .filter(date__gte=start_of_year)
        .annotate(month=TruncMonth('date'))  # Group by month
        .values('month')  # Select the month
        .annotate(total=Sum('amount'))  # Sum expenses for each month
        .order_by('month')  # Order by month
    )

    # Total counts
    total_accounts_types = AccountType.objects.count()
    total_accounts = Account.objects.count()

    # Overall income and expenditure
    overall_income = Income.objects.aggregate(total=Sum('amount'))['total'] or Decimal('0.00')
    overall_expenditure = Expenditure.objects.aggregate(total=Sum('amount'))['total'] or Decimal('0.00')

    # Account balances
    account_balances = Account.objects.annotate(
        total_income=Sum('incomes__amount', default=0),
        total_expenditure=Sum('expenditures__amount', default=0),
    ).values('name', 'total_income', 'total_expenditure')

    # Income breakdown by payment method
    income_by_payment_method = Income.objects.values('payment_method').annotate(total=Sum('amount'))

    # Expenditure breakdown by payment method
    expenditure_by_payment_method = Expenditure.objects.values('payment_method').annotate(total=Sum('amount'))

    # Category-wise income summary
    income_by_category = IncomeCategory.objects.annotate(total=Sum('incomes__amount')).values('name', 'total')

    # Category-wise expenditure summary
    expenditure_by_category = ExpenditureCategory.objects.annotate(total=Sum('expenditures__amount')).values('name', 'total')

    # Income and expenses grouped by account
    account_income = (
        Account.objects
        .annotate(total_income=Sum('incomes__amount', default=0))
        .values('name', 'total_income')
        .order_by('-total_income')  # Sort by highest income
    )

    account_expenses = (
        Account.objects
        .annotate(total_expenditure=Sum('expenditures__amount', default=0))
        .values('name', 'total_expenditure')
        .order_by('-total_expenditure')  # Sort by highest expenses
    )

    context = {
        "total_accounts_types": total_accounts_types,
        "total_expenses": total_expenses,
        "total_income": total_income,
        "total_accounts": total_accounts,
        "overall_income": overall_income,
        "overall_expenditure": overall_expenditure,
        "account_balances": list(account_balances),
        "income_by_payment_method": list(income_by_payment_method),
        "expenditure_by_payment_method": list(expenditure_by_payment_method),
        "income_by_category": list(income_by_category),
        "expenditure_by_category": list(expenditure_by_category),
        "monthly_income": list(monthly_income),  # Monthly income data
        "monthly_expenses": list(monthly_expenses),  # Monthly expenses data
        "account_income": list(account_income),  # Income grouped by account
        "account_expenses": list(account_expenses),  # Expenses grouped by account
    }

    return render(request, 'dashboard.html', context)

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


