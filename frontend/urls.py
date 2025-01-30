from django.urls import path
from .views import dashboard,create_account_type_form, create_account_form

urlpatterns = [
    path("", dashboard, name="dashboard"),
    path("account_type/form", create_account_type_form, name="create_account_type_form"),
    path("accounts/form", create_account_form, name="create_account_form"),

]
