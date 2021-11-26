from django.db import models


class Employee(models.Model):
    identification = models.CharField(max_length=13)
    name = models.CharField(max_length=60)
    lastname = models.CharField(max_length=60)
    job = models.CharField(max_length=60)
    department = models.CharField(max_length=60)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    state = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.identification} - {self.name} {self.lastname}'
class Reason(models.Model):
    name = models.CharField(max_length=60)
    description = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    state = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name}{self.description}'

class Requirements(models.Model):
    code = models.CharField(max_length=15)
    date_requirement = models.DateField()
    date_start = models.DateTimeField()
    date_end = models.DateTimeField()
    hours_discount = models.IntegerField()
    employee = models.ForeignKey(
        Employee,
        related_name='employee',
        on_delete=models.SET_NULL,
        null=True
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    reason = models.ForeignKey(
        Reason,
        related_name='reason',
        on_delete=models.SET_NULL,
        null=True
    )
    def __str__(self):
        return f'{self.code}- {self.date_requirement} - {self.date_start} - {self.date_end} - {self.hours_discount}'

class Holidays(models.Model):
    date_start = models.DateField()
    date_end = models.DateField()
    days = models.DateField()

    employee = models.ForeignKey(
        Employee,
        related_name='employeeHolidays',
        on_delete=models.SET_NULL,
        null=True
    )
    def __str__(self):
        return f'{self.date_start} - {self.date_end} - {self.days}'
        