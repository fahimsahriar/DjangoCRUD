from django.contrib import admin
from django.urls import path

from PayRollApp import views


urlpatterns = [
    path('Employees/', views.EmployeesList, name='employe_list'),   
    path('employee/<int:id>/', views.EmployeeDetails, name='employee_detail'),
    path('DeleteEmployee/<int:id>/', views.EmployeeDelete, name='Delete_Employee'),
    path('EmployeeUpdate/<int:id>/', views.EmployeeUpdate, name='EmployeeUpdate'),
    path('AddEmployee/', views.AddEmployee, name='AddEmployee'),
    path('signup/', views.SignUp, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('', views.Home, name='home'),
]
