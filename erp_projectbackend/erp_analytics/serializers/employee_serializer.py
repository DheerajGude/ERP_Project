from rest_framework import serializers
from erp_analytics.models.employee import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'
