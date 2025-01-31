from rest_framework import serializers
from .models import Account, Expenditure, Income, IncomeCategory, ExpenditureCategory,AccountType


class AccountTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountType
        fields = "__all__"

class AccountSerializer(serializers.ModelSerializer):
    account_type = AccountTypeSerializer()

    class Meta:
        model = Account
        fields = "__all__"

class AccountReadSerializer(serializers.ModelSerializer):
    account_type = AccountTypeSerializer()

    class Meta:
        model = Account
        fields = "__all__"

class AccountWriteSerializer(serializers.ModelSerializer):
    account_type = serializers.PrimaryKeyRelatedField(queryset=AccountType.objects.all())

    class Meta:
        model = Account
        fields = "__all__"


class IncomeCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = IncomeCategory
        fields = "__all__"


class ExpenditureCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpenditureCategory
        fields = "__all__"


class IncomeSerializer(serializers.ModelSerializer):
    category = IncomeCategorySerializer()  # Nested category serializer

    class Meta:
        model = Income
        fields = "__all__"


class ExpenditureSerializer(serializers.ModelSerializer):
    category = ExpenditureCategorySerializer()  # Nested category serializer

    class Meta:
        model = Expenditure
        fields = "__all__"
