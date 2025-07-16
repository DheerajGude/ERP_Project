from django import forms
from erp_analytics.models.sales import SalesOrder    # or Quotation etc.


class SaleForm(forms.ModelForm):
    class Meta:
        model = SalesOrder
        fields = ['customer', 'product', 'quantity', 'price']

