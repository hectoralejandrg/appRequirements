from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from employee.models import Employee, Holidays, Jefatura, Penalty, Requirements, Reason
from datetime import date, datetime

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
    jefatura = forms.ModelChoiceField(label='Cargo/Jefatura', empty_label='Seleccione', queryset=Jefatura.objects.all(), widget=forms.Select(attrs={'class':'form-select'}))


class RequirementForm(forms.ModelForm):

    class Meta:
        model = Requirements
        exclude = ('code','hours_discount',)

    def clean(self):
        super(RequirementForm, self).clean()
        dateStart = datetime.fromisoformat(self.cleaned_data.get('date_start'))
        dateEnd = datetime.fromisoformat(self.cleaned_data.get('date_end'))
        dif = dateEnd - dateStart
        minutes = dif.seconds / 60
        hours = divmod(minutes, 60)
        hd = hours[0]
        if hours[1]>40:
            hd = hd+1
        if hd>8:
            self.add_error('date_end', 'Campo: Fin del Permiso incorrecto. No se puede superar las 8 horas de permiso.')
        if hd == 0:
            self.add_error('date_end', 'Campo: Fin del Permiso incorrecto. Debe haber al menos 1 hora de diferencia.')

    # code = forms.CharField(
    #     label='Código', widget=forms.TextInput(attrs={'class': 'form-control'}))
    date_requirement = forms.CharField(
        label='Fecha de Solicitud del Permiso', widget=forms.TextInput(attrs={'type': 'date', 'class': 'form-control'}))
    date_start = forms.CharField(
        label='Inicio del Permiso', widget=forms.TextInput(attrs={'type': 'datetime-local', 'class': 'form-control'}))
    date_end = forms.CharField(
        label='Fin del Permiso', widget=forms.TextInput(attrs={'type': 'datetime-local', 'class': 'form-control'}))
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
    penalty = forms.CharField(label='Cargo a vacaciones?', widget=forms.CheckboxInput())


    ##Reason = forms.ModelChoiceField(label='Reason', empty_label='Seleccione', queryset=Reason.objects.all(), widget=forms.Select(attrs={'class':'form-select'}))

class HolidayForm(forms.ModelForm):

    class Meta:
        model = Holidays
        fields = '__all__'
    position = forms.CharField(
        label='Cargo', widget=forms.TextInput(attrs={'class': 'form-control'}))
    date_requirement = forms.CharField(
        label='Fecha del documento', widget=forms.TextInput(attrs={'type': 'date', 'class': 'form-control'}))
    date_job = forms.CharField(
        label='Fecha a oficio', widget=forms.TextInput(attrs={'type': 'date', 'class': 'form-control'}))
    days_pending = forms.CharField(
        label='Dias pendientes de  vacaciones', widget=forms.TextInput(attrs={'type': 'number', 'class':'form-control'}))
    date_start = forms.CharField(
        label='Dia de Inicio', widget=forms.TextInput(attrs={'type': 'date', 'class': 'form-control'}))
    date_end = forms.CharField(
        label='Dia de Fin', widget=forms.TextInput(attrs={'type': 'date', 'class': 'form-control'}))
    days = forms.CharField(
        label='Dias de vacaciones', widget=forms.TextInput(attrs={'type': 'number', 'class':'form-control'}))
    entry_work = forms.CharField(
        label='Entrada de trabajo', widget=forms.TextInput(attrs={'type': 'date', 'class': 'form-control'}))
    period = forms.CharField(
        label='Periodo', widget=forms.TextInput(attrs={'type': 'number', 'class':'form-control'}))
    employee = forms.ModelChoiceField(label='Empleado', empty_label='Seleccione', queryset=Employee.objects.all(), widget=forms.Select(attrs={'class':'form-select'}))

class JefaturaForm(forms.ModelForm):

    class Meta:
        model = Jefatura
        fields = ('__all__')
    
    description = forms.CharField(
        label='Descripcion', widget=forms.TextInput(attrs={'class': 'form-control'}))

class PenaltyForm(forms.ModelForm):
    class Meta:
        model = Penalty
        fields = ('__all__')
    hours_penalty = forms.CharField(
        label='Horas a penalizar', widget=forms.TextInput(attrs={'type': 'number', 'class': 'form-control', 'list':'datalistOptions'}))

    date = forms.CharField(
    label='Fecha', widget=forms.TextInput(attrs={'type': 'date' , 'class': 'form-control'}))

    observations = forms.CharField(
        label='Observaciones', widget=forms.TextInput(attrs={'class': 'form-control'}))

    requirement = forms.ModelChoiceField(label='Requerimientos', empty_label='Seleccione', queryset=Requirements.objects.all().order_by("-code"), widget=forms.Select(attrs={'class':'form-select'}))