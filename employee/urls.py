from django.urls import path
from employee.views import EmployeeDeleteView, EmployeeGenericView, EmployeeUpdateView, Login, ReasonGenericView, RequirementsGenericView,HolidaysGenericView, EmployeeCreateView, RequirementsCreateView
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

app_name= 'employee'

urlpatterns =[
    #Login
    path('login/', Login.as_view(), name="login"),
    path('logout/', auth_views.LogoutView.as_view(template_name='login/login_form.html'), name='logout'),
    #Employee
    path('employee/', login_required(EmployeeGenericView.as_view()), name="list_employee"),
    path('employee/new', login_required(EmployeeCreateView.as_view()), name="new_employee"),
    path('employee/<pk>/update', login_required(EmployeeUpdateView.as_view()), name='update_employee'),
    path('employee/<pk>/delete', login_required(EmployeeDeleteView.as_view()), name='delete_employee'),
    #Requirements
    path('requirements/', RequirementsGenericView.as_view(), name="list_requirements"),
    path('requirements/new', RequirementsCreateView.as_view(), name="new_requirements"),
    #Reasons
    path('reason/', ReasonGenericView.as_view(), name="list_reason"),
    #Holidays
    path('holidays/', HolidaysGenericView.as_view(), name="list_holidays"),
]

