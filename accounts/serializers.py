from rest_framework import serializers
from .models import Account, Expenditure, Income, IncomeCategory, ExpenditureCategory,AccountType

from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data['email'],
            username=validated_data['username'],
            password=validated_data['password']
        )
        return user
    
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

    class Meta:
        model = Income
        fields = "__all__"


class ExpenditureSerializer(serializers.ModelSerializer):

    class Meta:
        model = Expenditure
        fields = "__all__"
