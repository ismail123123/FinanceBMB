from django import forms
from .models import Portfolio


class ProductForm(forms.ModelForm):
    class Meta:
        model = Portfolio
        fields = ['company_name', 'value']
        widgets = {
            'company_name':
                forms.TextInput(attrs={'class':'form-control'}),
            'value': forms.TextInput(attrs={'class': ' form-control'})

        }
