from django import forms
from .models import Portfolio


class ProductForm(forms.ModelForm):
    class Meta:
        model = Portfolio
        fields = ['company_name', 'value', 'shares']
        widgets = {
            'company_name': forms.TextInput(attrs={'class': 'form-control'}),
            'value': forms.TextInput(attrs={'class': 'form-control'}),
            'shares': forms.TextInput(attrs={'class': 'form-control'}),


        }
