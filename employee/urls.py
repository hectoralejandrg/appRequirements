from django.urls import path
from employee.views import *
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

app_name= 'employee'

urlpatterns =[
    #Login
    path('login/', Login.as_view(), name="login"),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout/logout.html'), name='logout'),
    #Employee
    path('employee/', login_required(EmployeeGenericView.as_view()), name="list_employee"),
    path('employee/new', login_required(EmployeeCreateView.as_view()), name="new_employee"),
    path('employee/<pk>/update', login_required(EmployeeUpdateView.as_view()), name='update_employee'),
    path('employee/<pk>/detail', login_required(EmployeeDetailView.as_view()), name='detail_employee'),
    path('employee/<pk>/delete', login_required(EmployeeDeleteView.as_view()), name='delete_employee'),
    #Requirements
    path('requirements/', login_required(RequirementsGenericView.as_view()), name="list_requirements"),
    path('requirements/new', login_required(RequirementsCreateView.as_view()), name="new_requirements"),
    path('requirements/<pk>/update', login_required(RequirementsUpdateView.as_view()), name='update_requirements'),
    path('requirements/<pk>/detail', login_required(RequirementsDetailView.as_view()), name='detail_requirements'),
    path('requirements/<pk>/delete', login_required(RequirementsDeleteView.as_view()), name='delete_requirements'),
    path('requirements/<pk>/report', login_required(MyDetailViewPDF.as_view()), name='report_requirements'),
    #Reasons
    path('reason/', ReasonGenericView.as_view(), name="list_reason"),
    path('reason/new', ReasonCreateView.as_view(), name="new_reason"),
    path('reason/<pk>/update', ReasonUpdateView.as_view(), name='update_reason'),
    path('reason/<pk>/detail', ReasonDetailView.as_view(), name='detail_reason'),
    path('reason/<pk>/delete', ReasonDeleteView.as_view(), name='delete_reason'),
    #Holidays
    path('holidays/', login_required(HolidaysGenericView.as_view()), name="list_holidays"),
    path('holidays/new', login_required(HolidaysCreateView.as_view()), name="new_holidays"), 
    path('holidays/<pk>/update', login_required(HolidaysUpdateView.as_view()), name='update_holidays'),
    path('holidays/<pk>/detail', login_required(HolidaysDetailView.as_view()), name='detail_holidays'),
    path('holidays/<pk>/delete', HolidaysDeleteView.as_view(), name='delete_holidays'),
    #Jefatura
    path('jefatura/', login_required(JefaturaGenericView.as_view()), name="list_jefatura"),
    path('jefatura/new', login_required(JefaturaCreateView.as_view()), name="new_jefatura"),
    path('jefatura/<pk>/update', login_required(JefaturaUpdateView.as_view()), name='update_jefatura'),
    path('jefatura/<pk>/detail', login_required(JefaturaDetailView.as_view()), name='detail_jefatura'),
    path('jefatura/<pk>/delete', login_required(JefaturaDeleteView.as_view()), name='delete_jefatura'),
    #Penalty
    path('penalty/', login_required(PenaltyGenericView.as_view()), name='list_penalty'),
    path('penalty/new', login_required(PenaltyCreateView.as_view()), name='new_penalty'),
]

