from django.urls import path
from employee.views import EmployeeDeleteView, EmployeeGenericView, EmployeeUpdateView, Login, ReasonGenericView, RequirementsGenericView,HolidaysGenericView, EmployeeCreateView, RequirementsCreateView

app_name= 'employee'

urlpatterns =[
    #Login
    path('login/', Login.as_view(), name="login"),
    #Employee
    path('employee/', EmployeeGenericView.as_view(), name="list_employee"),
    path('employee/new', EmployeeCreateView.as_view(), name="new_employee"),
    path('employee/<pk>/update', EmployeeUpdateView.as_view(), name='update_employee'),
    path('employee/<pk>/delete', EmployeeDeleteView.as_view(), name='delete_employee'),
    #Requirements
    path('requirements/', RequirementsGenericView.as_view(), name="list_requirements"),
    path('requirements/new', RequirementsCreateView.as_view(), name="new_requirements"),
    #Reasons
    path('reason/', ReasonGenericView.as_view(), name="list_reason"),
    #Holidays
    path('holidays/', HolidaysGenericView.as_view(), name="list_holidays"),
]

