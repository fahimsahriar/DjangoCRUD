from django.db import models

# Create your models here.
class Country(models.Model):
    CountryName = models.CharField(max_length=40)

    def __str__(self):
        return self.CountryName
    
class Department(models.Model):
    DepartmentName = models.CharField(max_length=40)
    LocationName = models.CharField(max_length=40)

    def __str__(self):
        return self.DepartmentName

class Employe(models.Model):
    
    COUNTRIES =[
        ("IND", "INDIA"),
        ("USA", "United States Of America"),
        ("UK", "United Kingdom"),
        ("AUS", "AUSTRALIA"),
        ("AU", "AUSTRIA"),
        ("SP", "SPAIN"),
    ]

    FirstName = models.CharField(max_length=30)
    LastName = models.CharField(max_length=30)
    TitleName = models.CharField(max_length=30)
    HasPassport = models.BooleanField()
    Salary = models.IntegerField()
    BirthDate = models.DateField()
    HiringDate = models.DateField()
    Notes = models.CharField(max_length=200)
    #Country = models.CharField(max_length=35, choices=COUNTRIES, default=None)
    Country = models.ForeignKey("Country", default=0, on_delete=models.PROTECT)
    Email = models.EmailField(max_length=100, default="")
    EmployeeDepartment = models.ForeignKey("Department", default=0, on_delete=models.PROTECT)
