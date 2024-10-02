from django.contrib import admin
from django.urls import path

from PayRollApp import views


urlpatterns = [
    path('Employees/', views.EmployeesList, name='employe_list'),
    path('employee/<int:id>/', views.EmployeeDetails, name='employee_detail'),
    path('DeleteEmployee/<int:id>/', views.EmployeeDelete, name='Delete_Employee'),
]
