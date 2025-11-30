from django import forms
from .models import BillingDetails

class BillingDetailsForm(forms.ModelForm):
    class Meta:
        model = BillingDetails
        fields = [
            'first_name',
            'last_name',
            'company_name',
            'address',
            'town',
            'country',
            'postcode',
            'mobile',
            'email'
        ]