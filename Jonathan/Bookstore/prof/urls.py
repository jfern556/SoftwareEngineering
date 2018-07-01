from django.urls import path
from . import views

urlpatterns = [
    path ('', views.home, name = 'home'),
    path('register/', views.RegistrationView, name = 'register'),
    path('login/', views.login, name = 'login'),
]
