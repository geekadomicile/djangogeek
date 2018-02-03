from django import forms
from .models import Purchase, PurchaseLine
from django.forms import inlineformset_factory

class PurchaseForm(forms.ModelForm):
    class Meta:
        model = Purchase
        exclude = ()

PurchaseFormSet = inlineformset_factory(Purchase, PurchaseLine, form=PurchaseForm, extra=5)
