from django.contrib import admin
from django.urls import path

from PayRollApp import views


urlpatterns = [
    path('Employees/', views.EmployeesList, name='person_list'),
]
