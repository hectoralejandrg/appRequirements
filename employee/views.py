from django.views.generic import ListView, CreateView, DetailView
from django.views.generic.edit import UpdateView, DeleteView
from employee.forms import EmployeeForm, HolidayForm, JefaturaForm, LoginForm, PasswordChangeForm, PenaltyForm, RequirementForm, ReasonForm
from django.contrib.auth.views import LoginView, PasswordChangeView
from employee.models import Employee, Jefatura, Penalty, Reason, Requirements, Holidays
from django.db.models import Sum, Q
from django.http import HttpResponseRedirect
import datetime


#Login
class Login(LoginView):
    template_name= 'login/login_form.html'
    form_class= LoginForm

class ChangePassword(PasswordChangeView):
    template_name= 'login/change_password.html'
    form_class= PasswordChangeForm
    success_url = '/employee/'


#Employe CRUD
class EmployeeGenericView(ListView):
    model = Employee
    paginate_by= 10
    context_object_name = 'employees'

    def get_queryset(self):
       result = super(EmployeeGenericView, self).get_queryset().order_by("-lastname")
       query = self.request.GET.get('search')
       if query:
           searchName = Employee.objects.filter(Q(identification__icontains=query)| Q(lastname__icontains=query)).order_by("-lastname")
           result = searchName
       else:
           result = Employee.objects.all()
       return result

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
       result = super(RequirementsGenericView, self).get_queryset().order_by("-code")
       query = self.request.GET.get('search')
       if query:
           searchName = Requirements.objects.filter(Q(employee__lastname=query)|Q(code=query)).order_by("-code")
           result = searchName
       else:
           result = Requirements.objects.all()
       return result

class RequirementsCreateView(CreateView):
    model = Requirements
    template_name= 'requirements/requirements_form.html'
    form_class = RequirementForm
    success_url= '/requirements/'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        requi = self.object
        dateEnd = requi.date_end
        dateStart = requi.date_start
        dif = dateEnd-dateStart
        minutes = dif.seconds / 60
        hours = divmod(minutes, 60)
        hd = hours[0]
        if hours[1]>40:
            hd = hd + 1
        requi.hours_discount = int(hd)
        requi.save()

        if requi.reason.penalty:
            Penalty.objects.create(hours_penalty=requi.hours_discount, observations=requi.reason.name,date=requi.date_requirement, requirement=requi)
        return HttpResponseRedirect(self.get_success_url())


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

    def get_queryset(self):
       result = super(HolidaysGenericView, self).get_queryset()
       query = self.request.GET.get('search')
       if query:
           result = Holidays.objects.filter(Q(employee__identification__icontains=query)| Q(employee__lastname__icontains=query)).order_by("-date_requirement")
       else:
           result = Holidays.objects.all().order_by("-date_job")
       return result

class HolidaysCreateView(CreateView):
    model = Holidays
    template_name= 'holidays/holidays_form.html'
    form_class = HolidayForm 
    success_url= '/holidays/'

    def get_context_data(self, **kwargs):
        context = super(HolidaysCreateView, self).get_context_data(**kwargs)
        context["employeeList"] = Employee.objects.all()
        employeeSelect = self.request.GET.get('employeeSelect')
        dateLastHolidays = self.request.GET.get('dateLastHolidays')
        if employeeSelect and dateLastHolidays:
            employee = Employee.objects.get(identification= employeeSelect)
            totalHoursPenalty = Penalty.objects.filter(requirement__employee__identification= employeeSelect, date__range=[dateLastHolidays, datetime.datetime.now()]).aggregate(Sum('hours_penalty'))
            try:
                hours_penalty = divmod(totalHoursPenalty["hours_penalty__sum"], 8)
                days = hours_penalty[0]
                hours = hours_penalty[1]
            except:
                days = 0
                hours = 0
            data = {'employee':employee, 'days': days, 'hours':hours}
            context['data']= data
        return context
    
    def form_valid(self, form):
        self.object = form.save(commit=False)
        holiday = self.object
        totalHoursPenalty = Penalty.objects.filter(requirement__employee__identification= holiday.employee.identification, date__range=[holiday.date_last_holidays, datetime.datetime.now()]).aggregate(Sum('hours_penalty'))
        hours_penalty = divmod(totalHoursPenalty["hours_penalty__sum"], 8)
        print(f'********{hours_penalty}')
        holiday.days_penalty = hours_penalty[0]
        day_solicitados = holiday.days + hours_penalty[0]
        if holiday.days_total - day_solicitados >= 0:
            holiday.days_take = day_solicitados
            holiday.days_pending =  holiday.days_total - holiday.days_take
            holiday.date_end = holiday.date_start + datetime.timedelta(days=holiday.days-1)
        else:
            holiday.days_take = holiday.days - hours_penalty[0]
            holiday.days_pending =  holiday.days_total - holiday.days
            holiday.date_end = holiday.date_start + datetime.timedelta(days=holiday.days-1) - datetime.timedelta(days=hours_penalty[0])

        holiday.entry_work = holiday.date_end + datetime.timedelta(days=1)
        holiday.save()
        return HttpResponseRedirect(self.get_success_url())

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

    def get_queryset(self):
       result = super(JefaturaGenericView, self).get_queryset()
       query = self.request.GET.get('search')
       if query:
           searchName = Jefatura.objects.filter(Q(description__icontains=query))
           result = searchName
       else:
           result = Jefatura.objects.all()
       return result

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

#ReportPDF requerimiento
class MyDetailViewPDF(DetailView):
    # vanilla Django DetailView
    model = Requirements
    template_name = 'report/requirementsReport.html'

#ReportPDFHolidays
class MyDetailViewPDF2(DetailView):
    # vanilla Django DetailView
    model = Holidays
    template_name = 'report/holidaysReport.html'

    def get_context_data(self, **kwargs):
        object = super().get_context_data(**kwargs)
        date_diff = object['object'].date_end - object['object'].date_start
        object['date_diff'] = date_diff.days + 1
        # object['date_dif']= self.request.GET.get('days')-self.request.GET.get('days_penalty')
        return object

class PenaltyGenericView(ListView):
    model = Penalty
    paginate_by= 10
    template_name= 'penalty/penalty_list.html'
    context_object_name = 'penalties'

    def get_queryset(self):
        return super().get_queryset().order_by('-requirement__code')

class PenaltyCreateView(CreateView):
    model = Penalty
    template_name= 'penalty/penalty_form.html'
    form_class = PenaltyForm
    success_url= '/penalty/'

class PenaltyUpdateView(UpdateView):
    model = Penalty
    template_name= 'penalty/penalty_form.html'
    form_class = PenaltyForm
    def get_success_url(self):
        return '/penalty/'

class PenaltyDetailView(DetailView):
    model = Penalty
    template_name= 'penalty/penalty_detail.html'

class PenaltyDeleteView(DeleteView):
    model = Penalty
    template_name= 'penalty/penalty_form.html'
    success_url = '/penalty/'

#reportPenalty CRUD
class ReportGenericView(ListView):
    model = Penalty
    template_name= 'report/report_list.html'
    context_object_name = 'context'

    def get_queryset(self):
        result = super(ReportGenericView, self).get_queryset()
        employee = self.request.GET.get('employee')
        dateStart = self.request.GET.get('dateStart')
        dateEnd = self.request.GET.get('dateEnd')
        if employee and dateStart and dateEnd:
            result = Penalty.objects.filter(requirement__employee__identification= employee, date__range=[dateStart, dateEnd])
        else:
            result = None
        return result

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['employee']=Employee.objects.all()
        
        employee = self.request.GET.get('employee')
        dateStart = self.request.GET.get('dateStart')
        dateEnd = self.request.GET.get('dateEnd')
        if employee and dateStart and dateEnd:
            result = Penalty.objects.filter(requirement__employee__identification= employee, date__range=[dateStart, dateEnd]).aggregate(Sum('hours_penalty'))
            context['total'] = result
        return context

#reportRequirements CRUD
class Report2GenericView(ListView):
    model = Requirements
    template_name= 'report/reportPermiso_list.html'
    context_object_name = 'context'

    def get_queryset(self):
        result = super(Report2GenericView, self).get_queryset()
        employee = self.request.GET.get('employee')
        dateStart = self.request.GET.get('dateStart')
        dateEnd = self.request.GET.get('dateEnd')
        if employee and dateStart and dateEnd:
            result = Requirements.objects.filter(employee__identification= employee, date_requirement__range=[dateStart, dateEnd])
        else:
            result = None
        return result

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['employee']=Employee.objects.all()
        
        return context