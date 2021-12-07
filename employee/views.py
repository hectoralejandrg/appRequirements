from django.core import paginator
from django.views.generic import ListView, CreateView, DetailView
from django.views.generic.edit import UpdateView, DeleteView
from employee.forms import EmployeeForm, HolidayForm, JefaturaForm, LoginForm, RequirementForm, ReasonForm
from django.contrib.auth.views import LoginView
from employee.models import Employee, Jefatura, Reason, Requirements, Holidays
from django.core.paginator import Paginator
from django.http import Http404


#Login
class Login(LoginView):
    template_name= 'login/login_form.html'
    form_class= LoginForm

#Employe CRUD
class EmployeeGenericView(ListView):
    model = Employee
    paginate_by= 10
    context_object_name = 'employees'

class EmployeeCreateView(CreateView):
    model = Employee
    form_class = EmployeeForm
    success_url= '/employee/'

class EmployeeUpdateView(UpdateView):
    model = Employee
    form_class = EmployeeForm

    def get_success_url(self):
        return '/employee/'

class EmployeeDetailView(DetailView):
    model = Employee

class EmployeeDeleteView(DeleteView):
    model = Employee
    success_url = '/employee/'

#Requirements CRUD
class RequirementsGenericView(ListView):
    model = Requirements
    template_name= 'requirements/requirements_list.html'
    paginate_by= 10
    context_object_name = 'requirements'

    def get_queryset(self):
       result = super(RequirementsGenericView, self).get_queryset()
       query = self.request.GET.get('search')
       if query:
           searchName = Requirements.objects.filter(employee__lastname__contains=query).order_by("-date_requirement")
           result = searchName
       else:
           result = Requirements.objects.all()
       return result

class RequirementsCreateView(CreateView):
    model = Requirements
    template_name= 'requirements/requirements_form.html'
    form_class = RequirementForm
    success_url= '/requirements/'

class RequirementsUpdateView(UpdateView):
    model = Requirements
    template_name= 'requirements/requirements_form.html'
    form_class = RequirementForm

    def get_success_url(self):
        return '/requirements/'

class RequirementsDetailView(DetailView):
    model = Requirements
    template_name= 'requirements/requirements_detail.html'

class RequirementsDeleteView(DeleteView):
    model = Requirements
    success_url = '/requirements/'

#Reason CRUD
class ReasonGenericView(ListView):
    model = Reason
    paginate_by= 10
    template_name= 'reason/reason_list.html'
    context_object_name = 'reasons'

class ReasonCreateView(CreateView):
    model = Reason
    template_name= 'reason/reason_form.html'
    form_class = ReasonForm
    success_url= '/reason/'

class ReasonUpdateView(UpdateView):
    model = Reason
    template_name= 'reason/reason_form.html'
    form_class = ReasonForm
    def get_success_url(self):
        return '/reason/'

class ReasonDetailView(DetailView):
    model = Reason
    template_name= 'reason/reason_detail.html'

class ReasonDeleteView(DeleteView):
    model = Reason
    template_name= 'reason/reason_form.html'
    success_url = '/reason/'

#Holidays CRUD
class HolidaysGenericView(ListView):
    model = Holidays
    paginate_by= 10
    template_name= 'holidays/holidays_list.html'
    context_object_name = 'holidays'


class HolidaysCreateView(CreateView):
    model = Holidays
    template_name= 'holidays/holidays_form.html'
    form_class = HolidayForm 
    success_url= '/holidays/'

class HolidaysUpdateView(UpdateView):
    model = Holidays
    template_name= 'holidays/holidays_form.html'
    form_class = HolidayForm
    def get_success_url(self):
        return '/holidays/'

class HolidaysDetailView(DetailView):
    model = Holidays
    template_name= 'holidays/holidays_detail.html'

class HolidaysDeleteView(DeleteView):
    model = Holidays
    template_name= 'holidays/holidays_form.html'
    success_url = '/holidays/'

#Jefatura CRUD
class JefaturaGenericView(ListView):
    model = Jefatura
    paginate_by= 10
    template_name= 'jefatura/jefatura_list.html'
    context_object_name = 'jefaturas'

class JefaturaCreateView(CreateView):
    model = Jefatura
    template_name= 'jefatura/jefatura_form.html'
    form_class = JefaturaForm
    success_url= '/jefatura/'

class JefaturaUpdateView(UpdateView):
    model = Jefatura
    template_name= 'jefatura/jefatura_form.html'
    form_class = JefaturaForm
    def get_success_url(self):
        return '/jefatura/'

class JefaturaDetailView(DetailView):
    model = Jefatura
    template_name= 'jefatura/jefatura_detail.html'

class JefaturaDeleteView(DeleteView):
    model = Jefatura
    template_name= 'jefatura/jefatura_form.html'
    success_url = '/jefatura/'
