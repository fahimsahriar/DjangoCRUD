from django.db import models
from django.core.validators import (
    MinLengthValidator, MaxLengthValidator, MinValueValidator, MaxValueValidator, EmailValidator
)

class Country(models.Model):
    CountryName = models.CharField(
        max_length=40,
        validators=[MinLengthValidator(2)]
    )  # Country name must be at least 2 characters long

    def __str__(self):
        return self.CountryName


class Department(models.Model):
    DepartmentName = models.CharField(
        max_length=40,
        validators=[MinLengthValidator(2)]
    )  # Department name must be at least 2 characters long
    LocationName = models.CharField(
        max_length=40,
        validators=[MinLengthValidator(2)]
    )  # Location name must be at least 2 characters long

    def __str__(self):
        return self.DepartmentName


class Employe(models.Model):

    FirstName = models.CharField(
        max_length=30,
        validators=[MinLengthValidator(2)]
    )  # First name must be at least 2 characters long

    LastName = models.CharField(
        max_length=30,
        validators=[MinLengthValidator(2)]
    )  # Last name must be at least 2 characters long

    TitleName = models.CharField(
        max_length=30,
        validators=[MinLengthValidator(2)]
    )  # Title name must be at least 2 characters long

    HasPassport = models.BooleanField()  # BooleanField doesn't need additional validation

    Salary = models.IntegerField(
        validators=[MinValueValidator(10000), MaxValueValidator(5000000)]
    )  # Salary must be between 10,000 and 5,000,000

    BirthDate = models.DateField()  # For dates, you can use custom validators if necessary

    HiringDate = models.DateField()

    Notes = models.CharField(
        max_length=200,
        validators=[MaxLengthValidator(200)]
    )  # Notes can have a maximum of 200 characters

    Country = models.ForeignKey(
        "Country", on_delete=models.PROTECT
    )  # Country is required

    Email = models.EmailField(
        max_length=100,
        validators=[EmailValidator()]
    )  # Email validation ensures it's a valid email format

    EmployeeDepartment = models.ForeignKey(
        "Department", on_delete=models.PROTECT
    )  # Employee department is required
