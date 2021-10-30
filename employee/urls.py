from django.urls import path

from employee.views import EmployeeGenericView, ReasonGenericView, RequirementsGenericView,HolidaysGenericView, EmployeeCreateView


app_name= 'employee'

urlpatterns =[
    path('employee/', EmployeeGenericView.as_view(), name="list_employee"),
    path('employee/new', EmployeeCreateView.as_view(), name="new_employee"),
    path('reason/', ReasonGenericView.as_view(), name="list_reason"),
    path('requirements/', RequirementsGenericView.as_view(), name="list_requirements"),
    path('holidays/', HolidaysGenericView.as_view(), name="list_holidays"),
]

