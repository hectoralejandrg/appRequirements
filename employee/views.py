from django.shortcuts import render
from django.views.generic import ListView

from employee.models import Employee


class EmployeeGenericView(ListView):
    model = Employee
    context_object_name = 'employees'

