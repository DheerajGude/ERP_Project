from rest_framework import serializers
from erp_analytics.models.finance import Transaction

class FinanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'
