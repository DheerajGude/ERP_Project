from rest_framework import serializers
from erp_analytics.models.sales import Sales

class SaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sales
        fields = '__all__'
