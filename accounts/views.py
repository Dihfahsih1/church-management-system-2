from django.contrib.auth import logout
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Account, AccountType, Income, Expenditure,IncomeCategory, ExpenditureCategory,PAYMENT_METHODS
from .serializers import AccountReadSerializer, AccountSerializer, AccountTypeSerializer, AccountWriteSerializer, IncomeSerializer, ExpenditureSerializer, \
                        IncomeCategorySerializer, ExpenditureCategorySerializer

from django.contrib.auth import authenticate,login
from django.middleware.csrf import get_token
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User
from django.utils import timezone
from .serializers import UserSerializer 
from datetime import timedelta

from django.db.models import Sum
from django.utils.timezone import now, timedelta

def get_date_range(date_filter):
    """Determine the start and end date based on the date filter."""
    today = timezone.now().date()

    if date_filter == 'daily':
        start_date = end_date = today
    elif date_filter == 'weekly':
        start_date = today - timedelta(days=today.weekday())  # Monday of this week
        end_date = today
    elif date_filter == 'monthly':
        start_date = today.replace(day=1)  # First day of the month
        end_date = today
    elif date_filter == 'yearly':
        start_date = today.replace(month=1, day=1)  # First day of the year
        end_date = today
    else:
        return None, None  # Invalid filter

    return start_date, end_date

@api_view(['GET'])
def filter_income(request):
    """Filter income records based on date range."""
    date_filter = request.GET.get('date_filter', 'daily')  # Default to daily
    start_date, end_date = get_date_range(date_filter)

    if not start_date:
        return Response({"error": "Invalid date filter"}, status=400)

    incomes = Income.objects.filter(date__range=[start_date, end_date])
    serializer = IncomeSerializer(incomes, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def filter_expenditure(request):
    """Filter expenditure records based on date range."""
    date_filter = request.GET.get('date_filter', 'daily')
    start_date, end_date = get_date_range(date_filter)

    if not start_date:
        return Response({"error": "Invalid date filter"}, status=400)

    expenditures = Expenditure.objects.filter(date__range=[start_date, end_date])
    serializer = ExpenditureSerializer(expenditures, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def report_summary(request):
    filter_type = request.GET.get('filter', 'daily')   
    start_date, end_date = get_date_range(filter_type)

    if start_date is None:
        return Response({"error": "Invalid filter type"}, status=400)

    # Aggregate Income
    total_income = Income.objects.filter(date__range=[start_date, end_date]).aggregate(total=Sum('amount'))['total'] or 0.00
    
    # Aggregate Expenditure
    total_expenditure = Expenditure.objects.filter(date__range=[start_date, end_date]).aggregate(total=Sum('amount'))['total'] or 0.00
    
    return Response({
        "filter_type": filter_type,
        "start_date": start_date,
        "end_date": end_date,
        "total_income": total_income,
        "total_expenditure": total_expenditure,
        "net_balance": total_income - total_expenditure
    })

@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse({'message': 'User registered successfully'}, status=201)
    return JsonResponse(serializer.errors, status=400)

@api_view(['POST'])
@permission_classes([AllowAny])
def login_user(request):
    username = request.data.get('username')   
    password = request.data.get('password')

    user = authenticate(request, username=username, password=password)   
    if user is not None:
        login(request, user)  # This creates the session!

        refresh = RefreshToken.for_user(user)
        return JsonResponse({
            'access': str(refresh.access_token),
            'refresh': str(refresh),
            'csrf_token': get_token(request)   
        })

    return JsonResponse({'error': 'Invalid credentials'}, status=400)

from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib import messages
 
@permission_classes([IsAuthenticated])
def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out successfully.")
    return redirect('auth')   

######### INCOME CATEGORY ##########

# Create Income Category
@api_view(["POST"])
def create_income_category(request):
    serializer = IncomeCategorySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Retrieve Income Category
@api_view(["POST"])
def retrieve_income_category(request):
    category_id = request.data.get("id")
    try:
        category = IncomeCategory.objects.get(id=category_id)
        serializer = IncomeCategorySerializer(category)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except IncomeCategory.DoesNotExist:
        return Response({"error": "Income Category not found."}, status=status.HTTP_404_NOT_FOUND)


# List of income categories 
@api_view(['GET'])
def list_income_categories(request):
    # Fetch all categories and related account data using select_related to optimize query
    categories = IncomeCategory.objects.all().select_related('account').order_by('-id')

    # Manually structure the data to include the account name
    categories_data = []
    for category in categories:
        categories_data.append({
            'id': category.id,
            'name': category.name,
            'account_name': category.account.name if category.account else 'No account',  
            'account_id': category.account.id if category.account else 'No account', 
            'description': category.description
            
        })
    
    return Response(categories_data)
# Update Income Category
@api_view(["POST"])
def update_income_category(request):
    category_id = request.data.get("id")
    try:
        category = IncomeCategory.objects.get(id=category_id)
        serializer = IncomeCategorySerializer(category, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except IncomeCategory.DoesNotExist:
        return Response({"error": "Income Category not found."}, status=status.HTTP_404_NOT_FOUND)

# Delete Income Category
@api_view(["POST"])
def delete_income_category(request):
    category_id = request.data.get("id")
    try:
        category = IncomeCategory.objects.get(id=category_id)
        category.delete()
        return Response({"message": "Income Category deleted successfully."}, status=status.HTTP_200_OK)
    except IncomeCategory.DoesNotExist:
        return Response({"error": "Income Category not found."}, status=status.HTTP_404_NOT_FOUND)


######### EXPENDITURE CATEGORY ##########

# Create Expenditure Category
@api_view(["POST"])
def create_expenditure_category(request):
    serializer = ExpenditureCategorySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# List of Expenditure categories 
@api_view(['GET'])
def list_expenditure_categories(request):
    # Fetch all categories and related account data using select_related to optimize query
    categories = ExpenditureCategory.objects.all().select_related('account').order_by('-id')

    # Manually structure the data to include the account name
    categories_data = []
    for category in categories:
        categories_data.append({
            'id': category.id,
            'name': category.name,
            'account_name': category.account.name if category.account else 'No account',  
            'account_id': category.account.id if category.account else 'No account',  
            'description': category.description
        })
    
    return Response(categories_data)

# Retrieve Expenditure Category
@api_view(["POST"])
def retrieve_expenditure_category(request):
    category_id = request.data.get("id")
    try:
        category = ExpenditureCategory.objects.get(id=category_id)
        serializer = ExpenditureCategorySerializer(category)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except ExpenditureCategory.DoesNotExist:
        return Response({"error": "Expenditure Category not found."}, status=status.HTTP_404_NOT_FOUND)

# Update Expenditure Category
@api_view(["POST"])
def update_expenditure_category(request):
    category_id = request.data.get("id")
    try:
        category = ExpenditureCategory.objects.get(id=category_id)
        serializer = ExpenditureCategorySerializer(category, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except ExpenditureCategory.DoesNotExist:
        return Response({"error": "Expenditure Category not found."}, status=status.HTTP_404_NOT_FOUND)

# Delete Expenditure Category
@api_view(["POST"])
def delete_expenditure_category(request):
    category_id = request.data.get("id")
    try:
        category = ExpenditureCategory.objects.get(id=category_id)
        category.delete()
        return Response({"message": "Expenditure Category deleted successfully."}, status=status.HTTP_200_OK)
    except ExpenditureCategory.DoesNotExist:
        return Response({"error": "Expenditure Category not found."}, status=status.HTTP_404_NOT_FOUND)

#########  ACCOUNT TYPES  ##########
@api_view(["POST"])
def create_account_type(request):
    if request.method == 'POST':
        # Check if the request contains a list of account types
        if isinstance(request.data, list):
            # Serialize the list of account types
            serializer = AccountTypeSerializer(data=request.data, many=True)
            if serializer.is_valid():
                serializer.save()  # Save multiple account types at once
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        # If it's a single account type (not a list)
        serializer = AccountTypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # Save single account type
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#List of account types
@api_view(['GET'])
def list_account_types(request): 
    account_types = AccountType.objects.all().order_by('-id')
    serializer = AccountTypeSerializer(account_types, many=True) 
    return Response(serializer.data, status=status.HTTP_200_OK)

# Retrieve Account Type
@api_view(["POST"])
def retrieve_account_type(request):
    account_id = request.data.get("id")
    try:
        account = AccountType.objects.get(id=account_id)
        serializer = AccountTypeSerializer(account)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except AccountType.DoesNotExist:
        return Response({"error": "Account not found."}, status=status.HTTP_404_NOT_FOUND)

# Update Accounttype
@api_view(["POST"])
def update_account_type(request):
    account_id = request.data.get("id")
    try:
        account = AccountType.objects.get(id=account_id)
        serializer = AccountTypeSerializer(account, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except AccountType.DoesNotExist:
        return Response({"error": "Account not found."}, status=status.HTTP_404_NOT_FOUND)

# Delete Account Type
@api_view(["POST"])
def delete_account_type(request):
    account_id = request.data.get("id")
    try:
        account = AccountType.objects.get(id=account_id)
        account.delete()
        return Response({"message": "Account Type deleted successfully."}, status=status.HTTP_200_OK)
    except AccountType.DoesNotExist:
        return Response({"error": "Account not found."}, status=status.HTTP_404_NOT_FOUND)


#########  ACCOUNTS  ##########
@api_view(['GET', 'POST'])
def list_or_create_accounts(request): 
    if request.method == 'GET':
        accounts = Account.objects.all().order_by('-id')
        serializer = AccountReadSerializer(accounts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'POST':
        serializer = AccountWriteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Retrieve Account
@api_view(["POST"])
def retrieve_account(request):
    account_id = request.data.get("id")
    try:
        account = Account.objects.get(id=account_id)
        serializer = AccountSerializer(account)
        return Response(serializer.data)
    except Account.DoesNotExist:
        return Response({"error": "Account not found."}, status=status.HTTP_404_NOT_FOUND)

@api_view(["POST"])
def update_account(request):
    account_id = request.data.get("id")   
    
    if not account_id:
        return Response({"error": "Account ID is required."}, status=status.HTTP_400_BAD_REQUEST)
    
    try:
        account = Account.objects.get(id=account_id)
        serializer = AccountSerializer(account, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Account updated successfully.", "data": serializer.data}, status=status.HTTP_200_OK)

        return Response({"error": "Invalid data.", "details": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    except Account.DoesNotExist:
        return Response({"error": "Account not found."}, status=status.HTTP_404_NOT_FOUND)

    except Exception as e:
        return Response({"error": "An unexpected error occurred.", "details": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# Delete Account
@api_view(["POST"])
def delete_account(request):
    account_id = request.data.get("id")
    try:
        account = Account.objects.get(id=account_id)
        account.delete()
        return Response({"message": "Account deleted successfully."}, status=status.HTTP_200_OK)
    except Account.DoesNotExist:
        return Response({"error": "Account not found."}, status=status.HTTP_404_NOT_FOUND)



######### INCOMES ##########

# Create Income
@api_view(["POST"])
def create_income(request):
    serializer = IncomeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# List of income categories 
@api_view(['GET'])
def list_incomes(request):
    incomes = Income.objects.all().select_related('category').order_by('-id')

    # Manually structure the data to include the income name
    incomes_data = []
    for income in incomes:
        incomes_data.append({
            'id': income.id,
            'date':income.date,
            'account_id': income.account_id,
            'category_id': income.category_id,
            'payment_methods':income.payment_method,
            'account_name': income.account.name if income.account else 'No account',  # Handle missing account
            'category_name': income.category.name if income.category else 'No category',
            'amount': income.amount if income.amount else 0,
            'description': income.description
        })
    
    return Response(incomes_data)

# Retrieve Income
@api_view(["POST"])
def retrieve_income(request):
    income_id = request.data.get("id")
    try:
        income = Income.objects.get(id=income_id)
        serializer = IncomeSerializer(income)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Income.DoesNotExist:
        return Response({"error": "Income not found."}, status=status.HTTP_404_NOT_FOUND)

# Update Income
@api_view(["POST"])
def update_income(request):
    income_id = request.data.get("id")
    try:
        income = Income.objects.get(id=income_id)
        serializer = IncomeSerializer(income, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Income.DoesNotExist:
        return Response({"error": "Income not found."}, status=status.HTTP_404_NOT_FOUND)

# Delete Income
@api_view(["POST"])
def delete_income(request):
    income_id = request.data.get("id")
    try:
        income = Income.objects.get(id=income_id)
        income.delete()
        return Response({"message": "Income deleted successfully."}, status=status.HTTP_200_OK)
    except Income.DoesNotExist:
        return Response({"error": "Income not found."}, status=status.HTTP_404_NOT_FOUND)

####### EXPENDITURE #######
@api_view(["POST"])
def create_expenditure(request):
    """
    Create a new Expenditure entry.
    """
    serializer = ExpenditureSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# List of income categories 
@api_view(['GET'])
def list_expenditure(request):
    expenditures = Expenditure.objects.all().select_related('category').order_by('-id')

    # Manually structure the data to include the expenditure name
    expenditure_data = []
    for expenditure in expenditures:
        expenditure_data.append({
            'id': expenditure.id,
            'date':expenditure.date,
            'account_id': expenditure.account_id,
            'category_id': expenditure.category_id,
            'account_name': expenditure.account.name if expenditure.account else 'No account',  # Handle missing account
            'category_name': expenditure.category.name if expenditure.category else 'No category',
            'amount': expenditure.amount if expenditure.amount else 0,
            'payment_methods':expenditure.payment_method,
            'description': expenditure.description
        })
    
    return Response(expenditure_data)


@api_view(["POST"])
def retrieve_expenditure(request):
    """
    Retrieve an Expenditure entry by ID (provided in the request body).
    """
    expenditure_id = request.data.get("id")
    if not expenditure_id:
        return Response({"error": "ID is required"}, status=status.HTTP_400_BAD_REQUEST)
    try:
        expenditure = Expenditure.objects.get(pk=expenditure_id)
        serializer = ExpenditureSerializer(expenditure)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Expenditure.DoesNotExist:
        return Response({"error": "Expenditure not found"}, status=status.HTTP_404_NOT_FOUND)


@api_view(["POST"])
def update_expenditure(request):
    """
    Update an existing Expenditure entry (ID provided in the request body).
    """
    expenditure_id = request.data.get("id")
    if not expenditure_id:
        return Response({"error": "ID is required"}, status=status.HTTP_400_BAD_REQUEST)
    try:
        expenditure = Expenditure.objects.get(pk=expenditure_id)
        serializer = ExpenditureSerializer(expenditure, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Expenditure.DoesNotExist:
        return Response({"error": "Expenditure not found"}, status=status.HTTP_404_NOT_FOUND)


@api_view(["POST"])
def delete_expenditure(request):
    """
    Delete an Expenditure entry (ID provided in the request body).
    """
    expenditure_id = request.data.get("id")
    if not expenditure_id:
        return Response({"error": "ID is required"}, status=status.HTTP_400_BAD_REQUEST)
    try:
        expenditure = Expenditure.objects.get(pk=expenditure_id)
        expenditure.delete()
        return Response({"message": "Expenditure deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
    except Expenditure.DoesNotExist:
        return Response({"error": "Expenditure not found"}, status=status.HTTP_404_NOT_FOUND)


def get_payment_methods(request):
    return JsonResponse({'payment_methods': dict(PAYMENT_METHODS)})


def get_date_range(start_date=None, end_date=None):
    """Determine the start and end date based on the user's input or default to monthly."""
    today = timezone.now().date()

    if start_date and end_date:
        return start_date, end_date  # User-provided date range

    # Default to monthly view
    start_date = today.replace(day=1)  # First day of the current month
    end_date = today  # Today's date

    return start_date, end_date

@api_view(['GET'])
def balance_sheet(request):
    """Generate balance sheet report for income and expenditures aggregated by account."""
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    # Convert string dates to date objects
    if start_date and end_date:
        start_date = timezone.datetime.strptime(start_date, "%Y-%m-%d").date()
        end_date = timezone.datetime.strptime(end_date, "%Y-%m-%d").date()

    start_date, end_date = get_date_range(start_date, end_date)

    # Aggregate income and expenditures by account
    income_aggregation = Income.objects.filter(date__range=[start_date, end_date])\
        .values("account__name")\
        .annotate(total_income=Sum('amount'))

    expenditure_aggregation = Expenditure.objects.filter(date__range=[start_date, end_date])\
        .values("account__name")\
        .annotate(total_expenditure=Sum('amount'))

    # Merging the aggregated results into a single structure
    account_data = {}

    for income in income_aggregation:
        account_name = income["account__name"] or "Uncategorized"
        account_data[account_name] = {
            "account": account_name,
            "total_income": income["total_income"] or 0,
            "total_expenditure": 0
        }

    for expenditure in expenditure_aggregation:
        account_name = expenditure["account__name"] or "Uncategorized"
        if account_name in account_data:
            account_data[account_name]["total_expenditure"] = expenditure["total_expenditure"] or 0
        else:
            account_data[account_name] = {
                "account": account_name,
                "total_income": 0,
                "total_expenditure": expenditure["total_expenditure"] or 0
            }

    # Convert dictionary to list
    balance_sheet_data = list(account_data.values())

    # Calculate total income, total expenditure, and balance
    total_income = sum(item["total_income"] for item in balance_sheet_data)
    total_expenditure = sum(item["total_expenditure"] for item in balance_sheet_data)
    balance = total_income - total_expenditure

    # Fetch full records for serialization
    incomes = Income.objects.filter(date__range=[start_date, end_date])
    expenditures = Expenditure.objects.filter(date__range=[start_date, end_date])

    income_serializer = IncomeSerializer(incomes, many=True)
    expenditure_serializer = ExpenditureSerializer(expenditures, many=True)

    return Response({
        "start_date": start_date,
        "end_date": end_date,
        "total_income": total_income,
        "total_expenditure": total_expenditure,
        "balance": balance,
        "accounts": balance_sheet_data,  # Aggregated per account
        "income_details": income_serializer.data,
        "expenditure_details": expenditure_serializer.data
    })