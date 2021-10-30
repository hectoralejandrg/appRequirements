from django.urls import path

from employee.views import EmployeeGenericView, ReasonGenericView

app_name= 'employee'

urlpatterns =[
    path('employee/', EmployeeGenericView.as_view(), name="list_employee"),
    path('reason/', ReasonGenericView.as_view(), name="list_reason"),
]
