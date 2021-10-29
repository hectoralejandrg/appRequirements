from django.contrib import admin

# Register your models here.
from employee.models import Employee,Requirements,Reason,Holidays

admin.site.register(Employee)
admin.site.register(Requirements)
admin.site.register(Reason)
admin.site.register(Holidays)

