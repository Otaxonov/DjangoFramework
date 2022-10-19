from django.urls import path
from .views import (
    RegistrationView,
    LoginView,
    LogoutView,
    AccountEditView
)

urlpatterns = [
    path('registration/', RegistrationView, name='accounts_registration'),
    path('login/', LoginView, name='accounts_login'),
    path('logout/', LogoutView, name='accounts_logout'),
    path('edit/', AccountEditView, name='accounts_edit'),
]