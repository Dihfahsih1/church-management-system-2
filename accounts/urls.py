from django.urls import path
from .views import  create_account, create_account_type, delete_account_type, list_account_types, retrieve_account, retrieve_account_type, update_account, delete_account,\
                    create_income, retrieve_income, update_account_type, update_income, delete_income,\
                    create_expenditure,retrieve_expenditure,update_expenditure,delete_expenditure, \
                    create_income_category, retrieve_income_category, update_income_category, delete_income_category, \
                    create_expenditure_category, retrieve_expenditure_category, update_expenditure_category, delete_expenditure_category

urlpatterns = [
    
    path("accounts/create/", create_account, name="create_account"),
    path("accounts/retrieve/", retrieve_account, name="retrieve_account"),
    path("accounts/update/", update_account, name="update_account"),
    path("accounts/delete/", delete_account, name="delete_account"),

    path("accounttypes/create/", create_account_type, name="create_account_type"),
    path("accountstypes/retrieve/", retrieve_account_type, name="retrieve_account_type"),
    path("accountstypes/update/", update_account_type, name="update_account_type"),
    path("accountstypes/delete/", delete_account_type, name="delete_account_type"),
    path("accountstypes/list/", list_account_types, name="list_account_types"),

    path("incomes/create/", create_income, name="create_income"),
    path("incomes/retrieve/", retrieve_income, name="retrieve_income"),
    path("incomes/update/", update_income, name="update_income"),
    path("incomes/delete/", delete_income, name="delete_income"),

    path("expenditures/create/", create_expenditure, name="create_expenditure"),
    path("expenditures/retrieve/", retrieve_expenditure, name="retrieve_expenditure"),
    path("expenditures/update/", update_expenditure, name="update_expenditure"),
    path("expenditures/delete/", delete_expenditure, name="delete_expenditure"),

     # Income Category
    path("income-category/create/", create_income_category, name="create_income_category"),
    path("income-category/retrieve/", retrieve_income_category, name="retrieve_income_category"),
    path("income-category/update/", update_income_category, name="update_income_category"),
    path("income-category/delete/", delete_income_category, name="delete_income_category"),

    # Expenditure Category
    path("expenditure-category/create/", create_expenditure_category, name="create_expenditure_category"),
    path("expenditure-category/retrieve/", retrieve_expenditure_category, name="retrieve_expenditure_category"),
    path("expenditure-category/update/", update_expenditure_category, name="update_expenditure_category"),
    path("expenditure-category/delete/", delete_expenditure_category, name="delete_expenditure_category"),
 
]