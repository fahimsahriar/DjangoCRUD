from django import forms
from PayRollApp.models import Employe
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#Creating  a form based model
class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employe
        fields = "__all__"

        widgets = {
            'BirthDate' : forms.widgets.DateInput(attrs={'type':'date'}),
            'HiringDate' : forms.widgets.DateInput(attrs={'type':'date'})
        }

#form for user sign up

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    username = forms.CharField(max_length=30, required=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']