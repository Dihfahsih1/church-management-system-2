from django.db import models
from django.utils import timezone

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
 

class UserManager(BaseUserManager):
    def create_user(self, email, username, password=None, **extra_fields):
        if not email:
            raise ValueError("Email is required")
        if not username:
            raise ValueError("Username is required")
        
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, username, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150, unique=True)   
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'username'  
    REQUIRED_FIELDS = ['email'] 

    def __str__(self):
        return self.email


class AccountType(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(null=True, blank=True)
    date = models.DateField(null=True, blank=True) 

    def __str__(self):
        return self.name
    
# Account Model
class Account(models.Model):
    name = models.CharField(max_length=255, unique=True)   
    account_type = models.ForeignKey(AccountType, related_name='accounts', on_delete=models.SET_NULL, blank=True, null=True)
    description = models.TextField(blank=True, null=True)   
    opening_balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)   
    date = models.DateField(null=True, blank=True) 
    def __str__(self):
        return self.name

# Income Category Model
class IncomeCategory(models.Model):
    account = models.ForeignKey(Account, on_delete=models.SET_NULL, related_name="income_categories",blank=True, null=True)  
    name = models.CharField(max_length=255)   
    description = models.TextField(blank=True, null=True)
    date = models.DateField(null=True, blank=True) 
    
    class Meta:
        unique_together = ("account", "name")
    
    def __str__(self):
        return f"{self.name} ({self.account.name})"

# Expenditure Category Model
class ExpenditureCategory(models.Model):
    account = models.ForeignKey(Account, on_delete=models.SET_NULL, related_name="expenditure_categories",  blank=True, null=True)   
    name = models.CharField(max_length=255)   
    description = models.TextField(blank=True, null=True)
    date = models.DateField(null=True, blank=True) 
    
    class Meta:
        unique_together = ("account", "name")
    
    def __str__(self):
        return f"{self.name} ({self.account.name})"

# Income Model
class Income(models.Model):
    account = models.ForeignKey(Account, on_delete=models.SET_NULL, related_name="incomes",  blank=True, null=True)  
    category = models.ForeignKey(IncomeCategory, on_delete=models.SET_NULL, related_name="incomes",  blank=True, null=True)  
    amount = models.DecimalField(max_digits=10, decimal_places=2) 
    date = models.DateField(null=True, blank=True)  
    description = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.category.name} - {self.amount}"

# Expenditure Model
class Expenditure(models.Model):
    account = models.ForeignKey(Account, on_delete=models.SET_NULL, related_name="expenditures",  blank=True, null=True) 
    category = models.ForeignKey(ExpenditureCategory, on_delete=models.SET_NULL, related_name="expenditures",  blank=True, null=True)  
    amount = models.DecimalField(max_digits=10, decimal_places=2)  
    date = models.DateField(null=True, blank=True)  
    description = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.category.name} - {self.amount}"
