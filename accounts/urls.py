from django.urls import path
from .views import create_account, retrieve_account, update_account, delete_account,\
                    create_income, retrieve_income, update_income, delete_income,\
                    create_expenditure,retrieve_expenditure,update_expenditure,delete_expenditure

urlpatterns = [
    
    path("accounts/create/", create_account, name="create_account"),
    path("accounts/retrieve/", retrieve_account, name="retrieve_account"),
    path("accounts/update/", update_account, name="update_account"),
    path("accounts/delete/", delete_account, name="delete_account"),

    path("incomes/create/", create_income, name="create_income"),
    path("incomes/retrieve/", retrieve_income, name="retrieve_income"),
    path("incomes/update/", update_income, name="update_income"),
    path("incomes/delete/", delete_income, name="delete_income"),

    path("expenditures/create/", create_expenditure, name="create_expenditure"),
    path("expenditures/retrieve/", retrieve_expenditure, name="retrieve_expenditure"),
    path("expenditures/update/", update_expenditure, name="update_expenditure"),
    path("expenditures/delete/", delete_expenditure, name="delete_expenditure"),
]