from django.db import models

from django.db import models

# Account Model
class Account(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)
    handles_income = models.BooleanField(default=False)  # Can this account handle incomes?
    handles_expenditure = models.BooleanField(default=False)  # Can this account handle expenditures?

    def __str__(self):
        return self.name


# Income Model
class Income(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="incomes")
    category = models.CharField(max_length=255)  # E.g., "Tithe", "Thanksgiving Offering"
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(auto_now_add=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.category} - {self.amount}"


# Expenditure Model
class Expenditure(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="expenditures")
    category = models.CharField(max_length=255)  # E.g., "Fuel", "Salaries"
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(auto_now_add=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.category} - {self.amount}"

