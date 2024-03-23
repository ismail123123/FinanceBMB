from django import forms
from .models import Portfolio
from yfinance import Ticker

class ProductForm(forms.ModelForm):
    class Meta:
        model = Portfolio
        fields = ['company_name', 'value', 'shares']
        widgets = {
            'company_name': forms.TextInput(attrs={'class': 'form-control'}),
            'value': forms.TextInput(attrs={'class': 'form-control'}),
            'shares': forms.TextInput(attrs={'class': 'form-control'}),


        }

class CompanySearchForm(forms.Form):
    company_name = forms.CharField(label='Company Name', max_length=100)

    def clean_company_name(self):
        company_name = self.cleaned_data['company_name']
        try:
            Ticker(company_name)
        except Exception as e:
            raise forms.ValidationError(f"Invalid company name: {e}")
        return company_name