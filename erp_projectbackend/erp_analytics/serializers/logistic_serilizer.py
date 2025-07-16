from rest_framework import serializers
from erp_analytics.models.logistics import Shipment

class LogisticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shipment
        fields = '__all__'
