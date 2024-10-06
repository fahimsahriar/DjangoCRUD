from django.shortcuts import redirect, render
from django.core.paginator import Paginator
from django.db.models import Q, Value
from django.db.models.functions import Concat

from PayRollApp.forms import EmployeeForm
from PayRollApp.models import Employe
from crudProjectDjango import settings

# Create your views here.
def EmployeesList(request):
    TemplateFile = "PayRollApp/EmployeesList.html"

    #Employees = Employe.objects.all()
    #Employees = Employe.objects.select_related('EmployeeDepartment', 'Country').all()
    # for employee in Employees:
    #     print(employee.FirstName, employee.LastName, employee.Salary)
    #     fields = [field.name for field in employee._meta.get_fields()]
    #     print(fields)

    #sorting
    sort_by = request.GET.get('sort_by', 'id')
    sort_order = request.GET.get('sort_order', 'asc')

    valid_sort_fields = ['id', 'FirstName', 'LastName', 'TitleName']
    if sort_by not in valid_sort_fields:
        sort_by = 'id'

    

    #search query code
    search_query = request.GET.get('search', '') #(parameter explanation)if we try to put something on search box
    #then it will come along search, either
    #the search query will be empty
    # Employees = Employe.objects.select_related('EmployeeDepartment', 'Country').filter(
    #     Q(id__icontains=search_query) |
    #     Q(FirstName__icontains=search_query) |
    #     Q(LastName__icontains=search_query) |
    #     Q(Email__icontains=search_query) |
    #     Q(TitleName__icontains=search_query) 
    # )

    Employees = Employe.objects.select_related('EmployeeDepartment', 'Country').annotate(
    full_name=Concat('FirstName', Value(' '), 'LastName', Value(' '), 'TitleName')
    ).filter(
        Q(id__icontains=search_query) |
        Q(FirstName__icontains=search_query) |
        Q(LastName__icontains=search_query) |
        Q(Email__icontains=search_query) |
        Q(TitleName__icontains=search_query) |
        Q(full_name__icontains=search_query)  # Search the combined full_name
    )

    #sorting part 2
    if(sort_order == 'dsc'):
        Employees = Employees.order_by(f'-{sort_by}')
    else:
        Employees = Employees.order_by(sort_by)
        

    #Paginator code
    page_size = getattr(settings, 'Employee_List_Page_Size', 2)
    paginator = Paginator(Employees, page_size)  # Show 25 contacts per page.
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    
    dict = {'employees' : page_obj, 'sort_by': sort_by, 'sort_order': sort_order}
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
def EmployeeUpdate(request, id):
    TemplateFile = "PayRollApp/EmployeeUpdate.html"
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