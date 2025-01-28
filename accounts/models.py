from django.db import models


# Account Model
class Account(models.Model):
    name = models.CharField(max_length=255, unique=True)  # Name of the ledger/account
    description = models.TextField(blank=True, null=True)  # Optional description
    opening_balance = models.DecimalField(
        max_digits=10, decimal_places=2, default=0.00
    )  # Initial balance
    handles_income = models.BooleanField(default=False)  # Handles incomes?
    handles_expenditure = models.BooleanField(default=False)  # Handles expenditures?

    def __str__(self):
        return self.name


# Income Category Model
class IncomeCategory(models.Model):
    account = models.ForeignKey(
        Account, on_delete=models.CASCADE, related_name="income_categories"
    )  # Each category is tied to an account
    name = models.CharField(max_length=255)  # Name of the income category
    description = models.TextField(blank=True, null=True)  # Optional description

    class Meta:
        unique_together = ("account", "name")  # Prevent duplicate categories within the same account

    def __str__(self):
        return f"{self.name} ({self.account.name})"


# Expenditure Category Model
class ExpenditureCategory(models.Model):
    account = models.ForeignKey(
        Account, on_delete=models.CASCADE, related_name="expenditure_categories"
    )  # Each category is tied to an account
    name = models.CharField(max_length=255)  # Name of the expenditure category
    description = models.TextField(blank=True, null=True)  # Optional description

    class Meta:
        unique_together = ("account", "name")  # Prevent duplicate categories within the same account

    def __str__(self):
        return f"{self.name} ({self.account.name})"


# Income Model
class Income(models.Model):
    account = models.ForeignKey(
        Account, on_delete=models.CASCADE, related_name="incomes"
    )  # Link to the associated account
    category = models.ForeignKey(
        IncomeCategory, on_delete=models.CASCADE, related_name="incomes"
    )  # Link to the income category
    amount = models.DecimalField(max_digits=10, decimal_places=2)  # Income amount
    date = models.DateField(auto_now_add=True)  # Date of income
    description = models.TextField(blank=True, null=True)  # Optional description

    def __str__(self):
        return f"{self.category.name} - {self.amount}"


# Expenditure Model
class Expenditure(models.Model):
    account = models.ForeignKey(
        Account, on_delete=models.CASCADE, related_name="expenditures"
    )  # Link to the associated account
    category = models.ForeignKey(
        ExpenditureCategory, on_delete=models.CASCADE, related_name="expenditures"
    )  # Link to the expenditure category
    amount = models.DecimalField(max_digits=10, decimal_places=2)  # Expenditure amount
    date = models.DateField(auto_now_add=True)  # Date of expenditure
    description = models.TextField(blank=True, null=True)  # Optional description

    def __str__(self):
        return f"{self.category.name} - {self.amount}"
