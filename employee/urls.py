from django.urls import path

from employee.views import EmployeeGenericView,RequirementsGenericView

app_name= 'employee'

urlpatterns =[
    path('employee/', EmployeeGenericView.as_view(), name="list_employee"),
    path('requirements/', RequirementsGenericView.as_view(), name="list_requirements"),
]

