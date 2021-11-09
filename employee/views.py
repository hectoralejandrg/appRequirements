from django.views.generic import ListView, CreateView,DetailView,DeleteView
from django.views.generic.edit import UpdateView
from employee.forms import EmployeeForm, RequirementForm, ReasonForm
from django.contrib.auth.views import LoginView
from employee.models import Employee, Reason, Requirements, Holidays

#Login
class Login(LoginView):
    template_name= 'login/login_form.html'

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

class ReasonCreateView(CreateView):
    model = Reason
    form_class = ReasonForm
    success_url= '/reason/'

class ReasonUpdateView(UpdateView):
    model = Reason
    form_class = ReasonForm
    sucess_url = '/reason/'


class ReasonDetailView(DetailView):
    queryset = Reason.objects.all()


class ReasonDeleteView(DeleteView):
    model = Reason
    success_url = '/reason/'

#Holidays CRUD
class HolidaysGenericView(ListView):
    model = Holidays
    context_object_name = 'holidays'

