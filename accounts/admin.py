from django.contrib import admin
from .models import User, AccountType, Account, IncomeCategory, ExpenditureCategory, Income, Expenditure

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'username', 'is_active', 'is_staff')
    search_fields = ('email', 'username')
    list_filter = ('is_active', 'is_staff')

@admin.register(AccountType)
class AccountTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'date')
    search_fields = ('name',)
    list_filter = ('date',)

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('name', 'account_type', 'opening_balance', 'date')
    search_fields = ('name',)
    list_filter = ('account_type', 'date')

@admin.register(IncomeCategory)
class IncomeCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'account', 'date')
    search_fields = ('name', 'account__name')
    list_filter = ('date',)

@admin.register(ExpenditureCategory)
class ExpenditureCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'account', 'date')
    search_fields = ('name', 'account__name')
    list_filter = ('date',)

@admin.register(Income)
class IncomeAdmin(admin.ModelAdmin):
    list_display = ('category', 'account', 'amount', 'date')
    search_fields = ('category__name', 'account__name')
    list_filter = ('date',)

@admin.register(Expenditure)
class ExpenditureAdmin(admin.ModelAdmin):
    list_display = ('category', 'account', 'amount', 'date')
    search_fields = ('category__name', 'account__name')
    list_filter = ('date',)
