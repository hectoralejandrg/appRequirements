from django.db import models
from django.views.generic import ListView, CreateView, DetailView
from django.views.generic.edit import UpdateView, DeleteView
from employee.forms import EmployeeForm, LoginForm, RequirementForm
from django.contrib.auth.views import LoginView
from employee.models import Employee, Reason, Requirements, Holidays

#Login
class Login(LoginView):
    template_name= 'login/login_form.html'
    form_class= LoginForm

#Employe CRUD
class EmployeeGenericView(ListView):
    model = Employee
    context_object_name = 'employees'

class EmployeeCreateView(CreateView):
    model = Employee
    form_class = EmployeeForm
    success_url= '/employee/'

class EmployeeUpdateView(UpdateView):
    model = Employee
    form_class = EmployeeForm
    sucess_url = '/employee/'

class EmployeeDetailView(DetailView):
    queryset = Employee.objects.all()

class EmployeeDeleteView(DeleteView):
    model = Employee
    success_url = '/employee/'

#Requirements CRUD
class RequirementsGenericView(ListView):
    model = Requirements
    context_object_name = 'requirements'

class RequirementsCreateView(CreateView):
    model = Requirements
    form_class = RequirementForm
    success_url= '/requirements/'


#Reason CRUD
class ReasonGenericView(ListView):
    model = Reason
    context_object_name = 'reasons'

#Holidays CRUD
class HolidaysGenericView(ListView):
    model = Holidays
    context_object_name = 'holidays'

