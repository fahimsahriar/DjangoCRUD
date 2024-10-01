from django.shortcuts import render

from PayRollApp.models import Employe

# Create your views here.
def EmployeesList(request):
    Employees = Employe.objects.all()
    TemplateFile = "PayRollApp/EmployeesList.html"
    dict = {'employees' : Employees}
    return render(request, TemplateFile, context=dict)
