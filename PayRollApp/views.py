from django.shortcuts import redirect, render
from django.core.paginator import Paginator

from PayRollApp.forms import EmployeeForm
from PayRollApp.models import Employe
from crudProjectDjango import settings

# Create your views here.
def EmployeesList(request):
    TemplateFile = "PayRollApp/EmployeesList.html"

    #Employees = Employe.objects.all()
    Employees = Employe.objects.select_related('EmployeeDepartment', 'Country').all()
    # for employee in Employees:
    #     print(employee.FirstName, employee.LastName, employee.Salary)
    #     fields = [field.name for field in employee._meta.get_fields()]
    #     print(fields)

    page_size = getattr(settings, 'Employee_List_Page_Size', 2)
    paginator = Paginator(Employees, page_size)  # Show 25 contacts per page.
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    
    dict = {'employees' : page_obj}
    return render(request, TemplateFile, context=dict)

#function for individual employee detail
def EmployeeDetails(request, id):
    TemplateFile = "PayRollApp/EmployeeDetails.html"
    #employee = Employe.objects.get(id = id)
    employee = Employe.objects.select_related('EmployeeDepartment', 'Country').all().filter(id = id)
    dict = {'employee' : employee[0]}
    return render(request, TemplateFile, context=dict)

#function for deleting an employee
def EmployeeDelete(request, id):
    TemplateFile = "PayRollApp/EmployeeDelete.html"
    employee = Employe.objects.select_related('EmployeeDepartment', 'Country').all().filter(id = id)
    dict = {'employee' : employee[0]}
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

#function for editing employee detail
def EmployeeUpadte(request, id):
    TemplateFile = "PayRollApp/EmployeeUpadte.html"
    employee = Employe.objects.get(id = id)

    if request.method == "POST":
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
        return redirect("employe_list")
    else:
        form = EmployeeForm(instance=employee)

    dict = {'form' : form}
    return render(request, TemplateFile, context=dict)

#function for adding new employee
def AddEmployee(request):
    TemplateFile = "PayRollApp/AddEmployee.html"
    employee = Employe()

    if request.method == "POST":
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect("employe_list")
        else:
            print(form.errors)  # Print any validation errors
    else:
        form = EmployeeForm(instance=employee)
    dict = {'form' : form}

    return render(request, TemplateFile, context=dict)