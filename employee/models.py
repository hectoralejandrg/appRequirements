from django.db import models


class Employee(models.Model):
    identification = models.CharField(max_length=13)
    name = models.CharField(max_length=60)
    lastname = models.CharField(max_length=60)
    job = models.CharField(max_length=60)
    department = models.CharField(max_length=60)
    created = models.DateField()
    updated = models.DateField()
    state = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.identification} - {self.name} {self.lastname}'
