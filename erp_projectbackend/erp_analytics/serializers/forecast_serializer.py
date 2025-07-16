from rest_framework import serializers
from erp_analytics.models.forecast import Forecast

class ForecastSerializer(serializers.ModelSerializer):
    class Meta:
        model = Forecast
        fields = '__all__'
