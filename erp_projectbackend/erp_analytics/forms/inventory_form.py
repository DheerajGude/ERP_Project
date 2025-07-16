from django import forms
from erp_analytics.models.inventory import InventoryItem

class InventoryItemForm(forms.ModelForm):
    class Meta:
        model = InventoryItem
        fields = '__all__'  # or list only correct fields like ['sku', 'quantity_in_stock']

