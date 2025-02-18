from django.urls import path
from .views import  create_account_type, delete_account_type, list_account_types, list_expenditure, list_expenditure_categories, list_income_categories, list_incomes, list_or_create_accounts, retrieve_account, retrieve_account_type, update_account, delete_account,\
                    create_income, retrieve_income, update_account_type, update_income, delete_income,\
                    create_expenditure,retrieve_expenditure,update_expenditure,delete_expenditure, \
                    create_income_category, retrieve_income_category, update_income_category, delete_income_category, \
                    create_expenditure_category, retrieve_expenditure_category, update_expenditure_category, delete_expenditure_category, \
                    register_user, login_user, logout_user
urlpatterns = [
    path('accounts/register/', register_user, name='register'),
    path('accounts/login/', login_user, name='login'),
    path('accounts/logout/', logout_user, name='logout'),

    path("accounts/create/", list_or_create_accounts, name="create_account"),
    path("accounts/retrieve/", retrieve_account, name="retrieve_account"),
    path("accounts/update/", update_account, name="update_account"),
    path("accounts/delete/", delete_account, name="delete_account"),
    path("accounts/list/", list_or_create_accounts, name="list_account"),

    path("accounttypes/create/", create_account_type, name="create_account_type"),
    path("accountstypes/retrieve/", retrieve_account_type, name="retrieve_account_type"),
    path("accountstypes/update/", update_account_type, name="update_account_type"),
    path("accountstypes/delete/", delete_account_type, name="delete_account_type"),
    path("accountstypes/list/", list_account_types, name="list_account_types"),

    path("incomes/create/", create_income, name="create_income"),
    path("incomes/retrieve/", retrieve_income, name="retrieve_income"),
    path("incomes/update/", update_income, name="update_income"),
    path("incomes/delete/", delete_income, name="delete_income"),
    path("incomes/list/", list_incomes, name="list_incomes"),

    path("expenditures/create/", create_expenditure, name="create_expenditure"),
    path("expenditures/retrieve/", retrieve_expenditure, name="retrieve_expenditure"),
    path("expenditures/update/", update_expenditure, name="update_expenditure"),
    path("expenditures/delete/", delete_expenditure, name="delete_expenditure"),
    path("expenditures/list/", list_expenditure, name="list_expenditures"),

     # Income Category
    path("income-category/create/", create_income_category, name="create_income_category"),
    path("income-category/retrieve/", retrieve_income_category, name="retrieve_income_category"),
    path("income-category/update/", update_income_category, name="update_income_category"),
    path("income-category/delete/", delete_income_category, name="delete_income_category"),
    path("income-category/list/", list_income_categories, name="list_income_categories"),
    

    # Expenditure Category
    path("expenditure-category/create/", create_expenditure_category, name="create_expenditure_category"),
    path("expenditure-category/retrieve/", retrieve_expenditure_category, name="retrieve_expenditure_category"),
    path("expenditure-category/update/", update_expenditure_category, name="update_expenditure_category"),
    path("expenditure-category/delete/", delete_expenditure_category, name="delete_expenditure_category"),
    path("expenditure-category/list/", list_expenditure_categories, name="list_expenditure_categories"),
 
]