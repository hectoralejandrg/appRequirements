from django.shortcuts import render
from django.views.generic import ListView, CreateView

from employee.models import Employee, Reason, Requirements, Holidays


class EmployeeGenericView(ListView):
    model = Employee
    context_object_name = 'employees'


class EmployeeCreateView(CreateView):
    model = Employee
    fields = '__all__'
    success_url= '/employee/'


class ReasonGenericView(ListView):
    model = Reason
    context_object_name = 'reasons'

class ReasonCreateView(CreateView):
    model = Reason
    fields = '__all__'
    success_url= '/reason/'
    
class RequirementsGenericView(ListView):
    model = Requirements
    context_object_name = 'requirements'

class HolidaysGenericView(ListView):
    model = Holidays
    context_object_name = 'holidays'

