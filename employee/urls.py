from django.urls import path

from employee.views import EmployeeGenericView

app_name= 'employee'

urlpatterns =[
    path('employee/', EmployeeGenericView.as_view(), name="list_employee"),
]