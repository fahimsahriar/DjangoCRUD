from django.db import models

# Create your models here.
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
    Country = models.CharField(max_length=35, choices=COUNTRIES, default=None)
    Email = models.EmailField(max_length=100, default="")
