from django.db import models
import datetime

class Jefatura(models.Model):
    description = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    state = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.description}'

class Employee(models.Model):
    identification = models.CharField(max_length=13)
    name = models.CharField(max_length=60)
    lastname = models.CharField(max_length=60)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    jefatura = models.ForeignKey(
        Jefatura,
        related_name='jefatura',
        on_delete=models.SET_NULL,
        null=True
    )
    state = models.BooleanField(default=True)
  
    def __str__(self):
        return f'{self.identification} - {self.name} {self.lastname}'
        
class Reason(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    state = models.BooleanField(default=True)
    penalty = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name} - {self.description}'

class Requirements(models.Model):
    code = models.CharField(max_length=6, null=True, blank=True)
    date_requirement = models.DateField()
    date_start = models.DateTimeField()
    date_end = models.DateTimeField()
    hours_discount = models.IntegerField(null=True, blank=True)
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

    class Meta:
        ordering = ('-pk', )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        id = str(self.pk)
        self.code = id.zfill(6)
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.code} - {self.employee.lastname} {self.employee.name}- {self.date_requirement}'

class Holidays(models.Model):
    employee = models.ForeignKey(
        Employee,
        related_name='employeeHolidays',
        on_delete=models.SET_NULL,
        null=True
    )
    position = models.CharField(max_length=100)
    date_last_holidays = models.DateField(null=True, blank=True)
    # date_requirement = models.DateField()
    date_job = models.DateField()
    date_start = models.DateField()
    date_end = models.DateField(null=True, blank=True)
    days = models.IntegerField()
    days_pending = models.IntegerField(null=True, blank=True)
    entry_work= models.DateField(null=True, blank=True)
    days_total= models.IntegerField()
    days_take = models.IntegerField(default=0)
    days_penalty = models.IntegerField(null=True, blank=True)
    period= models.CharField(max_length=100)
    def __str__(self):
        return f'{self.position}- {self.date_requirement}- {self.date_job}- {self.date_start}- {self.date_end} - {self.days} - {self.days_pending} - {self.entry_work}- {self.period}'

class Penalty(models.Model):
    hours_penalty = models.IntegerField()
    observations = models.TextField()
    date = models.DateField(default=datetime.date.today)
    requirement = models.ForeignKey(
        Requirements,
        related_name='requirements',
        on_delete=models.SET_NULL,
        null=True
    )
    def __str__(self):
        return f'{self.hours_penalty}'
