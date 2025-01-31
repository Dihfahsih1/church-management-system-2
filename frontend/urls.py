from django.urls import path
from .views import create_expenditure_category_form, create_income_category_form, dashboard,create_account_type_form, create_account_form

urlpatterns = [
    path("", dashboard, name="dashboard"),
    path("account_type/form", create_account_type_form, name="create_account_type_form"),
    path("accounts/form", create_account_form, name="create_account_form"),
    path("income_catory/form", create_income_category_form, name="create_income_category_form"),
    path("expenditure_catory/form", create_expenditure_category_form, name="create_expenditure_category_form"),
]
