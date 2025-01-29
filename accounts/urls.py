from django.urls import path
from .views import create_account, retrieve_account, update_account, delete_account,\
                    create_income, retrieve_income, update_income, delete_income,\
                    create_expenditure,retrieve_expenditure,update_expenditure,delete_expenditure, \
    create_income_category, retrieve_income_category, update_income_category, delete_income_category, \
    create_expenditure_category, retrieve_expenditure_category, update_expenditure_category, delete_expenditure_category
)

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