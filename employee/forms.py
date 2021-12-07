from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from employee.models import Employee, Holidays, Jefatura, Requirements, Reason


class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'remember_me']

    username = forms.CharField(label='Usuario', max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Contraseña', max_length=50,
                               required=True,
                               widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                 'data-toggle': 'password',
                                                                 'id': 'password',
                                                                 'name': 'password',
                                                                 }))
    remember_me = forms.BooleanField(required=False)


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
        fields = '__all__'

    # code = forms.CharField(
    #     label='Código', widget=forms.TextInput(attrs={'class': 'form-control'}))
    date_requirement = forms.CharField(
        label='Fecha del requerimiento', widget=forms.TextInput(attrs={'type': 'date', 'class': 'form-control'}))
    date_start = forms.CharField(
        label='Inicio', widget=forms.TextInput(attrs={'type': 'datetime-local', 'class': 'form-control'}))
    date_end = forms.CharField(
        label='Fin', widget=forms.TextInput(attrs={'type': 'datetime-local', 'class': 'form-control'}))
    hours_discount = forms.CharField(
        label='Horas de permiso', widget=forms.TextInput(attrs={'type': 'number', 'class':'form-control'}))
    employee = forms.ModelChoiceField(label='Empleado', empty_label='Seleccione', queryset=Employee.objects.all(), widget=forms.Select(attrs={'class':'form-select'}))
    reason = forms.ModelChoiceField(label='Razones', empty_label='Seleccione', queryset=Reason.objects.all(), widget=forms.Select(attrs={'class':'form-select'}))

class ReasonForm(forms.ModelForm):

    class Meta:
        model = Reason
        fields = ('__all__')
    
    name = forms.CharField(
        label='Nombre', widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(
        label='Descripcion', widget=forms.TextInput(attrs={'class': 'form-control'}))


    ##Reason = forms.ModelChoiceField(label='Reason', empty_label='Seleccione', queryset=Reason.objects.all(), widget=forms.Select(attrs={'class':'form-select'}))

class HolidayForm(forms.ModelForm):

    class Meta:
        model = Holidays
        fields = '__all__'

    date_start = forms.CharField(
        label='Dia de Inicio', widget=forms.TextInput(attrs={'type': 'date', 'class': 'form-control'}))
    date_end = forms.CharField(
        label='Dia de Fin', widget=forms.TextInput(attrs={'type': 'date', 'class': 'form-control'}))
    days = forms.CharField(
        label='Dias de vacaciones', widget=forms.TextInput(attrs={'type': 'number', 'class':'form-control'}))
    employee = forms.ModelChoiceField(label='Empleado', empty_label='Seleccione', queryset=Employee.objects.all(), widget=forms.Select(attrs={'class':'form-select'}))

class JefaturaForm(forms.ModelForm):

    class Meta:
        model = Jefatura
        fields = ('__all__')
    
    description = forms.CharField(
        label='Descripcion', widget=forms.TextInput(attrs={'class': 'form-control'}))