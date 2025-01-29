from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Account, AccountType, Income, Expenditure,IncomeCategory, ExpenditureCategory
from .serializers import AccountSerializer, AccountTypeSerializer, IncomeSerializer, ExpenditureSerializer, \
                        IncomeCategorySerializer, ExpenditureCategorySerializer

 
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
@api_view(['POST'])
def list_account_types(request): 
    account_types = AccountType.objects.all() 
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
@api_view(["POST"])
def create_account(request):
    serializer = AccountSerializer(data=request.data)
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
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Account.DoesNotExist:
        return Response({"error": "Account not found."}, status=status.HTTP_404_NOT_FOUND)

# Update Account
@api_view(["POST"])
def update_account(request):
    account_id = request.data.get("id")
    try:
        account = Account.objects.get(id=account_id)
        serializer = AccountSerializer(account, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Account.DoesNotExist:
        return Response({"error": "Account not found."}, status=status.HTTP_404_NOT_FOUND)

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

####### EXPENDTIURE #######
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
