from django import forms
from erp_analytics.models.logistics import Logistics, Vehicle

class LogisticsForm(forms.ModelForm):
    class Meta:
        model = Logistics
        fields = ['shipment_id', 'origin', 'destination', 'status']

class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = ['vehicle_id', 'vehicle_type', 'plate_number', 'driver_name', 'capacity', 'status']
