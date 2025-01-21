from django.urls import path
from . import views

urlpatterns = [
    path('add_house/', views.add_house, name='add_house'),
]
