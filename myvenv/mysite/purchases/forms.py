from django import forms
from .models import Purchase

class PurchaseForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = (
            'file_name',
            'supplier_name',
            'order_number',
            'file_path',
            'details',
            'purchase_date',
            'net_paid',
            'included_vat',
            'currency',
            'vat_rate',
            'currency_to_EUR_rate',
            )
