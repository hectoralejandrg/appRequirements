from django.shortcuts import render
from django.views.generic import ListView

from employee.models import Employee, Requirements


class EmployeeGenericView(ListView):
    model = Employee
    context_object_name = 'employees'

class RequirementsGenericView(ListView):
    model = Requirements
    context_object_name = 'requirements'

