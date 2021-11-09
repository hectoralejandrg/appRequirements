from django import forms
from django.contrib.auth.models import User
from django.forms import fields
from employee.models import Employee, Reason, Requirements

class LoginForm(forms.ModelForm):
    class Meta:
        model= User
        fields = ['username', 'password']

    username = forms.ChoiceField(label='Usuario',widget=forms.TextInput(attrs={'class': 'form-control'}))

class EmployeeForm(forms.ModelForm):

    class Meta:
        model = Employee
        fields = '__all__'

    identification = forms.CharField(
        label='Identificación', widget=forms.TextInput(attrs={'class': 'form-control'}))
    name = forms.CharField(
        label='Nombres', widget=forms.TextInput(attrs={'class': 'form-control'}))
    lastname = forms.CharField(
        label='Apellidos', widget=forms.TextInput(attrs={'class': 'form-control'}))
    department = forms.CharField(
        label='Departamento', widget=forms.TextInput(attrs={'class': 'form-control'}))
    job = forms.CharField(
        label='Cargo', widget=forms.TextInput(attrs={'class': 'form-control'}))


class RequirementForm(forms.ModelForm):

    class Meta:
        model = Requirements
        fields = ('code', 'date_requirement', 'date_start',
              'date_end', 'hours_discount', 'employee')

    code = forms.CharField(
        label='Código', widget=forms.TextInput(attrs={'class': 'form-control'}))
    date_requirement = forms.CharField(
        label='Fecha del requerimiento', widget=forms.TextInput(attrs={'type': 'date', 'class':'form-control'}))
    date_start = forms.CharField(
        label='Inicio', widget=forms.TextInput(attrs={'type': 'datetime-local', 'class':'form-control'}))
    date_end = forms.CharField(
        label='Fin', widget=forms.TextInput(attrs={'type': 'datetime-local', 'class':'form-control'}))
    hours_discount = forms.CharField(
        label='Horas de permiso', widget=forms.TextInput(attrs={'type': 'number', 'class':'form-control'}))
    employee = forms.ModelChoiceField(label='Empleado', empty_label='Seleccione', queryset=Employee.objects.all(), widget=forms.Select(attrs={'class':'form-select'}))

class ReasonForm(forms.ModelForm):

    class Meta:
        model = Reason
        fields = ('__all__')
    
    description = forms.CharField(
        label='Descripcion', widget=forms.TextInput(attrs={'class': 'form-control'}))


    ##Reason = forms.ModelChoiceField(label='Reason', empty_label='Seleccione', queryset=Reason.objects.all(), widget=forms.Select(attrs={'class':'form-select'}))


