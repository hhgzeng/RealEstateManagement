from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_user, name='login'),
    path('register/', views.register_user, name='register'),
    path('manage_salesperson/', views.manage_salesperson, name='manage_salesperson'),
    path('get_salespeople/', views.get_salespeople, name='get_salespeople'),
]
