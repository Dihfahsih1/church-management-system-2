from rest_framework import serializers
from .models import Account, Expenditure, Income, IncomeCategory, ExpenditureCategory

class AccountSerializer(serializers.ModelSerializer):
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
