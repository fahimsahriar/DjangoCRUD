from django.shortcuts import redirect, render

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

#function for deleting an employee
def EmployeeDelete(request, id):
    TemplateFile = "PayRollApp/EmployeeDelete.html"
    employee = Employe.objects.get(id = id)
    dict = {'employee' : employee}
    print(dict)

    #delete button action
    if(request.method == "POST"):
        employee.delete()
        return redirect("employe_list") #need to know how the arguments url works(relative url or static url)
        #explanation of redirect function's first argument
        # to: The destination to which you want to redirect the user. This can be:

        # A URL pattern name (the name defined in urls.py).
        #return redirect('employe_list')  # Assuming 'employe_list' is a URL name in urls.py

        # A relative URL (e.g., "/persons/Employees").
        #path('persons/Employees/', views.employe_list, name='employe_list')

        # An absolute URL (e.g., "https://www.example.com").
        # A model object with a get_absolute_url() method defined.

        # *args: Positional arguments to pass if you're using a URL pattern name.
        #return redirect('employee_detail', id=employee.id)

        # **kwargs: Keyword arguments to pass if your URL pattern expects parameters (e.g., passing an id to a detail view).
        #path('employees/<int:id>/', views.employee_detail, name='employee_detail')

    return render(request, TemplateFile, context=dict)
