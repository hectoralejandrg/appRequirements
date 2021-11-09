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

class Requirements(models.Model):
    code = models.CharField(max_length=15)
    date_requirement = models.DateField()
    date_start = models.DateField()
    date_end = models.DateField()
    hours_discount = models.IntegerField()
    employee = models.ForeignKey(
        Employee,
        related_name='employee',
        on_delete=models.SET_NULL,
        null=True
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.code}- {self.date_requirement} - {self.date_start} - {self.date_end} - {self.hours_discount}'

class Reason(models.Model):
    description = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    state = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.description}'

class Holidays(models.Model):
    date_start = models.DateField()
    date_end = models.DateField()
    days = models.DateField()

    def __str__(self):
        return f'{self.date_start} - {self.date_end} - {self.days}'
