from django import forms
from PayRollApp.models import Employe

#Creating  a form based model
class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employe
        fields = "__all__"

        widgets = {
            'BirthDate' : forms.widgets.DateInput(attrs={'type':'date'}),
            'HiringDate' : forms.widgets.DateInput(attrs={'type':'date'})
        }