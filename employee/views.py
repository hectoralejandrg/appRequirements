from django.views.generic import ListView, CreateView, DetailView
from django.views.generic.edit import UpdateView, DeleteView
from employee.forms import EmployeeForm, LoginForm, RequirementForm, ReasonForm
from django.contrib.auth.views import LoginView
from employee.models import Employee, Reason, Requirements, Holidays


import functools
from django.conf import settings
from django_weasyprint import WeasyTemplateResponseMixin
from django_weasyprint.views import WeasyTemplateResponse

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
    context_object_name = 'requirements'

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
    template_name= 'holidays/holidays_list.html'
    context_object_name = 'holidays'


#ReportPDF
class MyDetailViewPDF(DetailView):
    # vanilla Django DetailView
    model = Requirements
    template_name = 'report/requirementsReport.html'

class DynamicNameView(WeasyTemplateResponseMixin, MyDetailViewPDF):
    # dynamically generate filename
    def get_pdf_filename(self, *args, **kwargs):
        data=self.get_context_data(**kwargs)
        #data2= **data
        print(data)
        
        name = data.__str__
        return f'foo-{name}.pdf'