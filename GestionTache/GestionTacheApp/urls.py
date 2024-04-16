from django.urls import path
from GestionTacheApp import views

urlpatterns = [
    path('', views.home, name='home'),
]