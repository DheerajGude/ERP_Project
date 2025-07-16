from django import forms
from erp_analytics.models.employee import Employee, AttendanceRecord

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'email', 'role', 'date_joined']

class AttendanceForm(forms.ModelForm):
    class Meta:
        model = AttendanceRecord
        fields = ['employee', 'date', 'status']
