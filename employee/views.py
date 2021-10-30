from django.shortcuts import render
from django.views.generic import ListView

from employee.models import Employee, Reason, Requirements


class EmployeeGenericView(ListView):
    model = Employee
    context_object_name = 'employees'


class ReasonGenericView(ListView):
    model = Reason
    context_object_name = 'reasons'
    
class RequirementsGenericView(ListView):
    model = Requirements
    context_object_name = 'requirements'

