from django import forms
from employee.models import Employee


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
    # state = forms.CharField(
    #     label='Estado', widget=forms.HiddenInput())