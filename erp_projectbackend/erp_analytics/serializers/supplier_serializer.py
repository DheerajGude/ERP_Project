from rest_framework import serializers
from erp_analytics.models.supplier import Supplier

class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'
