from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Account, Income, Expenditure
from .serializers import AccountSerializer, IncomeSerializer, ExpenditureSerializer

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
