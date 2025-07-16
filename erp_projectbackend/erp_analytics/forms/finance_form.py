from django import forms
from erp_analytics.models.finance import Finance, Invoice

class FinanceForm(forms.ModelForm):
    class Meta:
        model = Finance
        fields = ['revenue', 'expense', 'date']

class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ['customer', 'amount', 'due_date', 'status']
