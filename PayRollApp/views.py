from django.shortcuts import render

from PayRollApp.models import Employe

# Create your views here.
def EmployeesList(request):
    Employees = Employe.objects.all()
    TemplateFile = "PayRollApp/EmployeesList.html"
    dict = {'employees' : Employees}
    return render(request, TemplateFile, context=dict)

#function for individual employee detail
def EmployeeDetails(request, id):
    TemplateFile = "PayRollApp/EmployeeDetails.html"
    employee = Employe.objects.get(id = id)
    dict = {'employee' : employee}
    print(dict)
    return render(request, TemplateFile, context=dict)
