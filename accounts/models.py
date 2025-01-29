from django.db import models

# Account Model
class Account(models.Model):
    name = models.CharField(max_length=255, unique=True)   
    description = models.TextField(blank=True, null=True)   
    opening_balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)   
    handles_income = models.BooleanField(default=False)  
    handles_expenditure = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name

# Income Category Model
class IncomeCategory(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="income_categories")  
    name = models.CharField(max_length=255)   
    description = models.TextField(blank=True, null=True)
    
    class Meta:
        unique_together = ("account", "name")
    
    def __str__(self):
        return f"{self.name} ({self.account.name})"

# Expenditure Category Model
class ExpenditureCategory(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="expenditure_categories")   
    name = models.CharField(max_length=255)   
    description = models.TextField(blank=True, null=True)
    
    class Meta:
        unique_together = ("account", "name")
    
    def __str__(self):
        return f"{self.name} ({self.account.name})"

# Income Model
class Income(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="incomes")  
    category = models.ForeignKey(IncomeCategory, on_delete=models.CASCADE, related_name="incomes")  
    amount = models.DecimalField(max_digits=10, decimal_places=2) 
    date = models.DateField(auto_now_add=True)  
    description = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.category.name} - {self.amount}"

# Expenditure Model
class Expenditure(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="expenditures")  
    category = models.ForeignKey(ExpenditureCategory, on_delete=models.CASCADE, related_name="expenditures")  
    amount = models.DecimalField(max_digits=10, decimal_places=2)  
    date = models.DateField(auto_now_add=True)  
    description = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.category.name} - {self.amount}"
